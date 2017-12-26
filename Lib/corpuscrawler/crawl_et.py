# coding: utf-8
#
# Copyright 2017 Google LLC
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
    clean_paragraphs, crawl_udhr, crawl_sputnik_news, extract
)


def crawl(crawler):
    out = crawler.get_output(language='et')
    crawl_udhr(crawler, out, filename='udhr_est.txt')
    crawl_sputnik_news(crawler, out, host='sputnik-news.ee')
    _crawl_eestikirik_ee(crawler, out)


def _crawl_eestikirik_ee(crawler, out):
    for url in sorted(_find_urls_eestikirik_ee(crawler)):
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        html = doc.content.decode('utf-8')
        title = extract('<h1 class="entry_title">', '</h1>', html) or ''
        entry = extract('<div class="entry">', '<div style="min-height:33px;"',
                        html) or ''
        pubdate = re.search('(\d{1,2})\.(\d{1,2})\.(20\d{2})',
                            extract('<div id="content">', '</small>', html))
        if pubdate is not None:
            pubdate = '%04d-%02d-%02d' % (int(pubdate.group(3)),
                                          int(pubdate.group(2)),
                                          int(pubdate.group(1)))
        paras = clean_paragraphs('%s<br/>%s' % (title, entry))
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')


def _find_urls_eestikirik_ee(crawler):
    urls = set()
    archive = crawler.fetch_content('http://www.eestikirik.ee/arhiiv/')
    for edition_url in re.findall(
            r'href="(http://www.eestikirik.ee/number/2[^/]+/)"', archive):
        edition_index = crawler.fetch_content(edition_url)
        pages = re.findall(edition_url + r'page/(\d+)/', edition_index) or ['1']
        num_pages = max([int(p) for p in pages])
        for page in range(1, num_pages + 1):
            if page == 1:
                index = edition_index
            else:
                index = crawler.fetch_content(edition_url + 'page/%d/' % page)
        for url in re.findall(
                r'<a href="(http://www\.eestikirik\.ee/[^"]+?)" '
                r'class="title" rel="bookmark"', index):
            urls.add(url.replace('&amp;', '&'))
    return urls
