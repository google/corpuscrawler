# coding: utf-8
#
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
from corpuscrawler.util import clean_paragraphs, crawl_udhr, extract


def crawl(crawler):
    out = crawler.get_output(language='sl')
    crawl_udhr(crawler, out, filename='udhr_slv.txt')
    _crawl_dnevnik_si(crawler, out)


def _crawl_dnevnik_si(crawler, out):
    urls = set()
    for url in crawler.fetch_sitemap('https://www.dnevnik.si/sitemap'):
        match = re.search(r'#(\d+)$', url)
        if not match:
            match = re.search(r'dnevnik\.si/(\d+)', url)
        if match:
            urls.add('https://www.dnevnik.si/' + match.group(1))
    for url in sorted(urls):
        doc = crawler.fetch_content(url)
        title = re.search(r'<meta name="og:title" content="(.+?)"', doc)
        title = title.group(1).replace('&amp;', '&') if title else ''
        pubdate = re.search(r'<div class="dtstamp" title="(.+?)">', doc)
        pubdate = pubdate.group(1).strip() if pubdate else None
        text = extract('<div class="article-body article-wrap">',
                       '<div class="article-tags">', doc) or ''
        paras = clean_paragraphs(title + '<br/>' + text.replace('\r', '\n'))
        if not paras:
            continue
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        out.write('\n'.join(paras) + '\n')
