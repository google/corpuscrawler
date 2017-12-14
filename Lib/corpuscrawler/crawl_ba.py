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
from corpuscrawler.util import clean_paragraphs, crawl_udhr, extract, \
    urlencode, urljoin, crawl_bibleis


def crawl(crawler):
    out = crawler.get_output(language='ba')
    # As of November 2017, the Unicode UDHR project has no Bashkir translation.
    # crawl_udhr(crawler, out, filename='udhr_bak.txt')
    _crawl_yaikrb_ru(crawler, out)
    crawl_bibleis(crawler, out, 'BAKIBT')


def _crawl_yaikrb_ru(crawler, out):
    urls = set()
    # The site has an incomplete sitemap, so we also look at the archive pages.
    sitemap = crawler.fetch_sitemap('http://yaikrb.ru/sitemap.xml')
    for url in sorted(sitemap):
        crawler.fetch_content(url)
    main = crawler.fetch_content('http://yaikrb.ru/')
    archives = set([str(x) for x in range(1, 150)])
    archives.update(re.findall(r'/xf/num/([^/]+)/', main))
    for a in sorted(archives):
        doc = crawler.fetch(urlencode('http://yaikrb.ru/xf/num/%s/' % a))
        if doc.status != 200:
            continue
        for href in re.findall(r'<div class="n_more"><a href="([^"]+)"',
                               doc.content.decode('utf-8')):
            urls.add(urljoin('http://yaikrb.ru/', href, allow_fragments=False))
    for url in sorted(urls):
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        html = doc.content.decode('utf-8')
        title = re.search('<meta property="og:title" content="([^"]+)"', html)
        title = title.group(1) if title else ''
        text = extract('<div class="n_text">', '<div class="n_oth">', html)
        paras = clean_paragraphs('<h1>' + title + '</h1>' + text)
        if not paras:
            continue
        pubdate = re.search(
            r'<small>(\d{1,2})\.(\d{1,2})\.(20\d{2})\s*</small></h1>', html)
        if pubdate is not None:
            pubdate = '%s-%s-%s' % (pubdate.group(3),
                                    pubdate.group(2), pubdate.group(1))
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        out.write('\n'.join(paras) + '\n')
