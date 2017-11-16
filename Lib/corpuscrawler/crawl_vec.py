# coding: utf-8
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
from corpuscrawler.util import cleantext, crawl_udhr, extract


# URLs we exclude from the crawl because they contain non-Venetian content.
BLACKLISTED_URLS = {
    'http://www.quatrociacoe.it/200111/vocabolarieto.php',
}


def crawl(crawler):
    out = crawler.get_output(language='vec')
    crawl_udhr(crawler, out, filename='udhr_vec.txt')
    crawl_larenadomila_it(crawler)
    crawl_quatrociacoe_it(crawler)
    crawl_wikisource_trieste_vernacola(crawler)


def crawl_larenadomila_it(crawler):
    out = crawler.get_output(language='vec-u-sd-itvr')
    urls = find_urls_in_larenadomila_it(
        crawler, 'https://www.larenadomila.it/sito/index.php')
    for url in sorted(urls.difference(BLACKLISTED_URLS)):
        if url.find('&view=article&') < 0:
            continue
        doc = crawler.fetch(url)
        assert doc.status == 200, (doc.status, start_url)
        content = doc.content.decode('utf-8')
        title = cleantext(extract('<title>', '</title>', content))
        sections = [title] + [c.strip() for c in content.splitlines()]
        sections = [c for c in sections
                    if c.startswith('<div class="item_fulltext">')
                    or c.startswith('<p><span class="grassetto">')]
        sections = [c.replace(' <br />- ', ' ') for c in sections]
        text = '<br/>'.join(sections)
        text = text.replace('&nbsp;', ' ')  # used for spacing/formatting
        text = re.sub(r'</(?:div|DIV|p|P|[hH][1-6]|table)>', '\n', text)
        text = re.sub(r'<br\s*/?>', '\n', text)
        text = re.sub(r'\.{3,}', '… ', text)
        text = re.sub(r'\n(-)[^\s]', '- ', text)
        paras = filter(None, [cleantext(p) for p in text.split('\n')])
        if not paras:
            continue
        out.write('# Location: %s\n' % url)
        out.write('\n'.join(paras) + '\n')


def find_urls_in_larenadomila_it(crawler, start_url, urls=set()):
    if start_url in urls:
        return
    doc = crawler.fetch(start_url)
    if doc.status != 200:
        return
    content = doc.content.decode('utf-8')
    urls.add(start_url)
    for path in re.findall(r'href="(/sito/index.php?[^"]+)"', content):
        url = 'https://www.larenadomila.it' + path.replace('&amp;', '&')
        url = re.sub(r'\d(:[^&$]+)', '', url)
        def escape_char(c):
            return '%%%02X' % ord(c) if ord(c) > 0x80 else c
        url = ''.join([escape_char(c) for c in url])
        find_urls_in_larenadomila_it(crawler, url, urls)
    return urls


def crawl_quatrociacoe_it(crawler):
    out = crawler.get_output(language='vec-u-sd-itpd')
    urls = set()
    main = crawler.fetch('http://www.quatrociacoe.it/')
    assert main.status == 200, main.status
    for e in re.findall(r'href="/(\d{6})/\d{6}\.php"', main.content):
        ed = crawler.fetch('http://www.quatrociacoe.it/%s/%s.php' % (e, e))
        assert ed.status == 200, ed.status
        for path in re.findall(r'href="(/%s/.+?\.php)"' % e, ed.content):
            if path != '/%s/%s.php' % (e, e):
                urls.add('http://www.quatrociacoe.it' + path)
    for url in sorted(urls):
        if url in BLACKLISTED_URLS:
            continue
        doc = crawler.fetch(url)
        assert doc.status == 200, doc.status
        encoding = re.search(r'html;\s*charset=([\-a-zA-Z0-9]+)"', doc.content)
        encoding = encoding.group(1).lower() if encoding else 'utf-8'
        assert encoding in ('iso-8859-1', 'utf-8'), (encoding, url)
        content = doc.content.decode(encoding)
        text = extract('<!-- *** INIZIO ARTICOLO ***-->',
                       '<!-- *** FINE ARTICOLO ***-->', content)
        if not text:
            continue
        year, month = re.search(r'/(20\d{2})(\d{2})/', url).groups()
        text = text.replace('\n', ' ').replace('\r', ' ')
        text = re.sub('Torna\s+alla pagina principale', ' ', text)
        text = text.replace('[torna sopra]', ' ')
        text = re.sub(r'<!--.+?-->', '', text, flags=re.DOTALL)
        text = re.sub(r' alt="[^"]+"', ' ', text, flags=re.DOTALL)
        text = text.replace('\u0091', '’')  # misuse of U+0091 PRIVATE USE ONE
        text = text.replace('\u0092', '’')  # misuse of U+0092 PRIVATE USE TWO
        text = text.replace('<<', '«').replace('>>', '»')  # invalid HTML
        text = text.replace('&lt;&lt;', '«').replace('&gt;&gt;', '»')
        text = re.sub('\.{3,}', '…', text)
        text = re.sub(r'</(?:div|DIV|p|P|[hH][1-6]|table|TABLE)>', '\n', text)
        text = re.sub(r'<(?:br|BR)\s*/?>', '\n', text)
        paras = filter(None, [cleantext(p) for p in text.splitlines()])
        text = re.sub(r'<img.+?\n">', ' ', '\n'.join(paras))
        paras = filter(None, [cleantext(p) for p in text.splitlines()])
        out.write('# Location: %s\n' % url)
        out.write('# Publication-Date: %s-%s-01\n' % (year, month))
        out.write('# Genre: Fiction\n')
        out.write('\n'.join(paras) + '\n')


def crawl_wikisource_trieste_vernacola(crawler):
    out = crawler.get_output(language='vec-u-sd-itts')
    urls = set()
    index = crawler.fetch(
        'https://vec.wikisource.org/wiki/Indice:Trieste_vernacola.djvu')
    assert index.status == 200, index.status
    remarks = extract('<div id="remarks">', 'Colombe</a>',
                      index.content.decode('utf-8'))
    for urlpath in sorted(set(re.findall(r'href="(/wiki/[^"]+)"', remarks))):
        if not urlpath.startswith('/wiki/Trieste_vernacola/'):
            urls.add('https://vec.wikisource.org' + urlpath)
    for url in sorted(urls.difference(BLACKLISTED_URLS)):
        doc = crawler.fetch(url)
        assert doc.status == 200, (doc.status, url)
        content = doc.content.decode('utf-8')
        text = extract('<div id="scatola" class="testo">', '<noscript>',
                       content)
        text = text.split('<dt>Note</dt>')[0].split('<dl>')[0]
        text = text.replace('\n', ' ')
        text = re.sub(r'<sup.+?</sup>', '', text)
        text = text.replace('&#160;', ' ')  # NBSP used for spacing
        text = text.replace("'", "’")
        text = re.sub(r'<!--.+?-->', '', text, flags=re.DOTALL)
        text = re.sub(r' alt="[^"]+"', ' ', text, flags=re.DOTALL)
        text = re.sub(r'<span class="numeroriga".+?</span>', '', text)
        text = re.sub(r'</(?:div|DIV|p|P|[hH][1-6]|table|TABLE)>', '\n', text)
        text = re.sub(r'<(?:br|BR)\s*/?>', '\n', text)
        lines = [l for l in text.splitlines()
                 if l.find('noprint') < 0 and l.find('font-size:smaller') < 0]
        text = '\n'.join([cleantext(l) for l in lines])
        text = re.sub('\n{2,}', '<p>', text).replace('\n', ' | ')
        text = text.replace('<p>', '\n')
        paras = filter(None, [' '.join(p.split()) for p in text.splitlines()])
        if not paras:
            continue
        # The book, published in 1920, is a collection of earlier lyrics.
        pubyear = re.search(r'<span id="ws-year">(\d{4})</span>', content)
        pubyear = int(pubyear.group(1)) if pubyear else 1920
        out.write('# Location: %s\n' % url)
        out.write('# Genre: Lyrics\n')
        out.write('# Publication-Date: %d\n' % pubyear)
        out.write('\n'.join(paras) + '\n')
