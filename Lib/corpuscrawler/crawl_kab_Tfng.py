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
import re
from corpuscrawler.util import clean_paragraphs, crawl_udhr, extract, urlencode


def crawl(crawler):
    out = crawler.get_output(language='kab-Tfng')
    _crawl_aps_dz(crawler, out)


_FRENCH_MONTHS = {
    'janvier': 1,
    'février': 2,
    'mars': 3,
    'avril': 4,
    'mai': 5,
    'juin': 6,
    'juillet': 7,
    'août': 8,
    'septembre': 9,
    'octobre': 10,
    'novembre': 11,
    'décembre': 12
}


def _crawl_aps_dz(crawler, out):
    urls = set()
    for category in ['algerie', 'economie', 'societe', 'culture', 'sport',
                     'monde', 'regions', 'sante-sciences-tech']:
        category_url = 'http://tamazight.aps.dz/' + category
        category_html = crawler.fetch_content(category_url)
        starts = re.findall(r'/%s\?start=(\d+)' % category, category_html)
        last_page = max([int(x) for x in starts])
        for p in range(0, last_page + 1, 10):
            html = crawler.fetch_content(category_url + '?start=%d' % p)
            for u in re.findall(r'href="(/%s/[^"]+)"' % category, html):
                urls.add('http://tamazight.aps.dz' + u)
    for url in sorted(urls):
        doc = crawler.fetch(urlencode(url))
        if doc.status != 200:
            continue
        html = doc.content.decode('utf-8')
        pubdate = extract('<span class="itemDateCreated">', '</span>', html)
        pubdate = re.search(
              '(\d{1,2}) ([a-zA-Zéû]+) (20\d{2}) (\d{2}):(\d{2})',
              pubdate or '')
        if pubdate:
            day, month, year, hour, minute = pubdate.groups()
            month = _FRENCH_MONTHS[month]
            pubdate = '%04d-%02d-%02dT%02d:%02d:00Z' % (
                int(year), month, int(day), int(hour), int(minute))
        title = extract('<h2 class="itemTitle">', '</h2>', html) or ''
        content = extract('<div class="itemFullText">',
                          '<div class="itemContentFooter">', html) or ''
        paras = clean_paragraphs('<p/>'.join([title, content]))
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')
