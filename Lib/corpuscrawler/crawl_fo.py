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
from corpuscrawler.util import cleantext, crawl_udhr, urlencode, urlpath


def crawl(crawler):
    out = crawler.get_output(language='fo')
    crawl_udhr(crawler, out, filename='udhr_fao.txt')
    crawl_dimma_fo(crawler, out)


def crawl_dimma_fo(crawler, out):
    num_pages = int(re.search(
        r'<a href="http://www.dimma.fo/(\d+)" class="to-last"',
        crawler.fetch('http://www.dimma.fo/').content).group(1))
    urls = set()
    for i in range(1, num_pages + 1):
        doc = crawler.fetch('http://www.dimma.fo/%d' % i)
        html = doc.content.decode('utf-8')
        for u in re.findall(r'href="(http://www.dimma.fo/[^"]+?)"', html):
            path = urlpath(u)
            if re.match(r'/\d+', path) or u'/' in path[1:]:
                continue
            urls.add(u)
    for url in sorted(urls):
        doc = crawler.fetch(urlencode(url))
        if doc.status != 200:
            continue
        html = doc.content.decode('utf-8')
        content = html.split('class="content">')[1]
        pubdate = re.search(
            r'<span class="date">\s*'
            r'(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2})\s*</span>',
            content)
        if pubdate != None:
            pubdate = '%sT%s:00+01:00' % (pubdate.group(1), pubdate.group(2))
        paragraphs = []
        title = re.search(r'<h1>(.+?)</h1>', html, flags=re.DOTALL)
        if title != None:
            paragraphs.append(cleantext(title.group(1)))
        text = content.split('<p>', 1)[1].split('</div>')[0]
        text = text.replace('\n', ' ').replace('</p>', '\n')
        text = text.replace('<br />', '\n')
        paragraphs.extend([cleantext(p) for p in text.splitlines()])
        paragraphs = filter(None, paragraphs)
        if paragraphs:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            for p in paragraphs:
                out.write(p + '\n')
