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
from corpuscrawler.util import cleantext, crawl_udhr, urljoin
import re

def crawl(crawler):
    out = crawler.get_output(language='bm')
    crawl_udhr(crawler, out, filename='udhr_bam.txt')
    crawl_voa_news(crawler, out, site='https://voabambara.com')


def crawl_voa_news(crawler, out, site):
    sitemap = crawler.fetch_sitemap(urljoin(site, 'sitemap.xml'))
    for url in sorted(sitemap.keys()):
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue

        html = doc.content.decode('utf-8')
        title = re.search(r'<title>(.+?)</title>', html)
        if title:
            title = cleantext(title.group(1))
        pubdate = re.search(
            r'<div class="published">\s*<span class="date"\s*>\s*'
            r'<time datetime="(.+?)"', html)
        if pubdate:
            pubdate = cleantext(pubdate.group(1))
            if pubdate.startswith('1900'):
                pubdate = None
        description = re.search(
            r'<meta name="description" content="(.+?)"', html)
        if description:
            description = cleantext(description.group(1))
        paragraphs = filter(None, [title, description])
        if len(paragraphs) == 0:
            continue

        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        for p in paragraphs:
            out.write(p)
            out.write('\n')
