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
from corpuscrawler.util import crawl_udhr, clean_paragraphs, extract


def crawl(crawler):
    out = crawler.get_output(language='pt-PT')
    crawl_udhr(crawler, out, filename='udhr_por_PT.txt')
    _crawl_observador_pt(crawler, out)
    _crawl_visao_sapo_pt(crawler, out)


def _crawl_observador_pt(crawler, out):
    urls = set()
    for author_page in sorted(re.findall(
            r'href="(https?://observador.pt/perfil/[a-zA-Z_\-0-9]+/)"',
            crawler.fetch_content('http://observador.pt/autores/'))):
        html = crawler.fetch_content(author_page)
        urls.update(re.findall(
            r'href="(https?://observador.pt/20\d{2}/\d{2}/\d{2}/[^"]+)"',
            html))
    for url in sorted(urls):
        try:
            html = crawler.fetch_content(url)
        except UnicodeDecodeError:
            continue
        title = re.search(r'<meta property="og:title" content="([^"]+)"', html)
        title = title.group(1) or ''
        pubdate = re.search(r'"dateModified":"([^"]+)"', html)
        pubdate = pubdate.group(1) or None
        lead = extract('<div class="lead">', '</div>', html) or ''
        content = extract('<div class="content">', '<h1>', html) or ''
        text = '\n'.join(clean_paragraphs('<p>'.join([title, lead, content])))
        text = text.split('\nContinuar a ler')[0]
        text = text.split('\nLer mais')[0]
        text = text.split('\nPartilhe')[0]
        text = text.split('\nComente')[0]
        if text:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write(text)
            out.write('\n')


def _crawl_visao_sapo_pt(crawler, out):
    sitemap = crawler.fetch_sitemap(
        'http://visao.sapo.pt/sitemap/visao_index.xml')
    sitemap.update(crawler.fetch_sitemap(
        'http://visao.sapo.pt/sitemap/visao_news.xml'))
    for url in sorted(sitemap):
        html = crawler.fetch_content(url)
        title = re.search(r'<meta name="twitter:title" property="og:title" '
                          r'content="([^"]+)"', html)
        title = title.group(1) if title else ''
        pubdate = re.search(r'<p class="timeStamp publishedDate" datetime="'
                            r'([^"]+)"', html)
        pubdate = pubdate.group(1) if pubdate else None
        body = extract('<div class="afterHeader">', '<footer', html) or ''
        paras = clean_paragraphs('%s<p>%s' % (title, body))
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')
