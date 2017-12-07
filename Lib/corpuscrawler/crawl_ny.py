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
import os.path
import re

from corpuscrawler.util import crawl_udhr, clean_paragraphs, extract


def crawl(crawler):
    out = crawler.get_output(language='ny')
    crawl_udhr(crawler, out, filename='udhr_nya_chechewa.txt')
    _crawl_mwnation_com(crawler, out)


def _crawl_mwnation_com(crawler, out):
    urls = set()
    index = crawler.fetch_content('http://mwnation.com/section/chichewa/')
    pages = re.findall(r'/section/chichewa/page/(\d+)/', index)
    num_pages = max([int(p) for p in pages])
    for page in range (1, num_pages + 1):
        url = 'http://mwnation.com/section/chichewa/'
        if page > 1:
            url += 'page/%d/' % page
        doc = crawler.fetch_content(url)
        urls.update(re.findall(r'<a href="([^"]+?)">Continue Reading', doc))
    for url in sorted(urls):
        doc = crawler.fetch_content(url)
        pubdate = re.search(
            r'<meta property="article:published_time" content="([^"]+)"', doc)
        pubdate = pubdate.group(1) if pubdate is not None else None
        title = extract('<h1 class="entry-title" itemprop="headline">',
                        '</h1>', doc) or ''
        body = extract('<div class="entry-content" itemprop="articleBody">',
                       '<footer ', doc) or ''
        paras = clean_paragraphs(title + '<br/>' + body)
        text = '\n'.join(paras) + '\n'
        if text.find(' the ') >= 0:  # likely English
            continue
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write(text)
