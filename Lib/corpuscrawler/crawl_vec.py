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
    crawl_quatrociacoe_it(crawler, out)


def crawl_quatrociacoe_it(crawler, out):
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
