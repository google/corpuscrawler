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
    clean_paragraphs, crawl_udhr, extract, urlencode
)


def crawl(crawler):
    out = crawler.get_output(language='os')
    crawl_udhr(crawler, out, filename='udhr_oss.txt')
    _crawl_raestdzinad_ru(crawler, out)


def _crawl_raestdzinad_ru(crawler, out):
    urls = crawler.fetch_sitemap(
        urlencode('https://растдзинад.рф/sitemap_index.xml'))
    for url in sorted(urls):
        if re.search(r'/20\d{2}/', url) is None:
            continue
        html = crawler.fetch_content(url)
        title = extract('<h1 class="entry-title">', '</h1>', html) or ''
        text = extract('<div class="td-post-content">', '<footer>', html) or ''
        text = text.split('<div class = "evc-social-likes"')[0]
        pubdate = re.search(
            r'<meta property="article:published_time" content="([^"]+)"', html)
        if pubdate:
            pubdate = pubdate.group(1)
        paras = clean_paragraphs('%s<p/>%s' % (title, text))
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')
