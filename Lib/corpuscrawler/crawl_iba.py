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
from corpuscrawler.util import (
    clean_paragraphs, crawl_bibleis, extract, urljoin
)


def crawl(crawler):
    out = crawler.get_output(language='iba')
    crawl_bibleis(crawler, out, bible='IBATIV')
    _crawl_utusan_borneo_berita_iban(crawler, out)


def _crawl_utusan_borneo_berita_iban(crawler, out):
    for url in sorted(_find_urls_utusan_borneo_berita_iban(crawler)):
        doc = crawler.fetch_content(url)
        title = re.search(r'<meta property="og:title" content="(.+?)"', doc)
        title = title.group(1) if title else ''
        paras = clean_paragraphs('<h1>%s</h1>' % title +
                                 extract('<p>', '<footer>', doc))
        pubdate = re.search(
            r'<meta property="article:published_time" content="([\d\-]+)"',
            doc)
        pubdate = pubdate.group(1) if pubdate else None
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')


def _find_urls_utusan_borneo_berita_iban(crawler):
    urls = set()
    main = crawler.fetch_content('http://www.utusanborneo.com.my/iban')
    num_pages = max(map(int, re.findall('\?page=(\d+)', main)))
    for p in range(0, num_pages):
        index_url = 'http://www.utusanborneo.com.my/iban'
        if p > 0:
            index_url = index_url + '?page=%d' % p
        for url in re.findall(r'href="(/\d{4}/\d{2}/\d{2}/[^"]+)"',
                              crawler.fetch_content(index_url)):
            urls.add(urljoin(index_url, url))
    return urls
