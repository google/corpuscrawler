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
    clean_paragraphs, crawl_udhr, extract, replace_html_entities
)


def crawl(crawler):
    out = crawler.get_output(language='oc')
    crawl_udhr(crawler, out, filename='udhr_prv.txt')
    _crawl_jornalet_com(crawler, out)
    _crawl_lasetmana_fr(crawler, out)


def _crawl_jornalet_com(crawler, out):
    for url in sorted(_find_urls_jornalet_com(crawler)):
        try:
            html = crawler.fetch_content(url)
        except UnicodeDecodeError:
            continue
        title = re.search(r'<meta property="og:title" content="([^"]+)"', html)
        title = title.group(1) if title else ''
        subtitle = extract('<h4 class="subtitol">', '</h4>', html) or ''
        content = extract('<p class="contingut">', '<hr', html) or ''
        paras = clean_paragraphs('\n'.join(
            ['<p>%s</p>' % p for p in (title, subtitle, content) if p]))
        paras = [p for p in paras if p.find('Abonar los amics de Jornalet') < 0]
        if not paras:
            continue
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        out.write('\n'.join(paras) + '\n')


def _find_urls_jornalet_com(crawler):
    urls = set()
    main = crawler.fetch_content('https://www.jornalet.com/actualitats')
    num_pages = max([int(p) for p
                     in re.findall(r'actualitats/pagina/(\d+)"', main)])
    for p in range(1, num_pages + 1):
        index = crawler.fetch_content(
            'https://www.jornalet.com/actualitats/pagina/%d' % p)
        for u in re.findall(r'"(https://www.jornalet.com/nova/[^"]+)"', index):
            url = replace_html_entities(u.split('#')[0])
            url = url.replace(' ', '')
            urls.add(url)
    return urls


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
