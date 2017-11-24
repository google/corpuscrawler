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
from corpuscrawler.util import clean_paragraphs, crawl_udhr, extract, urlencode


def crawl(crawler):
    out = crawler.get_output(language='sah')
    crawl_udhr(crawler, out, filename='udhr_sah.txt')
    _crawl_kyym_ru(crawler, out)


def _crawl_kyym_ru(crawler, out):
    index = crawler.fetch_content('http://www.kyym.ru/')
    last = max([int(s) for s in re.findall(
        r'href="/index\.php\?start=(\d+?)"', index)])
    urls = set()
    for page in range(1, last + 1):
        doc = crawler.fetch_content(
            'http://www.kyym.ru/index.php?start=%d' % page)
        for path in re.findall(r'<a href="(/index\.php\?view=article&[^"]+?)"',
                              doc):
            urls.add('http://www.kyym.ru' + path.replace('&amp;', '&'))
    for url in sorted(urls):
        doc = crawler.fetch_content(url)
        html = extract('<div class="news_item_article">',
                       '<!--end news item -->', doc)
        if not html:
            continue
        paras = clean_paragraphs(html)
        if not paras:
            continue
        pubdate = re.search(r'<span class="createdate"><!-- date and by -->'
                            r'\s*(\d{1,2}).(\d{2}).(20\d{2})', doc,
                            flags = re.DOTALL)
        if pubdate is not None:
            pubdate = '%s-%s-%s' % (pubdate.group(3), pubdate.group(2),
                                    pubdate.group(1))
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        out.write('\n'.join(paras) + '\n')
