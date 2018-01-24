# coding: utf-8
#
# Copyright 2018 Google LLC
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
    clean_paragraphs, crawl_udhr, extract
)


def crawl(crawler):
    out = crawler.get_output(language='oc')
    crawl_udhr(crawler, out, filename='udhr_prv.txt')
    _crawl_lasetmana_fr(crawler, out)


def _crawl_lasetmana_fr(crawler, out):
    for url in sorted(_find_urls_lasetmana_fr(crawler)):
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        html = doc.content.decode('utf-8')
        title = re.search(r'<meta name="title" content="([^"]+)"', html)
        title = title.group(1) if title else ''
        content = extract('<div class="itemFullText">',
                          '<div class="itemLinks">', html)
        paras = clean_paragraphs('<h1>%s</h1>%s' % (title, content))
        if not paras:
            continue
        text = '\n'.join(paras)
        text = text.replace(
            'This email address is being protected from spambots. '
            'You need JavaScript enabled to view it.', '')
        pubdate = re.search(r'<time datetime="([^"]+)"', html)
        pubdate = pubdate.group(1).strip() if pubdate else None
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
          out.write('# Publication-Date: %s\n' % pubdate)
        out.write(text + '\n')


def _find_urls_lasetmana_fr(crawler):
    urls = set()
    for cat in ('internacionau politica societat economia cultura esport '
                'environament educacion santat literatura').split():
        caturl = 'http://lasetmana.fr/index.php/oc/' + cat
        limit = re.search(
            r'<a title="End" href=".+?start=(\d+)" class="pagenav">End</a>',
            crawler.fetch_content(caturl))
        limit = int(limit.group(1)) if limit else 0
        for p in range(0, limit, 8):
            page = crawler.fetch_content(caturl + '?start=%d' % p)
            for u in re.findall(r'(/index\.php/oc/[a-z]+/item/[^"]+)"', page):
                urls.add('http://lasetmana.fr' + u.split('#')[0])
    return urls
