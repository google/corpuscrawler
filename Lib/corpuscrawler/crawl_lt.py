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
from corpuscrawler.util import clean_paragraphs, cleantext, crawl_udhr, extract


def crawl(crawler):
    out = crawler.get_output(language='lt')
    crawl_udhr(crawler, out, filename='udhr_lit.txt')
    _crawl_kauno_diena_lt(crawler, out)


def _crawl_kauno_diena_lt(crawler, out):
    urls = {}
    for i in range(1, 6):
        url = 'http://kauno.diena.lt/sitemap/kd/sitemap%d.xml' % i
        urls.update(crawler.fetch_sitemap(url))
    for url in sorted(urls):
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        try:
            html = doc.content.decode('utf-8')
        except UnicodeDecodeError:
            continue
        title = extract('<h1 class="title" id="page-title">', '</h1>', html)
        title = cleantext(title if title else '')
        body = extract("<span itemprop='articleBody'>", '</div>', html) or ''
        paras = []
        for p in clean_paragraphs('%s<br/>%s' % (title, body)):
            if 'MicrosoftInternetExplorer4' in p:
                break
            paras.append(p)
        pubdate = re.search(
            r'<span\s+property="dc:date\s+dc:created"\s+content="(20[^"]+)"',
            html)
        pubdate = pubdate.group(1) if pubdate else None
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')
