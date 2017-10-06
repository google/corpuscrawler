# coding: utf-8
# Copyright 2017 Google Inc. All rights reserved.
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
import re
import unicodedata
from corpuscrawler.util import cleantext


def crawl(crawler):
    out = crawler.get_output(language='ae')
    out_latin = crawler.get_output(language='ae-Latn')
    crawl_titus_avestan(crawler, out, out_latin)


def crawl_titus_avestan(crawler, out, out_latin):
    for page in range(1, 249):
        url = ('http://titus.uni-frankfurt.de/texte/etcs/iran/airan/avesta/' +
               'avest%03d.htm' % page)
        doc = crawler.fetch(url)
        assert doc.status == 200, (doc.status, url)
        html = doc.content.decode('utf-8')
        for chapter_id, chapter in enumerate(
                re.split('<span id=(?:h3|subtitle)>', html)[1:]):
            chapter = chapter.replace('<SUP>\u030A</SUP>', '\u030A')
            chapter = chapter.replace('<SUP>v</SUP>', '\u1D5B')
            chapter = chapter.replace('β', '\uA7B5')  # LATIN SMALL LETTER BETA
            chapter = chapter.replace('δ', 'ẟ')  # LATIN SMALL LETTER DELTA
            title = re.search(r'<a id=subtitle[^>]*>(.+?)</a>', chapter)
            text = [title.group(1) if title else '']
            for paragraph in chapter.split('Paragraph')[1:]:
                cur_paragraph = []
                for verse in paragraph.split('Verse')[1:]:
                    verse = cleantext(verse.split('>', 1)[1])
                    verse = verse.split('This')[0]
                    verse = re.sub(r'(\s*:+\s*)',
                                   lambda m: ' ' + m.group(1).strip() + ' ',
                                   verse)
                    verse = re.sub('\.{2,}', '…', verse)
                    for c in '+*^':
                        verse = verse.replace(c, ' ')
                    verse = re.sub(r'[\s\.\d]+\)[\s\.]', ') ', verse)
                    verse = re.sub(r'[\s\.\d]+\]\.*', '] ', verse)
                    verse = re.sub(r'\{[^}]+\}', ' ', verse)
                    verse = re.sub(r'\(~[^)]+\)', ' ', verse)
                    verse = re.sub(r'[\s\.\d]*(:+)[\s\.\d]*',
                                   lambda m: m.group(1) + ' ', verse)
                    words = [w.strip('0123456789.') for w in verse.split()]
                    verse = cleantext(' '.join(words)).lower()
                    verse = verse.replace(': :', '::')
                    cur_paragraph.append(verse)
                p = ' '.join(cur_paragraph)
                p = re.sub(r'[^:]::[^:]', '. ', p)
                p = re.sub(r'[^:]::$', '. ', p) + ' '
                sentences = []
                for s in p.split('. '):
                    if len(s) > 1:
                        s = ' '.join(s.split())
                        sentences.append(s[0].title() + s[1:] + '. ')
                p = '. '.join(sentences).strip()
                p = p.replace('. .', '.')
                text.append(unicodedata.normalize('NFC', p))
            paras = filter(None, text)
            out.write('# Location: %s#%d\n' % (url, chapter_id + 1))
            out_latin.write('# Location: %s#%d\n' % (url, chapter_id + 1))
            out_latin.write('\n'.join(paras) + '\n')
            out.write(untransliterate('\n'.join(paras)) + '\n')


_TRANSLIT = {
    ' ': ' ',
    '[': '[',
    ']': ']',
    ':': '\U00010B3A', # TINY TWO DOTS OVER ONE DOT PUNCTUATION
    ';': '\U00010B3B', # SMALL TWO DOTS OVER ONE DOT PUNCTUATION
    '…': '\U00010B39',  # AVESTAN ABBREVIATION MARK
    'a': '\U00010B00',
    'ā': '\U00010B01',
    'å': '\U00010B02',
    'ā̊': '\U00010B03',
    'ą': '\U00010B04',
    'ą̇': '\U00010B05',
    'ə': '\U00010B06',
    'ə̄': '\U00010B07',
    'e': '\U00010B08',
    'ē': '\U00010B09',
    'o': '\U00010B0A',
    'ō': '\U00010B0B',
    'i': '\U00010B0C',
    'ī': '\U00010B0D',
    'u': '\U00010B0E',
    'ū': '\U00010B0F',
    'k': '\U00010B10',
    'x': '\U00010B11',
    'x́': '\U00010B12',
    'xᵛ': '\U00010B13',
    'g': '\U00010B14',
    'ġ': '\U00010B15',
    'γ': '\U00010B16',
    'c': '\U00010B17',
    'j': '\U00010B18',
    't': '\U00010B19',
    'ϑ': '\U00010B1A',
    'd': '\U00010B1B',
    'ẟ': '\U00010B1C',  # LATIN SMALL LETTER DELTA
    'δ': '\U00010B1C',  # GREEK SMALL LETTER DELTA
    't̰': '\U00010B1D',
    'p': '\U00010B1E',
    'f': '\U00010B1F',
    'b': '\U00010B20',
    '\uA7B5': '\U00010B21',  # LATIN SMALL LETTER BETA
    'β': '\U00010B21',  # GREEK SMALL LETTER BETA
    'ŋ': '\U00010B22',
    'ŋ́': '\U00010B23',
    'ŋᵛ': '\U00010B24',
    'n': '\U00010B25',
    'ń': '\U00010B26',
    'ṇ': '\U00010B27',
    'm': '\U00010B28',
    'm̨': '\U00010B29',
    'ẏ': '\U00010B2A',
    'y': '\U00010B2B',
    'ii': '\U00010B0C\U00010B0C',
    'v': '\U00010B2C',
    'uu': '\U00010B0E\U00010B0E',
    'r': '\U00010B2D',
    'l': '\U00010B2E',
    's': '\U00010B2F',
    'z': '\U00010B30',
    'š': '\U00010B31',
    'ž': '\U00010B32',
    'š́': '\U00010B33',
    'ṣ̌': '\U00010B34',
    'h': '\U00010B35',
}


# Sort by reverse length.
_TRANSLITS = sorted(_TRANSLIT.items(), key=lambda x:(-len(x[0]), x[0]))
for latin, _ in _TRANSLITS:
    assert latin == unicodedata.normalize('NFC', latin), latin


def untransliterate(s):
    s = s.lower() + ' '

    # strong end of section = 2x LARGE TWO RINGS OVER ONE RING PUNCTUATION
    s = re.sub(r':::+ ', '\U00010B3E\U00010B3E ', s)

    # end of section = LARGE TWO RINGS OVER ONE RING PUNCTUATION
    s = re.sub(r'::', '\U00010B3E', s)

    s = s.replace('.', '\U00010B3C')  # LARGE TWO DOTS OVER ONE DOT PUNCTUATION
    s = s.replace(' ', '. ')
    s = re.sub(r'([\[\]\(\);:,…])\.', lambda m: m.group(1), s)
    s = s.replace('\U00010B3A.', '\U00010B3A')
    s = s.replace('\U00010B3B.', '\U00010B3B')
    s = s.replace('\U00010B3C.', '\U00010B3C')
    s = s.replace('\U00010B3D.', '\U00010B3D')
    s = s.replace('\U00010B3E.', '\U00010B3E')

    for latin, avestan in _TRANSLITS:
        s = s.replace(latin, avestan)

    return s.strip()
