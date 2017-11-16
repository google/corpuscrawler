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
from corpuscrawler.util import clean_paragraphs, crawl_udhr, extract


def crawl(crawler):
    out = crawler.get_output(language='iu')
    crawl_udhr(crawler, out, filename='udhr_ike.txt')
    _crawl_gov_nu_ca(crawler, out)


def _crawl_gov_nu_ca(crawler, out):
    site = 'https://www.gov.nu.ca/iu/news'
    index = crawler.fetch_content(site)
    last = max([int(m) for m in re.findall(r'/iu/news\?page=(\d+)', index)])
    seeds = [site] + [site + '?page=%d' % p for p in range(1, last + 1)]
    urls = set()
    for seed in seeds:
        page = crawler.fetch_content(seed)
        for path in re.findall(r'<a href="(/iu/[^"]+)">Read More', page):
            urls.add('https://www.gov.nu.ca' + path)
    for url in sorted(urls):
        page = crawler.fetch_content(url)
        pubdate = re.search(
            r'"dc:date" datatype="xsd:dateTime" content="([^"]+)"', page)
        pubdate = pubdate.group(1) if pubdate else None
        text = extract('<a id="main-content">', '<div id="footer-top">', page)
        text = text.split('<p>###')[0]
        paras = clean_paragraphs(text)
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')
