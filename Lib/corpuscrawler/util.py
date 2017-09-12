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
import time
import urllib

try:
    import xml.etree.cElementTree as etree
except ImportError:
    import xml.etree.ElementTree as etree

try:
    # Python 3
    from io import StringIO
    import urllib.robotparser as robotparser
    from urllib.urlparse import urlparse, urljoin
except ImportError:
    # Python 2
    from cStringIO import StringIO
    import robotparser
    from urlparse import urlparse, urljoin


FetchResult = collections.namedtuple('FetchResult',
                                     ['headers', 'content', 'status'])

_TAG_REGEX = re.compile(r'<.+?>')
def striptags(s):
    return _TAG_REGEX.sub('', s)


def urlpath(url):
    "'http://example.org/foo/bar.html?baz#qux' --> '/foo/bar.hml'"
    return urlparse(url)[2]


class URLOpener(urllib.FancyURLopener):
    # used as our User-Agent header, and for checking robots.txt
    version = 'LinguisticCorpusCrawler/1.0'


class Crawler(object):
    def __init__(self, language, output_dir, cache_dir):
        assert len(language) >= 2
        self.language = language
        self.cache_dir = cache_dir
        self.output_dir = output_dir
        self.outputs = {}  # bcp47 tag (eg. 'rm-puter') --> codecs.StreamWriter
        self.robotcheckers = {}
        self.urlopener = URLOpener()
        self.useragent_for_robots_txt = self.urlopener.version.split('/')[0]
        self.crawldelay = 2.0  # seconds between fetches
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
        response = self.urlopener.open(url)
        content = response.read()
        response.close()
        with open(filepath, 'w') as f:
            f.write(b'Status: %d\r\n' % response.getcode())
            f.write(str(response.headers).rstrip())
            f.write(b'\r\n\r\n\r\n')
            f.write(content)
        return FetchResult(headers=response.headers, content=content,
                           status=response.getcode())

    def fetch_sitemap(self, url, processed=set()):
        """'http://example.org/sitemap.xml' --> {url: lastmod}"""
        result = {}
        sitemap = etree.fromstring(self.fetch(url).content)
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
            robots_txt = self.fetch(robots_txt_url)[0] or ''
            checker = robotparser.RobotFileParser()
            checker.set_url(robots_txt_url)
            checker.parse(robots_txt)
            self.robotcheckers[robots_txt_url] = checker
        return checker.can_fetch(useragent=self.useragent_for_robots_txt,
                                 url=url)


# Normally we put site-specific logic into the language-specific scripts,
# but a couple sites have large amounts of text in many underserved languages,
# using the same site structure for all languages.
def crawl_bbc_news(crawler, out, urlprefix):
    # sitemap = {'http://www.bbc.com/burmese/world-41146701': None}
    sitemap = crawler.fetch_sitemap('http://www.bbc.com/sitemap.xml')
    pubdate_regex = re.compile(r'"dateModified":\s*"([0-9T:+\-]{25})"')
    for url in sitemap:
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
        if title: out.write(title + '\n')
        for paragraph in re.findall(r'<p>(.+?)</p>', html):
            out.write(striptags(paragraph).strip() + '\n')


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


_HTML_ENTITIES = {
    'Auml': 'Ä',
    'Ccedil': 'Ç',
    'Eacute': 'É',
    'Euml': 'Ë',
    'Iuml': 'Ï',
    'Ouml': 'Ö',
    'Uuml': 'Ü',
    'auml': 'ä',
    'ccedil': 'ç',
    'eacute': 'é',
    'euml': 'ë',
    'icirc': 'î',
    'iuml': 'ï',
    'nbsp': ' ',
    'ouml': 'ö',
    'uuml': 'ü',
    'pound': '£',
    'quot': '"',
}


def replace_html_entities(html):
    html = re.sub(r'&#([0-9]+);', lambda z:unichr(int(z.group(1))), html)
    html = re.sub(r'&([a-zA-Z]+);',
                  lambda z:_HTML_ENTITIES[z.group(1).lower()], html)
    return html
