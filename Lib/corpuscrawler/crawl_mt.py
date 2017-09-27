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
from corpuscrawler.util import cleantext, crawl_udhr, fixquotes, urljoin


def crawl(crawler):
    out = crawler.get_output(language='mt')
    crawl_udhr(crawler, out, filename='udhr_mlt.txt')
    crawl_newsbook_mt(crawler, out)


def crawl_newsbook_mt(crawler, out):
    urls = set()
    for section in ('internazzjonali', 'muzika', 'madwar-il-hajja',
                    'teknologijja', 'vatikan', 'sports', 'kummerc'):
        section_url = 'http://www.newsbook.com.mt/artikli/%s/' % section
        html = crawler.fetch(section_url).content.decode('utf-8')
        links = re.findall(r'/artikli/%s/(\d+)/' % section, html)
        num_toc_pages = max([int(x) for x in links])
        for i in range(1, num_toc_pages + 1):
            toc_url = section_url
            if i > 1:
                toc_url = toc_url + '%d/' % i
            html = crawler.fetch(toc_url).content.decode('utf-8')
            for u in re.findall('href="(/artikli/\d{4}/.+?)"', html):
                url = urljoin(toc_url, u)
                if url.find('/test') < 0:
                    urls.add(url)
    for url in sorted(urls):
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        html = doc.content.decode('utf-8')
        title = re.search(r'<meta content="([^"]+?)" name="title"', html)
        if title is not None:
            title = cleantext(title.group(1))
        pubdate = re.search(
            r'<meta content="([^"]+?)" itemprop="datePublished"', html)
        if pubdate is not None:
            pubdate = pubdate.group(1).strip().replace(' ', 'T') + 'Z'
        content = html.split('<p>', 1)[1].split('<div', 1)[0]
        content = content.replace('\n', ' ').replace('</p>', '\n')
        paras = [fixquotes(cleantext(p))
                 for p in [title] + content.splitlines()]
        paras = filter(None, paras)
        if not paras:
            continue
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        for p in paras:
            out.write(p + '\n')
