# coding: utf-8
# Copyright 2017 Google Inc. All rights reserved.
# Copyright 2017 Jim O'Regan
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
import sys

from corpuscrawler.util import crawl_udhr, urlpath


def crawl(crawler):
    out = crawler.get_output(language='ga')
    crawl_udhr(crawler, out, filename='udhr_gle.txt')
    crawl_nuachtrte(crawler, out)
    

# RTE has news sites both for its own Irish language news programme
# and for Raidió na Gaeltachta
def _rtenuacht_path(url):
    rtenuacht = urlpath(url).startswith('/news/nuacht/')
    rnagnuacht = urlpath(url).startswith('/rnag/nuacht-gaeltachta')
    return rtenuacht or rnagnuacht


def crawl_nuachtrte(crawler, out):
    sitemap = crawler.fetch_sitemap(
        'http://www.rte.ie/sitemap-20000.xml',
        subsitemap_filter=lambda s: _rtenuacht_path(s)
        )
    pubdate_regex = re.compile(r'name="DC.date" (?:scheme="DCTERMS.URI" )?content="([0-9T:+\-]{19,25})"')
    for url in sorted(sitemap.keys()):
        fetchresult = crawler.fetch(url)
        if fetchresult.status != 200:
            continue
        html = fetchresult.content.decode('utf-8')
        pubdate_match = pubdate_regex.search(html)
        pubdate = pubdate_match.group(1) if pubdate_match else None
        if pubdate is None: pubdate = fetchresult.headers.get('Last-Modified')
        if pubdate is None: pubdate = sitemap[url]
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate: out.write('# Publication-Date: %s\n' % pubdate)
        title = re.search(r'<title>(.+?)</title>', html)
        if title: title = striptags(title.group(1).split('- RTÉ')[0]).strip()
        if title: out.write(cleantext(title) + '\n')
        for paragraph in re.findall(r'<p>(.+?)</p>', html):
            out.write(cleantext(paragraph) + '\n')


        
