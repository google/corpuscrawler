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
from corpuscrawler.util import cleantext, crawl_udhr, find_wordpress_urls


def crawl(crawler):
    out = crawler.get_output(language='dz')
    crawl_udhr(crawler, out, filename='udhr_dzo.txt')
    crawl_kuensel(crawler, out)


def crawl_kuensel(crawler, out):
    urls = find_wordpress_urls(crawler, 'http://www.dzkuensel.com/')
    urls = [u for u in urls if '%' in u]
    for url in sorted(urls):
        doc = crawler.fetch(url)
        assert doc.status == 200, (doc.status, url)
        html = doc.content.decode('utf-8')
        title = re.search(r'<h1[^>]*>(.+?)</h1>', html).group(1)
        pubdate = re.search(r'"datePublished":"(.+?)"', html)
        pubdate = cleantext(pubdate.group(1)) if pubdate else None
        text = html.split('<div class="entry">', 1)[1].split('<!-- .entry ')[0]
        text = text.replace('\n', ' ').replace('</p>', '\n')
        paras = [cleantext(p) for p in [title] + text.splitlines()]
        paras = filter(None, paras)
        if any(p.startswith('Search for') for p in paras):
            continue
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        out.write('\n'.join(paras) + '\n')
