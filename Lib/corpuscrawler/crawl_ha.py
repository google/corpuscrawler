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
from corpuscrawler.util import cleantext, crawl_bbc_news, crawl_udhr


def crawl(crawler):
    out = crawler.get_output(language='ha')
    crawl_udhr(crawler, out, filename='udhr_hau_NG.txt')
    crawl_naij(crawler, out)


def crawl_naij(crawler, out):
    urls = crawler.fetch_sitemap(
        'https://hausa.naij.com/naij/sitemap/hausa/sitemap.xml').keys()
    urls = sorted([u for u in urls if u.find('hausa') > 0])
    for url in urls:
        doc = crawler.fetch(url).content.decode('utf-8')
        doc = re.sub(r'<script>.+?</script>', '', doc, flags=re.DOTALL)
        pubdate = re.search(r'<meta itemprop="datePublished" content="(.+?)"',
                            doc).group(1)
        title = cleantext(
            re.search(r'<h1.*?>(.+?)</h1>', doc, re.DOTALL).group(1))
        article = '<article' + doc.split('<article')[1].split('<p>Source:')[0]
        paragraphs = [title]
        for text in article.split('</p>'):
            text = cleantext(text)
            if text:
                paragraphs.append(text)
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        out.write('# Publication-Date: %s\n' % pubdate)
        for p in paragraphs:
            out.write(p + '\n')
