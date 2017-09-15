# -*- coding: utf-8 -*-
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
from corpuscrawler.util import crawl_udhr, replace_html_entities, striptags


def crawl(crawler):
    out = crawler.get_output(language='shn')
    crawl_udhr(crawler, out, filename='udhr_shn.txt')
    crawl_panglong(crawler, out)


def crawl_panglong(crawler, out):
    urls = set()
    extract_urls = lambda h: re.findall(r'http://panglong.org/\?p=[0-9]+', h)
    for cat in range(1, 20):
        caturl = 'http://panglong.org/?cat=%d' % cat
        page = crawler.fetch(caturl)
        if page.status != 200:
            continue
        urls.update(extract_urls(page.content))
        pageids = re.findall(r';paged=([0-9]+)', page.content)
        if len(pageids) > 0:
            for pageid in range(2, max([int(p) for p in pageids]) + 1):
                cpurl = 'http://panglong.org/?cat=%d&paged=%d' % (cat, pageid)
                page = crawler.fetch(cpurl)
                if page.status == 200:
                    urls.update(extract_urls(page.content))
    for url in urls:
        try:
            html = crawler.fetch(url).content.decode('utf-8')
        except UnicodeDecodeError:  # a handful of documents are invalid utf8
            continue
        pubdate = re.search(r'<meta itemprop="datePublished" content="(.+)?"',
                            html)
        if pubdate is not None:
            pubdate = pubdate.group(1).strip()
        title = re.search(r'<meta property="og:title" content="(.+?)"', html)
        paras = []
        if title is not None:
            paras.append(title.group(1).strip())
        if html.find('class="entry-content">') > 0:
            text = html.split('class="entry-content">')[1]
            text = text.split('<div')[0]
            for p in text.split('</p>'):
                p = ' '.join(striptags(replace_html_entities(p)).split())
                if p:
                    paras.append(p)
        if len(paras) == 0:
            continue
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        for p in paras:
            out.write(p + '\n')
