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
    crawl_deutsche_welle, crawl_udhr, extract, clean_paragraphs, urlpath
)

def crawl(crawler):
    out = crawler.get_output(language='pl')
    crawl_udhr(crawler, out, filename='udhr_pol.txt')
    #crawl_deutsche_welle(crawler, out, prefix='/pl/')
    crawl_pl_usembassy_gov(crawler)

def crawl_pl_usembassy_gov(crawler):
    top_sitemap = crawler.fetch_sitemap('https://pl.usembassy.gov/sitemap_index.xml')
    pubdate_regex = re.compile(
        r'<meta property="article:published_time" content="([^"]*)"'
    )
    links = set()
    for sm_url in sorted(top_sitemap.keys()):
        sitemap = crawler.fetch_sitemap(sm_url)
        for key in sitemap.keys():
            if 'pl.usembassy.gov/pl' in urlpath(key).startswith('/pl/'):
                links.add(key)
    for link in sorted(links):
        result = crawler.fetch(link)
        if result.status != 200:
            continue
        html = result.content.decode('utf-8')
        title = extract('<title>', '</title>', html)
        title = title if title else ''
        title = title.split(' | ')[0] if ' | ' in title else title
        pubdate_match = pubdate_regex.search(html)
        pubdate = pubdate_match.group(1) if pubdate_match else None
        if pubdate is None: pubdate = fetchresult.headers.get('Last-Modified')
        if pubdate is None: pubdate = sitemap[url]
        content = extract('<div class="entry-content">',
            '<!-- AddThis Advanced Settings above via filter on the_content -->')
        paras = clean_paragraphs(title + '<p/>' + content)
        if paras:
            out.write('# Location: %s\n' % link)
            out.write('# Genre: Diplomatic')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')

