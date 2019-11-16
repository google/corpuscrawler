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
import sys
import ssl
from corpuscrawler.util import (
    crawl_udhr, clean_paragraphs, cleantext, extract, striptags, urlpath
)

try:
    import xml.etree.cElementTree as etree
except ImportError:
    import xml.etree.ElementTree as etree


def crawl(crawler):
    out = crawler.get_output(language='ga')
    crawl_udhr(crawler, out, filename='udhr_gle.txt')
    crawl_tuairisc_ie(crawler, out)
    crawl_nuachtrte(crawler, out)
    crawl_irishtimes(crawler, out)
    crawl_chg(crawler, out)
    crawl_ainm_ie(crawler, out)
    crawl_blogspot(crawler, out, host='gaeltacht21.blogspot.com')
    crawl_blogspot(crawler, out, host='aonghus.blogspot.com')


# RTE has news sites both for its own Irish language news programme
# and for Raidió na Gaeltachta
def _rtenuacht_path(url):
    rtenuacht = urlpath(url).startswith('/news/nuacht/')
    rnagnuacht = urlpath(url).startswith('/rnag/nuacht-gaeltachta')
    return rtenuacht or rnagnuacht


def _rte_writable_paragraph(text):
    if text == '':
        return False
    if text.startswith('© RTÉ '):
        return False
    if text.startswith('By using this website, you consent'):
        return False
    if text.startswith('RTÉ.ie is the website of Raidió Teilifís Éireann'):
        return False
    if text.find('is not responsible for the content') >= 0:
        return False
    if text.find('RTÉ uses cookies in accordance with our Cookie Policy') >= 0:
        return False
    return True

def _check_rte_sitemap(url):
    urlmatch = re.search(r'https?://www.rte.ie/sitemap-([0-9]+)0000.xml', url)
    try:
        if int(urlmatch.group(1)) < 40:
            return True
        else:
            return False
    except AttributeError:
        return True

def crawl_nuachtrte(crawler, out):
    sitemap = crawler.fetch_sitemap(
        'http://www.rte.ie/sitemap.xml',
        subsitemap_filter=lambda x: _check_rte_sitemap(x)
        )
    pubdate_regex = re.compile(r'name="DC.date" (?:scheme="DCTERMS.URI" )?content="([0-9T:+\-]{19,25})"')
    for url in sorted(sitemap.keys()):
        if not _rtenuacht_path(url):
            continue
        fetchresult = crawler.fetch(url)
        if fetchresult.status != 200:
            continue
        html = fetchresult.content.decode('utf-8')
        pubdate_match = pubdate_regex.search(html)
        pubdate = pubdate_match.group(1) if pubdate_match else None
        if pubdate is None: pubdate = fetchresult.headers.get('Last-Modified')
        if pubdate is None: pubdate = sitemap[url]
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate: out.write('# Publication-Date: %s\n' % pubdate)
        title = re.search(r'<title>(.+?)</title>', html)
        if title: title = striptags(title.group(1).split('- RTÉ')[0]).strip()
        if title: out.write(cleantext(title) + '\n')
        for paragraph in re.findall(r'<p>(.+?)</p>', html):
            cleaned = cleantext(paragraph)
            if _rte_writable_paragraph(cleaned):
                out.write(cleaned + '\n')
            else:
                continue


def _irishtimes_section_list(crawler, out, url):
    page = crawler.fetch(url)
    if page.status != 200:
        return
    html = page.content.decode('utf-8')
    links = set()
    links.add(url)
    list = html.split('<ul class="page_numbers">')[1].split('</ul>')[0]
    for cnt in re.findall(r'(\?sectionTeaserPage[^"]+?)"', list):
        links.add('%s%s' % (url, cnt))
    return links


def crawl_irishtimes(crawler, out):
    crawler.set_context(ssl.SSLContext(ssl.PROTOCOL_TLSv1_2))
    start = 'https://www.irishtimes.com/culture/treibh'
    pubdatere1 = re.compile(
        r'<meta itemprop="datePublished" content="([^"]*)"/>')
    pubdatere2 = re.compile(r'"datePublished": "([^"])"')
    links = set()
    for contents in _irishtimes_section_list(crawler, out, start):
        init = crawler.fetch(contents)
        if init.status != 200:
            continue
        shtml = init.content.decode('utf-8')
        for doclink in re.findall('<p><a href="/culture/treibh/([^"]*)"', shtml):
            links.add('%s/%s' % (start, doclink))
    for url in links:
        res = crawler.fetch(url)
        if res.status != 200:
            continue
        html = res.content.decode('utf-8')
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        title = re.search(r'<title>(.+?)</title>', html)
        pubdate_match = pubdatere1.search(html)
        pubdate_match = pubdate_match if pubdate_match else pubdatere2.search(html)
        pubdate = pubdate_match.group(1) if pubdate_match else None
        if pubdate is None: pubdate = fetchresult.headers.get('Last-Modified')
        if pubdate: out.write('# Publication-Date: %s\n' % pubdate)
        if title: out.write(cleantext(title.group(1)) + '\n')
        for paragraph in re.findall(
                r'<p class="no_name">(.+?)</p>',
                html.split('<div class="article_bodycopy">')[1]):
            cleaned = cleantext(paragraph)
            out.write(cleaned + '\n')
    crawler.set_context(ssl.SSLContext(ssl.PROTOCOL_TLSv1))


def crawl_chg(crawler, out):
    def _chg_content(page):
        return page.split('<div class="container" id="article">')[1].split('<!-- /.right columns -->')[0]
    sitemap = 'https://www.chg.gov.ie/ga/help/sitemap/'
    res = crawler.fetch(sitemap)
    if res.status != 200:
        return
    links = set()
    html = res.content.decode('utf-8')
    body = _chg_content(html)
    for pagelink in re.findall('<a href="([^"]*)">', body):
        if pagelink.startswith('https://www.chg.gov.ie/ga/'):
            links.add(pagelink)
    for link in links:
        pres = crawler.fetch(link)
        if pres.status != 200:
            continue
        phtml = pres.content.decode('utf-8')
        ptext = _chg_content(phtml)
        title = re.search(r'<title>(.+?)</title>', phtml)
        if title: title = striptags(title.group(1).split('|')[0]).strip()
        pubdate = pres.headers.get('Last-Modified')
        out.write('# Location: %s\n' % link)
        out.write('# Genre: Government\n')
        if pubdate: out.write('# Publication-Date: %s\n' % pubdate)
        for paragraph in re.findall(r'<p>(.+?)</p>', ptext):
            cleaned = cleantext(paragraph)
            out.write(cleaned + '\n')


def crawl_blogspot(crawler, out, host):
    sitemap = crawler.fetch_sitemap('https://%s/sitemap.xml' % host)
    pubdate_regex = re.compile(
        r"<abbr class='published' title='([^']*)'>[^<]*</abbr>")
    for url in sorted(sitemap.keys()):
        fetchresult = crawler.fetch(url)
        if fetchresult.status != 200:
            continue
        html = fetchresult.content.decode('utf-8')
        pubdate_match = pubdate_regex.search(html)
        pubdate = pubdate_match.group(1) if pubdate_match else None
        if pubdate is None: pubdate = fetchresult.headers.get('Last-Modified')
        if pubdate is None: pubdate = sitemap[url]
        title = re.search(r"<meta content='([^']+)' property='og:title'/>",
                          html)
        title = title.group(1) if title else ''
        post = extract("<div class='post-body entry-content'>",
                       "<div class='post-footer'>", html)
        paras = clean_paragraphs(title + '<br/>' + post)
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: Blog\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')
        #post = html.split("<div class='post-body entry-content'>")[1].split("<div class='post-footer'>")[0]


def crawl_ainm_ie(crawler, out):
    links = set()
    for let in map(chr, range(65, 91)):
        idxres = crawler.fetch('https://www.ainm.ie/Abc.aspx?Letter=%s' % let)
        if idxres.status != 200:
            continue
        idxhtml = idxres.content.decode('utf-8')
        index = extract('<div id="pageContent" role="main">',
                        '<!-- .contentWrapper-->', idxhtml)
        for link in re.findall(r'<a href="(Bio.aspx\?ID=[^"]+?)">', index):
            links.add('https://www.ainm.ie/%s' % link)
    for url in sorted(links):
        fetchresult = crawler.fetch(url)
        if fetchresult.status != 200:
            continue
        html = fetchresult.content.decode('utf-8')
        title = re.search(r'<title>(.+?)</title>', html)
        title = title.group(1).split('|')[0] if title else ''
        body = extract('<div class="article">',
                       '<!-- .contentWrapper-->', html) or ''
        body = body.split('<div id="machines"')[0]
        paras = clean_paragraphs(title + '<br/>' + body)
        pubdate = fetchresult.headers.get('Last-Modified')
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: Biography\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')


# Tuairisc is wordpress based, but seems to have a different layout than
# the method in util.py caters to.
def crawl_tuairisc_ie(crawler, out):
    sitemap = crawler.fetch_sitemap('https://tuairisc.ie/sitemap.xml')
    pubdate_regex = re.compile(
        r'<time datetime="(20\d\d-\d\d-\d\d)\s+(\d\d:\d\d)" '
        r'itemprop="datePublished">')
    for url in sorted(sitemap.keys()):
        fetchresult = crawler.fetch(url)
        if fetchresult.status != 200:
            continue
        html = fetchresult.content.decode('utf-8')
        title = extract('<h1 class="title article--full__title">', '</h1>',
                        html) or ''
        pubdate_match = pubdate_regex.search(html)
        if pubdate_match:
            pubdate = '%sT%s:00Z' % (
                pubdate_match.group(1), pubdate_match.group(2))
        else:
            pubdate = sitemap[url]
        body = extract(
            '<div class="article--full__content" itemprop="articleBody">',
            '</article>', html)
        if not body:
            continue
        paras = clean_paragraphs(title + '<p/>' + body)
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')
