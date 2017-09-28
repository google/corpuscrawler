# -*- coding: utf-8 -*-
#
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
import base64
import collections
import codecs
import hashlib
import mimetools
import os
import random
import re
import ssl
import time
import urllib
import urllib2
import zlib

try:
    import xml.etree.cElementTree as etree
except ImportError:
    import xml.etree.ElementTree as etree

try:
    import htmlentitydefs
except ImportError:
    import html.entitites as htmlentitydefs

try:
    # Python 3
    from io import StringIO
    import urllib.robotparser as robotparser
    from urllib.urlparse import urljoin, urlparse, urlunparse
except ImportError:
    # Python 2
    from cStringIO import StringIO
    import robotparser
    from urlparse import urljoin, urlparse, urlunparse


FetchResult = collections.namedtuple('FetchResult',
                                     ['headers', 'content', 'status'])

_TAG_REGEX = re.compile(r'\<.+?\>', flags=re.DOTALL)
def striptags(s):
    return _TAG_REGEX.sub('', s)


def urlpath(url):
    "'http://example.org/foo/bar.html?baz#qux' --> '/foo/bar.hml'"
    return urlparse(url)[2]


def urlencode(url):
    p = list(urlparse(url))
    p[1] = p[1].encode('idna')
    for i in range(2, len(p)):
        p[i] = urllib.quote(p[i].encode('utf-8'))
    return urlunparse(p).encode('ascii')


class Crawler(object):
    def __init__(self, language, output_dir, cache_dir):
        assert len(language) >= 2
        self.language = language
        self.cache_dir = cache_dir
        self.output_dir = output_dir
        self.outputs = {}  # bcp47 tag (eg. 'rm-puter') --> codecs.StreamWriter
        self.robotcheckers = {}
        self.useragent = 'LinguisticCorpusCrawler/1.0'
        self.useragent_for_robots_txt = self.useragent.split('/')[0]
        self.crawldelay = 15.0  # seconds between fetches
        for path in (output_dir, cache_dir):
            if not os.path.exists(path):
                os.makedirs(path)

    def get_output(self, language=None):
        if language is None:
            language = self.language
        out = self.outputs.get(language)
        if out is not None:
            return out
        outpath = os.path.join(self.output_dir, language + '.txt')
        out = self.outputs[language] = codecs.open(outpath, 'w', 'utf-8')
        return out

    def close(self):
        for writer in self.outputs.values():
            writer.close()

    def fetch(self, url, redirections=None):
        if not self.is_fetch_allowed_by_robots_txt(url):
            return FetchResult(headers='', content='', status=403)

        digest = hashlib.sha256(url).digest()
        filepath = os.path.join(self.cache_dir,
                                "f" + base64.urlsafe_b64encode(digest))
        try:
            with open(filepath, 'r') as f:
                headers, content = f.read().split(b'\r\n\r\n\r\n', 1)
                headers = mimetools.Message(StringIO(headers))
                status = int(headers.get('Status', '200'))
                return FetchResult(headers, content, status)
        except IOError:
            pass
        delay = random.uniform(self.crawldelay, self.crawldelay + 2)  # jitter
        time.sleep(delay)
        print(url)
        request = urllib2.Request(url, headers={'User-Agent': self.useragent})
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        try:
            response = urllib2.urlopen(request, context=context)
        except urllib2.HTTPError as err:
            response = err
        status = response.getcode()
        content = response.read()
        response.close()
        if status == 200 or status >= 400 and status <= 499:
            with open(filepath, 'w') as f:
                f.write(b'Status: %d\r\n' % response.getcode())
                f.write(str(response.headers).rstrip())
                f.write(b'\r\n\r\n\r\n')
                f.write(content)
        return FetchResult(headers=response.headers, content=content,
                           status=status)

    def fetch_sitemap(self, url, processed=set()):
        """'http://example.org/sitemap.xml' --> {url: lastmod}"""
        result = {}
        content = self.fetch(url).content
        if content.startswith(b'\x1F\x8B'):
            content = zlib.decompress(content, zlib.MAX_WBITS|32)
        sitemap = etree.fromstring(content)
        xmlns = 'http://www.sitemaps.org/schemas/sitemap/0.9'  # XML namespace
        for s in sitemap.findall('{%s}sitemap/{%s}loc' % (xmlns, xmlns)):
            subsitemap = s.text.strip()
            if subsitemap not in processed:  # prevent infinite recursion
                processed.add(subsitemap)
                result.update(self.fetch_sitemap(subsitemap, processed))
        locpath, lastmodpath = '{%s}loc' % xmlns, '{%s}lastmod' % xmlns
        for urlinfo in sitemap.findall('{%s}url' % xmlns):
            location = urlinfo.find(locpath)
            if location is None:
                continue
            location = location.text.strip()
            lastmod = urlinfo.find(lastmodpath)
            if lastmod is not None:
                lastmod = lastmod.text.strip()
                if len(lastmod) == 0:
                    lastmod = None
            result[location] = lastmod
        return result

    def is_fetch_allowed_by_robots_txt(self, url):
        scheme, netloc, path, _, _, _ = urlparse(url)
        if path == '/robots.txt':
            return True
        robots_txt_url = '%s://%s/robots.txt' % (scheme, netloc)
        checker = self.robotcheckers.get(robots_txt_url)
        if checker is None:
            doc = self.fetch(robots_txt_url)
            robots_txt = doc.content if doc.status == 200 else ''
            checker = robotparser.RobotFileParser()
            checker.set_url(robots_txt_url)
            checker.parse(robots_txt)
            self.robotcheckers[robots_txt_url] = checker

        # Work around a RobotFileParser bug which makes it crash when
        # an URL contains non-ASCII characters, even when they are perfectly
        # escaped. (The library seems to make a hard-coded assumption that
        # URLs are encoded in ISO 8859-1 instead of UTF-8 before being escaped;
        # this had been true in the very early days of the web, but not
        # anymore.) To work around this bug, we double-encode the URL
        # for the purpose of robots checking; this prevents the crash.
        return checker.can_fetch(useragent=self.useragent_for_robots_txt,
                                 url=urlencode(url))


# Normally we put site-specific logic into the language-specific scripts,
# but a couple sites have large amounts of text in many underserved languages,
# using the same site structure for all languages.
def crawl_bbc_news(crawler, out, urlprefix):
    # sitemap = {'http://www.bbc.com/burmese/world-41146701': None}
    sitemap = crawler.fetch_sitemap('http://www.bbc.com/sitemap.xml')
    pubdate_regex = re.compile(r'"dateModified":\s*"([0-9T:+\-]{25})"')
    for url in sorted(sitemap.keys()):
        if not urlpath(url).startswith(urlprefix):
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
        if title: title = striptags(title.group(1).split('- BBC')[0]).strip()
        if title: out.write(cleantext(title) + '\n')
        for paragraph in re.findall(r'<p>(.+?)</p>', html):
            out.write(cleantext(paragraph) + '\n')


def crawl_korero_html(crawler, out, project, genre, filepath):
    url = 'https://raw.githubusercontent.com/korero/%s/master/%s' % (
        project, filepath)
    fetchresult = crawler.fetch(url)
    if fetchresult.status != 200:
        return
    doc = etree.fromstring(fetchresult.content)
    license = doc.find('./head/link[@rel="license"]')
    if license is not None: license = license.get('href', '').strip()
    articles = doc.findall('./body/article')
    if len(articles) == 0:
        out.write('# Location: %s\n' % url)
        if genre:
            out.write('# Genre: %s\n' % genre)
        if license:
            out.write('# License: %s\n' % license)
        write_paragraphs(doc.find('body'), out)
        out.write('#\n')
    else:
        for i, article in enumerate(articles):
            out.write('# Location: %s#%d\n' % (url, i + 1))
            if license:
                out.write('# License: %s\n' % license)
            pubdate = article.find('./footer//time')
            if pubdate is not None:
                pubdate = pubdate.attrib.get('datetime')
                if pubdate is not None:
                    out.write('# Publication-Date: %s\n' % pubdate)
            write_paragraphs(article, out)


def write_paragraphs(et, out):
    # Recursively descend into the etree until we find a paragraph-ish tag;
    # once we have one, write its entire inner text into a single line.
    if et.tag.lower() in {'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'div'}:
        text = ' '.join(' '.join(et.itertext()).split())
        if text: out.write(text + '\n')
    else:
        for e in et:
            write_paragraphs(e, out)


def crawl_deutsche_welle(crawler, out, prefix):
    urls = set()
    for url in crawler.fetch_sitemap('http://www.dw.com/sitemap.xml'):
        path = urlpath(url)
        if path.startswith(prefix) and \
                (re.match(r'/[^/]+/\d{2}-.*', path) is None):  # German lessons
            urls.add(url)
    for url in sorted(urls):
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        html = doc.content.decode('utf-8')
        pubdate = re.search(r'articleChangeDateShort: "(\d{8})"', html)
        if pubdate is not None:
            pubdate = pubdate.group(1)
            pubdate = '%s-%s-%s' % (pubdate[0:4], pubdate[4:6], pubdate[6:8])
        title = re.search(r'<h1>(.+?)</h1>', html)
        title = cleantext(title.group(1)) if title is not None else ''
        intro = re.search(r'<p class="intro">(.+?)</p>', html)
        intro = cleantext(intro.group(1)) if intro is not None else ''
        text = html.split('<div class="longText">', 1)
        text = text[1].split('</div>')[0] if len(text) == 2 else ''
        text = text.split('<div')[0]
        paras = [title, intro] + text.replace('</p>', '\n').splitlines()
        paras = filter(None, [cleantext(p) for p in paras if p])
        if not paras:
            continue
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        for p in paras:
            out.write(p + '\n')


def crawl_udhr(crawler, out, filename):
    url = 'http://www.unicode.org/udhr/d/' + filename
    response = crawler.fetch(url)
    assert response.status == 200, (response.status, url)
    text = response.content.decode('utf-8').split('---', 1)[1]
    out.write('# Location: %s\n' % url)
    out.write('# Genre: Legal\n')
    for paragraph in text.splitlines():
        paragraph = paragraph.strip()
        if len(paragraph) > 0:
            out.write(paragraph.strip() + '\n')


def replace_html_entities(html):
    entities = htmlentitydefs.name2codepoint
    html = re.sub(r'&#([0-9]+);', lambda z:unichr(int(z.group(1))), html)
    html = re.sub(
        r'&#[xX]([0-9a-fA-F]+);', lambda z:unichr(int(z.group(1), 16)), html)
    html = re.sub(r'&([a-zA-Z]+);',
                  lambda z:unichr(entities[z.group(1).lower()]), html)
    return html


def cleantext(html):
    html = replace_html_entities(striptags(html))
    # Some web sites insert zero-width spaces, possibly as byte order marks
    # (from Microsoft Notepad) which their scripts failed to recognize as such.
    html = html.replace('\u200B', '')
    return ' '.join(html.split())


def fixquotes(s):
    s = (' ' + s).replace(" '", " ‘").replace("'", "’")
    s = s.replace(' "', ' “').replace('"', '”')
    return s.strip()
