# coding: utf-8
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, print_function, unicode_literals
from datetime import date
import re
import subprocess
from corpuscrawler.util import clean_paragraphs, daterange, extract


def crawl(crawler):
    out = crawler.get_output(language='sat-Olck')
    _crawl_asymptotejournal_com(crawler, out)
    _crawl_disom_khobor(crawler, out)
    _crawl_khoborkagoj_com(crawler, out)


def _crawl_asymptotejournal_com(crawler, out):
    url = ('https://www.asymptotejournal.com/nonfiction/'
           'shibu-tudu-memories-of-the-kirta-dangra/santhali/')
    html = crawler.fetch_content(url)
    content = extract('<!-- article content -->',
                      '<img src="/images/end-logo-black.gif"', html)
    out.write('# Location: %s\n' % url)
    out.write('# Genre: Fiction\n')
    paras = clean_paragraphs(content)
    paras = [p for p in paras if p[0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    out.write('\n'.join(paras) + '\n')


def _crawl_disom_khobor(crawler, out):
    for url in sorted(set(re.findall(
            r'http://wesanthals.tripod.com/(?:disomk02|DK-\d+)/[^"\']+',
            crawler.fetch('http://wesanthals.tripod.com/id43.html').content))):
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        assert 'charset=ISO-8859-1' in doc.content
        html  = extract('sahta 1', '<hr', doc.content.decode('ISO-8859-1'))
        if not html:
            continue
        pubdate = max([_parse_date(d)
                       for d in re.findall(r'\d\d/\d\d/\d{2,4}', html)])
        html = html.replace(' ,', ',').replace(',', ', ')
        html = html.replace('(', ' (').replace(')', ') ')
        html = html.replace(') ,', '),')
        text = '\n'.join([_to_unicode(p) for p in clean_paragraphs(html)])
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        out.write('# Publication-Date: %s\n' % pubdate)
        out.write(text + '\n')


def _crawl_khoborkagoj_com(crawler, out):
    for d in daterange(date(2017, 11, 1), date.today()):
        url = ('http://khoborkagoj.com/wp-content/uploads/'
               '%04d/%02d/%02d%02d%04d.pdf' % (d.year, d.month,
                                               d.day, d.month, d.year))
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        converter = subprocess.Popen(
            ['pdftotext', '-raw', '-', '-'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = converter.communicate(input=doc.content)
        if stderr:
            print(stderr)
            continue
        lines = []
        for line in stdout.decode('iso-8859-1').splitlines():
            line = line.strip()
            if not line or line == '\x0B':
                continue
            word_lengths = [len(w) for w in line.split()]
            if sum(word_lengths) / float(len(word_lengths)) < 2:
                lines.append(''.join(line.split()))  # bogus justification
            else:
                contains_bad = False
                for bad in ('Jamshedpur', 'Printed', 'published', 'from',
                            'gmail', 'yahoo', 'Dishom', 'KHOBOR', 'KAGOJ'):
                    if bad in line:
                        contains_bad = True
                        break
                if not contains_bad:
                    lines.append(line)
        text = _to_unicode(' '.join(lines))
        text = text.replace('- ', '')  # hyphenation
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        out.write('# Publication-Date: %04d-%02d-%02d\n' %
                  (d.year, d.month, d.day))
        out.write(text + '\n')


def _parse_date(s):
    """'31/05/11' --> '2011-05-31'"""
    day, month, year = [int(x) for x in s.split('/')]
    if year < 15:
        year = 2000 + year
    if (year < 2001 or year > 2015):
        return None
    if (month < 1 or month > 12) or (day < 1 or day > 31):
        return None
    return '%04d-%02d-%02d' % (year, month, day)


_CHARMAP = {
  '!': '!',
  '"': '"',
  '#': '#',
  '$': '$',
  '%': '%',
  '&': '&',
  '\'': '\'',
  '(': '(',
  ')': ')',
  '*': '*',
  '+': '+',
  ',': ',',
  '-': '-',
  '.': '.',
  '/': '/',
  ':': ':',
  ';': ';',
  '<': '<',
  '=': '=',
  '>': '>',
  '[': '[',
  ']': ']',
  '^': '^',
  '{': '{',
  '}': '}',
  '0': '᱐',
  '1': '᱑',
  '2': '᱒',
  '3': '᱓',
  '4': '᱔',
  '5': '᱕',
  '6': '᱖',
  '7': '᱗',
  '8': '᱘',
  '9': '᱙',
  '\\': '᱿',
  '?': '?',
  '@': '@',
  'A': 'ᱟ',
  'B': 'ᱵ',
  'C': 'ᱪ',
  'D': 'ᱫ',
  'E': 'ᱮ',
  'F': 'ᱝ',
  'G': 'ᱜ',
  'H': 'ᱷ',
  'I': 'ᱤ',
  'J': 'ᱡ',
  'K': 'ᱠ',
  'L': 'ᱞ',
  'M': 'ᱬ',
  'N': 'ᱸ',
  'O': 'ᱳ',
  'P': 'ᱯ',
  'Q': 'ᱧ',
  'R': 'ᱨ',
  'S': 'ᱥ',
  'T': 'ᱛ',
  'U': 'ᱩ',
  'V': 'ᱶ',
  'W': 'ᱣ',
  'X': 'ᱽ',
  'Y': 'ᱭ',
  'Z': 'ᱲ',
  'a': 'ᱟ',
  'b': 'ᱵ',
  'c': 'ᱪ',
  'd': 'ᱰ',
  'e': 'ᱮ',
  'f': 'ᱝ',
  'g': 'ᱜ',
  'h': 'ᱦ',
  'i': 'ᱤ',
  'j': 'ᱡ',
  'k': 'ᱠ',
  'l': 'ᱞ',
  'm': 'ᱢ',
  'n': 'ᱱ',
  'o': 'ᱚ',
  'p': 'ᱯ',
  'q': 'ᱧ',
  'r': 'ᱨ',
  's': 'ᱥ',
  't': 'ᱴ',
  'u': 'ᱩ',
  'v': 'ᱶ',
  'w': 'ᱣ',
  'x': 'ᱽ',
  'y': 'ᱭ',
  'z': 'ᱲ',
  '|': '᱾',
  '.': '\u1C79',
  '~': '\u1C7B',
  '_': '\u1C7C',
}


def _to_unicode(s):
    s = ''.join([_CHARMAP.get(c, c) for c in s])
    # The font uses : both for an actual colon, and for the modifier letter
    # U+1C7A OL CHIKI MU-GAAHLAA TTUDDAAG. But we can disambiguate them,
    # because the real colon is always preceded by space in the texts.
    s = s.replace(' :', '@@@@@')
    s = s.replace(':', 'ᱺ')
    s = s.replace('@@@@@', ':')
    s = s.replace(':-', ' :- ')
    return ' '.join(s.split())
