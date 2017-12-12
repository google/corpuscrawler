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
from corpuscrawler.util import clean_paragraphs, crawl_udhr, extract, urlencode


def crawl(crawler):
    out = crawler.get_output(language='nl')
    crawl_udhr(crawler, out, filename='udhr_nld.txt')
    _crawl_telegraaf_nl(crawler, out)


def _crawl_telegraaf_nl(crawler, out):
    sitemap = crawler.fetch_sitemap(
        'http://www.telegraaf.nl/sitemap.xml',
        subsitemap_filter=_should_fetch_telegraaf_sitemap)
    for url in sorted(sitemap):
        doc = crawler.fetch(urlencode(url))
        if doc.status != 200:
          continue
        html = doc.content.decode('utf-8')
        title = re.search(
            r'<meta [a-zA-Z\-="]* property="og:title" content="(.+?)"', html)
        title = title.group(1) if title else ''
        pubdate = re.search(r'"publishDate":"([^"]+)"', html)
        pubdate = pubdate.group(1) if pubdate else None
        text = extract(
            'data-element="ArticlePage-intro">',
            '<div class="flex" data-element="ArticlePage-socialShare-root">',
            html) or ''
        paras = clean_paragraphs(title + '<br/>' + text)
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')


def _should_fetch_telegraaf_sitemap(url):
    """Decide if we should fetch a sub-sitemap from telegraaf.nl.

    Their main sitemap refers to sub-sitemaps which do not actually exist.
    """
    year, month = url.split('/')[-2:]
    year = int(year)
    return year > 2008 or (year == 2008 and month in ('oct', 'nov', 'dec'))
