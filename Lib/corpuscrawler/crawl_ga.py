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

from corpuscrawler.util import crawl_udhr, urlpath, striptags, cleantext

try:
    import xml.etree.cElementTree as etree
except ImportError:
    import xml.etree.ElementTree as etree

def crawl(crawler):
    out = crawler.get_output(language='ga')
    crawl_udhr(crawler, out, filename='udhr_gle.txt')
    crawl_nuachtrte(crawler, out)
    crawl_irishtimes(crawler, out)
    crawl_blogspot(crawler, out, 'http://gaeltacht21.blogspot.com/sitemap.xml', 'gaeltacht21')
    crawl_blogspot(crawler, out, 'http://aonghus.blogspot.com/sitemap.xml', 'Smaointe Fánacha Aonghusa')


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
    return True

def _check_rte_sitemap(url):
    urlmatch = re.search(r'http://www.rte.ie/sitemap-([0-9]+)0000.xml', url)
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
    start = 'https://www.irishtimes.com/culture/treibh'
    pubdatere1 = re.compile(r'<meta itemprop="datePublished" content="([^"]*)"/>')
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
        for paragraph in re.findall(r'<p class="no_name">(.+?)</p>', html.split('<div class="article_bodycopy">')[1]):
            cleaned = cleantext(paragraph)
            out.write(cleaned + '\n')


def crawl_blogspot(crawler, out, sitemap, default_title):
    sitemap = crawler.fetch_sitemap(sitemap)
    pubdate_regex = re.compile(r"<abbr class='published' title='([^']*)'>[^<]*</abbr>")
    for url in sorted(sitemap.keys()):
        fetchresult = crawler.fetch(url)
        if fetchresult.status != 200:
            continue
        html = fetchresult.content.decode('utf-8')
        pubdate_match = pubdate_regex.search(html)
        pubdate = pubdate_match.group(1) if pubdate_match else None
        if pubdate is None: pubdate = fetchresult.headers.get('Last-Modified')
        if pubdate is None: pubdate = sitemap[url]
        out.write('# Location: %s\n' % url)
        out.write('# Genre: Blog\n')
        if pubdate: out.write('# Publication-Date: %s\n' % pubdate)
        title = re.search(r'<title>(.+?)</title>', html)
        if title: title = striptags(title.group(1)).strip()
        if title and title == 'gaeltacht21': title = None
        start_title = '%s: ' % default_title
        if title and title.startswith(start_title): title = title[len(start_title):]
        if title: out.write(cleantext(title) + '\n')
        post = html.split("<div class='post-body entry-content'>")[1].split("<div class='post-footer'>")[0]
        for para in re.compile('<br ?/>').split(post):
            out.write(cleantext(para) + '\n')

