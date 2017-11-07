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

from __future__ import absolute_import, print_function, unicode_literals
import re

from corpuscrawler.util import crawl_udhr, cleantext, striptags


def crawl(crawler):
    out = crawler.get_output(language='mi')
    crawl_udhr(crawler, out, filename='udhr_mri.txt')
    _scrape_maoritelevision(crawler, out)
    _scrape_paiperatapu(crawler, out)

def _scrape_maoritelevision(crawler, out):
    articlelist = set()
    articlelist.add('http://www.maoritelevision.com/mi/purongo/purongo-hou')
    articlelist.add('http://www.maoritelevision.com/mi/purongo/hakinakina')
    for i in range(1, 101):
        articlelist.add('http://www.maoritelevision.com/mi/purongo/purongo-hou?page=%d' % i)
        articlelist.add('http://www.maoritelevision.com/mi/purongo/hakinakina?page=%d' % i)
    links = set()
    pubdate_regex = re.compile(r'<time datetime="([0-9T:+\-]{25})"')
    for url in articlelist:
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        content = doc.content.decode('utf-8')
        for articlepiece in content.split('<article')[1:]:
            for artlink in re.findall('<a href="(/mi/purongo/[^"]*)"', articlepiece):
                if not artlink.startswith('/mi/purongo/purongo-hou'):
                    links.add('http://www.maoritelevision.com%s' % artlink)
    for url in links:
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        if 'a-motu/rereatea-midday-news' in url:
            continue
        html = doc.content.decode('utf-8')
        if 'lang="mi"' not in html:
            continue
        if 'itemprop="articleBody"' not in html:
            continue
        genre = 'Sport' if '/hakinakina/' in url else 'News'
        pubdate_match = pubdate_regex.search(html)
        pubdate = pubdate_match.group(1) if pubdate_match else None
        if pubdate is None: pubdate = doc.headers.get('Last-Modified')
        if pubdate is None: pubdate = sitemap[url]
        # These news stories are a parallel (or at least comparable) corpus, so keeping
        # the link to the English article
        english = re.search(r'<a href="(/news/[^"]*)" class="language-link" lang="en">', html)
        if english: english = 'http://www.maoritelevision.com%s' % english.group(1)
        tags = set()
        if '<ul class="tags">' in html:
            tagshtml = html.split('<ul class="tags">')[1].split('</ul>')[0]
            for tag in re.findall(r'<a href="(?:[^"]*)">([^<]*)</a>', tagshtml):
                tags.add(cleantext(tag))
        paras = []
        title = re.search(r'<title>(.+?)</title>', html)
        if title:
            paras.append(cleantext(striptags(title.group(1).split('| Māori')[0])))
        articlehtml = html.split('class="field-body"')[1].split('</div>')[0]
        paras.extend([cleantext(p) for p in re.findall(r'<p>(.+?)</p>', articlehtml)])
        paras = [p for p in paras if p and p.find(' the ') < 0]  # filter out English
        if not paras:
            continue
        out.write('# Location: %s\n' % url)
        out.write('# Genre: %s\n' % genre)
        if pubdate: out.write('# Publication-Date: %s\n' % pubdate)
        if english: out.write('# Translation.en: %s\n' % english)
        if tags: out.write('# Tags: %s\n' % ', '.join(tags))
        out.write('\n'.join(paras) + '\n')


def _scrape_paiperatapu(crawler, out):
    booklist = list()
    books = crawler.fetch('http://www.paiperatapu.maori.nz/paipera-tapu-online')
    assert books.status == 200, books.status
    bookshtml = books.content.decode('utf-8')
    bookshtmlinner = bookshtml.split('<div class="bible-book-list">')[1].split('<li class="first bible-search">')[0]
    for bookslink in re.findall(r'<a href="(/bible/[0-9]*/[^"]*)">', bookshtmlinner):
        bookurl = 'http://www.paiperatapu.maori.nz' + bookslink
        book = crawler.fetch(bookurl)
        assert book.status == 200, book.status
        bookhtml = book.content.decode('utf-8')
        bookhtmlinner = bookhtml.split('<ul class="bible-chapter-list">')[1].split('<div class="bible-links">')[0]
        for chapterlink in re.findall(r'<a href="(/bible/[0-9]*/[^/]*/[^"]*)">', bookhtmlinner):
            url = 'http://www.paiperatapu.maori.nz' + chapterlink
            chapter = crawler.fetch(url)
            assert chapter.status == 200, chapter.status
            chapterhtml = chapter.content.decode('utf-8')
            if '<dl class="bible-chapter-content">' not in chapterhtml:
                continue
            out.write('# Location: %s\n' % url)
            title = re.search(r'<title>(.+?)</title>', chapterhtml)
            if title: title = striptags(title.group(1).split('| Te')[0]).strip()
            # Title is in English
            if title: out.write('# Title: %s\n' % cleantext(title))
            out.write('# Genre: Religion\n')
            chapterhtmlinner = chapterhtml.split('<dl class="bible-chapter-content">')[1].split('<div class="bible-chapter-seek">')[0]
            for verse in re.finditer(r'<dt><a name="[^"]*"></a>([^<]*)</dt><dd class="[^"]*">([^<]*)</dd>', chapterhtmlinner):
                out.write('%s %s\n' % (verse.group(1), cleantext(verse.group(2))))
