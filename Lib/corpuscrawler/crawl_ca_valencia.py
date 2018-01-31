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
from corpuscrawler.util import clean_paragraphs, extract


def crawl(crawler):
    out = crawler.get_output(language='ca-valencia')
    _crawl_val_levante_emv_com(crawler, out)


def _crawl_val_levante_emv_com (crawler, out):
    urls = set()
    for url in crawler.fetch_sitemap('http://val.levante-emv.com/sitemap.xml'):
        url = url.replace('//www.levante-emv.com', '//val.levante-emv.com')
        if re.search(r'/\d{4}/\d{2}/\d{2}/', url) is not None:
            urls.add(url)
    for url in sorted(urls):
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        es_url = url.replace('//val.levante-emv.com', '//www.levante-emv.com')
        html = doc.content.decode('utf-8')
        pubdate = re.search(
            r'<meta name="cXenseParse:recs:publishtime" content="([^"]+)"',
            html)
        pubdate = pubdate.group(1) if pubdate else None
        title = extract('<span itemprop="articleBody">', '</h1>', html)
        subtitle = extract('<h2 itemprop="description">', '</h2>', html)
        content = extract('<span itemprop="articleBody">',
                          '</apertium-notrans>', html)
        paras = clean_paragraphs(
            ''.join(['<p>%s</p>' % p for p in (title, subtitle, content) if p]))
        text = '\n'.join(paras)
        for sep in ['Compartir en Twitter', 'HEMEROTECA\n', '\nPublicitat\n']:
            text = text.split(sep)[0].strip()
        if not text:
            continue
        if any(b in text for b in ['inicia sessió si eres subscriptor',
                                   'Si eres subscriptor inicia sessió',
                                   'Para continuar leyendo... suscríbete']):
            continue
        out.write('# Location: %s\n' % url)
        out.write('# Translation.es: %s\n' % es_url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        out.write(text + '\n')
