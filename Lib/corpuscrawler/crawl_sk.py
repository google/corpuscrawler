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
    out = crawler.get_output(language='sk')
    crawl_udhr(crawler, out, filename='udhr_slk.txt')
    _crawl_pravda_sk(crawler, out)


def _crawl_pravda_sk(crawler, out):
    for url in sorted(_find_urls_on_pravda_sk(crawler)):
        doc = crawler.fetch_content(url)
        title = re.search(r'<h1[^>]*>(.+?)</h1>', doc)
        title = title.group(1) if title else ''
        pubdate = re.search(
            '<meta property="article:published_time" content="(.+?)"', doc)
        pubdate = pubdate.group(1) if pubdate else None
        text = extract('<div class="article-detail-perex">',
                       '<div class="clearfix">', doc) or ''
        paras = clean_paragraphs(title + '<br/>' + text)
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        out.write('\n'.join(paras) + '\n')


def _find_urls_on_pravda_sk(crawler):
    # The sitemap only contains seed pages.
    seeds = crawler.fetch_sitemap('https://www.pravda.sk/sitemap.xml')
    processed = set()
    urls = set()
    for seed_url in sorted(seeds):
        url = seed_url
        while url and url not in processed:
            processed.add(url)
            doc = crawler.fetch(url)
            if doc.status != 200:
                continue
            page = doc.content.decode('utf-8')
            for html in re.findall(
                    r'<div class="article-listing(.+?)</div>', page,
                    flags=re.DOTALL):
                link = re.search(r'<a href="(.+?)"', html)
                if link and link.group(1).startswith('https://'):
                    urls.add(link.group(1))
            url = re.search('<li class="next"><a href="(.+?)"', page)
            url = url.group(1) if url else ''
            if not url.startswith('http'):
                url = 'https://www.pravda.sk/' + url
    return urls
