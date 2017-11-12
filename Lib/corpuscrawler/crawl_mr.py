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
from corpuscrawler.util import cleantext, crawl_udhr, extract


def crawl(crawler):
    out = crawler.get_output(language='mr')
    crawl_udhr(crawler, out, filename='udhr_mar.txt')
    crawl_loksatta_com(crawler, out)


def crawl_loksatta_com(crawler, out):
    sitemap = crawler.fetch_sitemap('http://www.loksatta.com/sitemap.xml')
    for url in sorted(sitemap):
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        try:
            html = doc.content.decode('utf-8')
        except UnicodeDecodeError:
            continue
        pubdate = re.search(
            r'<meta itemprop="datePublished" content="(.+?)"', html)
        pubdate = cleantext(pubdate.group(1)) if pubdate else None
        headline = extract('<h1 itemprop="headline" id="headline">', '</h1>',
                           html)
        synopsis = extract('<h2 itemprop="description" class="synopsis">',
                           '</h2>', html)
        text = extract('itemprop="articleBody">', '<div', html)
        if not text:
            continue
        text = text.replace('\n', ' ')
        text = re.sub(r'</?(?:br|BR|p|P)\s*?/?>', '\n', text)
        paras = [headline, synopsis] + text.splitlines()
        paras = filter(None, [cleantext(p) for p in paras])
        if paras:
            out.write('# Location: %s\n# Genre: News\n' % url)
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')
