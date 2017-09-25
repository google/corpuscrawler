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
from corpuscrawler.util import cleantext


def crawl(crawler):
    out = crawler.get_output(language='kj')
    crawl_kundana(crawler, out)


def crawl_kundana(crawler, out):
    urls = crawler.fetch_sitemap('https://kundana.com.na/sitemap.xml').keys()
    for url in sorted(urls):
	# exclude banners, contact, logout, etc.
        if re.search(r'kundana.com.na/\d{4}/\d{2}/', url) is None:
            continue
        html = crawler.fetch(url).content.decode('utf-8')
        paragraphs = []
        pubdate = re.search(
            r'<meta property="article:published_time" content="(.+?)"', html)
        pubdate = pubdate.group(1) if pubdate else None
        title = re.search(r'<meta property="og:title" content="(.+?)"', html)
        title = title.group(1) if title else ''
        if title and not title.startswith('Kundana Oshiwambo Newspaper'):
            paragraphs.append(title)
        body = html.split('<footer')[0]
        for b in re.findall(r'<p>(.+?)<!-- A generate', body, flags=re.DOTALL):
            paragraphs.extend(b.split('</p>'))
        paragraphs = filter(None, [cleantext(p) for p in paragraphs])
        if paragraphs:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            for p in paragraphs:
                out.write(p + '\n')

