# coding: utf-8
# Copyright 2017 Google Inc. All rights reserved.
# Copyright 2017 Jim O'Regan
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

import json
import re
from corpuscrawler.util import crawl_udhr, cleantext, striptags

def crawl(crawler):
    out = crawler.get_output(language='ace')
    crawl_udhr(crawler, out, filename='udhr_ace.txt')
    crawl_bibleis(crawler, out, 'AC1IBS')

def crawl_bibleis(crawler, out, bible):
    firsturl = 'http://listen.bible.is/%s/Matt/1' % bible
    booklist = set()
    init = crawler.fetch(firsturl)
    if init.status != 200:
        return
    content = init.content.decode('utf-8')
    jsonraw = json.loads(content.split('var chaptersByBook = ')[1].split(';\n')[0])
    for book in jsonraw:
        for chapter in jsonraw.get(book):
            booklist.add('http://listen.bible.is/%s/%s/%s' % (bible, book, chapter))
    for url in booklist:
        doc = crawler.fetch(url)
        pubdate = doc.headers.get('Last-Modified')
        if doc.status != 200:
            continue
        html = doc.content.decode('utf-8')
        if 'var audioUrl = ' in html:
            audio = html.split('var audioUrl = "')[1].split('"')[0]
        inner = html.split('<div id="chapter-content"')[1].split('<div class="content-text">')[1].split('<hr>')[0]
        title = cleantext(striptags(inner.split('<span class="chapter-title">')[1].split('</span>')[0]))
        paras = []
        for verse in inner.split('<span class="verse-container"')[1:]:
            paras.append(cleantext(' '.join(re.findall(r'<span class="verse-(?:marker|text)">([^<]*)</span>', verse))))
        out.write('# Location: %s\n' % url)
        out.write('# Genre: Religion\n')
        if pubdate: out.write('# Publication-Date: %s\n' % pubdate)
        if audio: out.write('# Audio: %s\n' % audio)
        out.write('\n'.join(paras) + '\n')

