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
from datetime import datetime


def crawl(crawler):
    unicode_out = crawler.get_output(language='mnw')
    crawl_udhr(crawler, unicode_out, filename='udhr_mnw.txt')
    crawl_mon_news(crawler, unicode_out)


def crawl_mon_news(crawler, out):
    urls = set()
    for year in range(2009, datetime.today().year + 1):
        first_page = crawler.fetch('http://mon.monnews.org/%d/' % year)
        html = first_page.content.decode('utf-8')
        urls.update(extract_mon_news_urls(html))
        num_pages = re.search(
            r'<a href="http://mon.monnews.org/\d+/page/(\d+)/" class="last"',
            html)
        if num_pages != None:
            num_pages = int(num_pages.group(1))
            for page in range(2, num_pages + 1):
                next_page = crawler.fetch(
                    'http://mon.monnews.org/%d/page/%d/' % (year, page))
                if next_page.status != 200:
                    continue
                html = next_page.content.decode('utf-8')
                urls.update(extract_mon_news_urls(html))
    for url in sorted(urls):
        html = crawler.fetch(url.encode('utf-8')).content.decode('utf-8')
        pubdate = re.search(
            r'<meta property="article:published_time" content="(.+?)"',
            html)
        if pubdate is None:
            continue
        pubdate = pubdate.groups(1)
        text = html.split('</section>')[1].split('<div class="sharedaddy')[0]
        text = text.split('Share this:')[0]
        text = text.replace('\n', ' ')
        text = text.replace('</p>', '\n').replace('</div>', '\n')
        paragraphs = []
        for p in text.splitlines():
            p = ' '.join(striptags(replace_html_entities(p)).split())
            if p and '>' not in p:
                paragraphs.append(p)
        if len(paragraphs) > 0:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            out.write('# Publication-Date: %s\n' % pubdate)
            for p in paragraphs:
                out.write(p + '\n')


def extract_mon_news_urls(html):
    prefix = r'http://mon.monnews.org/\d{4}/\d{2}/\d{2}/'
    return set([u.split('#')[0]
                for u in re.findall(r'href="(%s.+?)"' % prefix, html)
                if '%' in u])
