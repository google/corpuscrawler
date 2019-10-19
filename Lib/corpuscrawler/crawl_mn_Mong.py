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
from datetime import datetime
import json
import re
from corpuscrawler.util import (
    clean_paragraphs, crawl_udhr, extract, urljoin, unichr
)


def crawl(crawler):
    out = crawler.get_output(language='mn-Mong')
    crawl_udhr(crawler, out, filename='udhr_khk_mong.txt')
    # TODO: _crawl_news_mn(crawler, out)


def _crawl_news_mn(crawler, out):
    index = crawler.fetch_content(
        'https://www.news.mn/api/v1/mongo/getNewsByLang?id=3')
    for i in sorted(set(item['newsId'] for item in json.loads(index))):
        url = 'https://www.news.mn/api/v1/news/%d/-1' % i
        doc = json.loads(crawler.fetch_content(url))
        pubDate = doc.get('publishDate', doc.get('createdAt'))
        if pubDate:
            pubDate = datetime.utcfromtimestamp(pubDate/1000.0).isoformat()
        title = doc.get('title', '')
        html = '<h1>%s</h1>%s' % (doc.get('title', ''),
                                  doc.get('infoHtml', ''))
        text = '\n'.join(clean_paragraphs(html))
        text = ''.join([QAGAN_CHARMAP.get(c, '') for c in text])
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubDate:
            out.write('# Publication-Date: %sZ\n' % pubDate)
        out.write(text + '\n')

# Mapping table to work around broken font encoding.
# Original font: https://www.news.mn/modules/core/font/Qagan.woff
QAGAN_CHARMAP = {
    '\uE235': '\u1801',  # MONGOLIAN ELLIPSIS
    '\uE236': '\u1802',  # MONGOLIAN COMMA
    '\uE237': '\u1803',  # MONGOLIAN FULL STOP
    '\uE238': '\u1804',  # MONGOLIAN COLON
    '\uE239': '\u1805',  # MONGOLIAN FOUR DOTS
    '\uE23A': '\u1806',  # MONGOLIAN TODO SOFT HYPHEN
    '\uE23B': '\u1807',  # MONGOLIAN SIBE SYLLABLE BOUNDARY MARKER
    '\uE23C': '\u1808',  # MONGOLIAN MANCHU COMMA
    '\uE23D': '\u1809',  # MONGOLIAN MANCHU FULL STOP
    '\uE23E': '\u180A',  # MONGOLIAN MANCHU NIRUGU
    '\uE244': '\u1810',  # MONGOLIAN DIGIT ZERO
    '\uE245': '\u1811',  # MONGOLIAN DIGIT ONE
    '\uE246': '\u1812',  # MONGOLIAN DIGIT TWO
    '\uE247': '\u1813',  # MONGOLIAN DIGIT THREE
    '\uE248': '\u1814',  # MONGOLIAN DIGIT FOUR
    '\uE249': '\u1815',  # MONGOLIAN DIGIT FIVE
    '\uE24A': '\u1816',  # MONGOLIAN DIGIT SIX
    '\uE24B': '\u1817',  # MONGOLIAN DIGIT SEVEN
    '\uE24C': '\u1818',  # MONGOLIAN DIGIT EIGHT
    '\uE24D': '\u1819',  # MONGOLIAN DIGIT NINE
    '\uE264': '\u1820',        # MONGOLIAN LETTER A
    '\uE265': '\u1821',        # MONGOLIAN LETTER E
    '\uE266': '\u1821\u180B',  # MONGOLIAN LETTER E (second form, initial)
    '\uE267': '\u1821',        # MONGOLIAN LETTER E (first form, initial)
    '\uE268': '\u1821',        # MONGOLIAN LETTER E (first form, final)
    '\uE269': '\u1821\u180B',  # MONGOLIAN LETTER E (second form, final)
    '\uE26A': '\u1821\u180B',  # MONGOLIAN LETTER E (second form, final)
    '\uE26B': '\u1821\u180B',  # MONGOLIAN LETTER E (second form, final)

    # TODO: Add missing entries.

    '\uE24E': '\u2048',  # QUESTION EXCLAMATION MARK
    '\uE24F': '\u2049',  # EXCLAMATION QUESTION MARK
    '\uE250': '!',
    '\uE251': '?',
    '\uE252': ';',
    '\uE253': '(',
    '\uE254': ')',

    # TODO: Add missing entries.

    '\uE263': ' ',
}

for c in range(1, 256):
    QAGAN_CHARMAP[unichr(c)] = unichr(c)
