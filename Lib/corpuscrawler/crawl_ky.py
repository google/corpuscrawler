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

from corpuscrawler.util import (
    cleantext, crawl_bbc_news, crawl_udhr, extract, urlpath)


def crawl(crawler):
    out = crawler.get_output(language='ky')
    crawl_udhr(crawler, out, filename='udhr_kir.txt')
    crawl_bbc_news(crawler, out, urlprefix='/kyrgyz/')
    crawl_azattyk_org(crawler, out)


def crawl_azattyk_org(crawler, out):
    sitemap = crawler.fetch_sitemap('https://www.azattyk.org/sitemap.xml')
    for url in sorted(sitemap.keys()):
        if not urlpath(url).startswith('/a/'):
            continue
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        html = doc.content.decode('utf-8')
        pubdate = re.search(r'"dateModified":"([^"]+)"', html)
        if pubdate is not None:
            pubdate = cleantext(pubdate.group(1)).replace(' ', 'T')
        title = extract('<title>', '</title>', html)
        text = extract('content-offset">', '<footer', html)
        if not title or not text:
            continue
        text = text.split('<span class="share')[0]
        text = text.split('<div class="region"')[0]
        text = text.replace('\n', ' ')
        paras = [title] + re.sub(r'<(?:br|p|div)\s*?/?>', '\n', text).splitlines()
        paras = filter(None, [cleantext(p.strip()) for p in paras])
        paras = [p for p in paras if not p.startswith('http')]
        if not paras:
            continue
        # Filter out English text.
        if ord(paras[0][0]) <= 0xFF or ord(paras[-1][-1]) <= 0xFF:
            continue
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        for p in paras:
            out.write(p + '\n')
