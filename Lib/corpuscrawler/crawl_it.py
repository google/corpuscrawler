# coding: utf-8
#
# Copyright 2017 Google LLC
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
    clean_paragraphs, crawl_udhr, crawl_sputnik_news, extract,
    replace_html_entities, urljoin
)


def crawl(crawler):
    out = crawler.get_output(language='it')
    crawl_udhr(crawler, out, filename='udhr_ita.txt')
    crawl_sputnik_news(crawler, out, host='it.sputniknews.com')
    _crawl_iltirreno_gelocal_it(crawler, out)


def _crawl_iltirreno_gelocal_it(crawler, out):
    urls = set()
    for category in ('italia-mondo', 'focus/toscana-economia',
                     'empoli/cronaca', 'grosseto/cronaca',
                     'livorno/cronaca', 'livorno/dagli-enti',
                     'lucca/cronaca', 'pisa/cronaca', 'prato/cronaca',
                     'versilia/cronaca'):
        urls.update(_find_tirreno_urls(crawler, category))
    for url in sorted(urls):
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        content = doc.content.decode('utf-8')
        header = extract('<h1 itemprop="headline name">',
                         '<span itemprop="author"', content) or ''
        body = extract('<span itemprop="articleBody" >', '©', content) or ''
        paras = clean_paragraphs('%s<p/>%s' % (header, body))
        text = '\n'.join(paras)
        for sep in ('Tags\n', 'Redazione | Scriveteci', 'TrovaRistorante',
                    '<a href="', 'I COMMENTI DEI LETTORI', '©RIPRODUZIONE'):
            text = text.split(sep)[0]
        paras = text.splitlines()
        pubdate = re.search(
            r'<time itemprop="datePublished" content="([^"]+)"', content)
        pubdate = pubdate.group(1) if pubdate else None
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')


def _find_tirreno_urls(crawler, category):
    site = 'http://iltirreno.gelocal.it/'
    urls = set()
    caturl = site + category
    catpage = crawler.fetch_content(caturl)
    num_pages = re.search(r'Pagina <span class="active">\d+</span> di (\d+)',
                          catpage)
    baseurl = re.search(r'<a title="Vai a pagina 1" href="([^"]+)"', catpage)
    if num_pages is None or baseurl is None:
        return urls
    num_pages = int(num_pages.group(1))
    baseurl = urljoin(site, baseurl.group(1))
    for p in range(1, num_pages + 1):
        url = '%s?page=%d' % (baseurl, p) if p > 1 else baseurl
        content = crawler.fetch_content(url)
        for u in re.findall(r'<h1><a href="([^"]+)">', content):
            u = urljoin(site, replace_html_entities(u.strip()))
            if not u.startswith('http://old.iltirreno.gelocal.it/'):
                urls.add(u)
    return urls
