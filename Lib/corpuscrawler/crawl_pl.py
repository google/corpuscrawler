# coding: utf-8
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
    crawl_deutsche_welle, crawl_udhr, extract, cleantext, clean_paragraphs, urlpath
)

def crawl(crawler):
    out = crawler.get_output(language='pl')
    crawl_udhr(crawler, out, filename='udhr_pol.txt')
    crawl_deutsche_welle(crawler, out, prefix='/pl/')
    crawl_pl_usembassy_gov(crawler, out)

def _pl_usembassy_gov_path(url):
    if not urlpath(url).startswith('/pl/'):
        return False
    else:
        if urlpath(url) == '/pl/':
            return False
        elif urlpath(url).startswith('/pl/category/'):
            return False
        elif urlpath(url).startswith('/pl/tag/'):
            return False
        else:
            return True

def crawl_pl_usembassy_gov(crawler, out):
    sitemap = crawler.fetch_sitemap('https://pl.usembassy.gov/sitemap_index.xml')
    trans_regex = re.compile(
        r'<h3>Tłumaczenie</h3><div class="translations_sidebar"><ul><li><a href ?="([^"]*)"'
    )
    pubdate_regex = re.compile(
        r'<meta property="article:published_time" content="([^"]*)"'
    )
    links = set()
    for key in sorted(sitemap.keys()):
        if _pl_usembassy_gov_path(key):
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
        trans_match = trans_regex.search(html)
        trans = trans_match.group(1) if trans_match else None
        if pubdate is None: pubdate = result.headers.get('Last-Modified')
        if pubdate is None: pubdate = sitemap[link]
        exstart = '<div class="entry-content">'
        exstart2 = '<div class="mo-page-content">'
        exend = '<!-- AddThis Advanced Settings above via filter on the_content -->'
        exstart = exstart2 if exstart2 in html else exstart
        content = extract(exstart, exend, html)
        cleanparas = clean_paragraphs(content) if content else None
        # Don't repeat the title if it's the only text content
        cleantitle = cleantext(title)
        if cleanparas:
            if len(cleanparas) == 1 and cleanparas[0] == cleantitle:
                paras = [cleantitle]
            else:
                paras = [cleantitle] + cleanparas
        else:
            paras = [cleantitle]
        # There are quite a few media pages whose only text is the filename
        # this, conveniently, is typically also the post's name
        if len(paras) == 1 and paras[0].lower() in urlpath(link).lower():
            continue
        if paras:
            out.write('# Location: %s\n' % link)
            out.write('# Genre: Diplomatic\n')
            if trans:
                out.write('# Translation: %s\n' % trans)
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')

