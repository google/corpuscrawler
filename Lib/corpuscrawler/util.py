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
from builtins import open, bytes, chr
import base64
import codecs
import collections
import datetime
import hashlib
import os
import random
import re
import ssl
import struct
import time
import unicodedata
import urllib
import zlib
import json

try:
    import xml.etree.cElementTree as etree
except ImportError:
    import xml.etree.ElementTree as etree
unichr = chr
try:
    # Python 2
    from cStringIO import StringIO
    import robotparser
    from urlparse import urljoin, urlparse, urlunparse
    from urllib2 import Request, urlopen, HTTPError
    from mimetools import Message
    from urllib import quote
    import urllib2
    from htmlentitydefs import name2codepoint
    py3 = False
    
except ImportError:
    # Python 3
    from io import StringIO
    import urllib.robotparser as robotparser
    from urllib.parse import urljoin, urlunparse, urlparse
    from urllib.error import HTTPError
    from urllib.request import urlopen, Request
    from email import message_from_string as Message
    from urllib.parse import quote
    from html.entities import name2codepoint
    py3 = True



# FetchResult: struct with information about a downloaded page
# headers: instance of Message
# content: byte string
# status: integer
# filepath: path to the cache file
FetchResult = collections.namedtuple('FetchResult',
                                     ['headers', 'content', 'status', 'filepath'])


def daterange(start, end):
    for n in range(int((end - start).days)):
        yield start + datetime.timedelta(n)


_TAG_REGEX = re.compile(r'\<.+?\>', flags=re.DOTALL)
def striptags(s):
    return _TAG_REGEX.sub('', s)


def urlpath(url):
    "'http://example.org/foo/bar.html?baz#qux' --> '/foo/bar.hml'"
    return urlparse(url)[2]


def urlencode(url):
    p = list(urlparse(url))
    #print(p)
    
    if not py3:
        p[1] = p[1].encode('idna')
        for i in range(2, len(p)):
            p[i] = quote(p[i].encode('utf-8'))
    #print(p)
    if py3:
        return urlunparse(p)
    else:
        return urlunparse(p).encode('utf-8')


class Crawler(object):
    def __init__(self, language, output_dir, cache_dir, crawldelay):
        assert len(language) >= 2
        self.language = language
        self.cache_dir = cache_dir
        self.output_dir = output_dir
        self.outputs = {}  # bcp47 tag (eg. 'rm-puter') --> codecs.StreamWriter
        self.robotcheckers = {}
        self.useragent = 'LinguisticCorpusCrawler/1.0'
        self.useragent_for_robots_txt = self.useragent.split('/')[0]
        self.crawldelay = crawldelay  # seconds between fetches (default 15)
        # Set this to ssl.SSLContext(ssl.PROTOCOL_TLSv1) if necessary for your site:
        self.context = None
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

    def fetch(self, url, redirections=None, fetch_encoding='utf-8'):
        if not self.is_fetch_allowed_by_robots_txt(url):
            print('Skipped:        %s' % url)
            return FetchResult(headers='', content='', status=403, filepath=None)
        try:
            digest = hashlib.sha256(url.encode('utf-8')).digest()
            filepath = os.path.join(self.cache_dir,
                "f" + base64.urlsafe_b64encode(digest).decode('utf-8'))
        except:
            digest = hashlib.sha256(url).digest()
            filepath = os.path.join(self.cache_dir,
                "f" + base64.urlsafe_b64encode(digest))

        try:
            with open(filepath, 'r', encoding='utf-8-sig', newline='') as f:
                cached = f.read().split('\r\n\r\n\r\n', 1)
            if len(cached) == 2:
                print('Cache-Hit:      %s' % url)
                headers, content = cached
                try:
                    content = content.encode('utf-8')
                except:
                    # already encoded as bytes
                    pass
                if py3:
                    headers = Message(headers)
                else:
                    headers = Message(StringIO(headers))
                status = int(headers.get('Status', '200').split()[0])
                return FetchResult(headers, content, status, filepath)
        except IOError:
            pass

        print('Downloading:    %s' % url)
        delay = random.uniform(self.crawldelay, self.crawldelay + 2)  # jitter
        time.sleep(delay)
        request = Request(url, headers={'User-Agent': self.useragent})
        try:
            response = urlopen(request, context=self.context)
        except HTTPError as err:
            response = err
        except UnicodeDecodeError as err:
            # The Arabic edition of Sputnik News sometimes emits redirects
            # which the urllib2 module of Python 2.7.13 tries to follow,
            # but then it causes an urllib2-internal crash.  We catch the
            # error here, and return it as '400 Bad Request' to our caller.
            return FetchResult({}, 'Bad Request: UnicodeDecodeError', 400, None)
        status = response.getcode()
        content = response.read().decode(fetch_encoding).encode('utf-8')
        response.close()
        if status == 200 or status >= 400 and status <= 499:
            with open(filepath, 'wb') as f:
                f.write(b'Status: %d\r\n' % response.getcode())
                f.write(str(response.headers).rstrip().encode('utf-8'))
                f.write(b'\r\n\r\n\r\n')
                f.write(content)
        return FetchResult(response.headers, content, status, filepath)

    def fetch_content(self, url, allow_404=False):
        doc = self.fetch(url)
        if not allow_404:
            assert doc.status == 200, (doc.status, url)
        try:
            return doc.content.decode('utf-8')
        except:
            return doc.content

    def fetch_sitemap(self, url, processed=set(), subsitemap_filter=lambda x: True):
        """'http://example.org/sitemap.xml' --> {url: lastmod}"""
        result = {}
        doc = self.fetch(url)
        assert doc.status == 200, (doc.status, url, doc.filepath)
        content = doc.content
        if content.startswith(b'\x1F\x8B'):
            content = zlib.decompress(content, zlib.MAX_WBITS|32)
        if content.startswith(b'\n'):
            content = content[1:]
        try:
            sitemap = etree.fromstring(content)
        except etree.ParseError:
            return {}
        xmlns = 'http://www.sitemaps.org/schemas/sitemap/0.9'  # XML namespace
        submap1 = sitemap.findall('{%s}sitemap/{%s}loc' % (xmlns, xmlns))
        submap2 = sitemap.findall('sitemap/loc')
        for s in submap1 + submap2:
            subsitemap = s.text.strip()
            # prevent infinite recursion
            if subsitemap in processed:
                continue
            if not subsitemap_filter(subsitemap):
                continue
            processed.add(subsitemap)
            result.update(self.fetch_sitemap(subsitemap, processed))
        locpath, lastmodpath = '{%s}loc' % xmlns, '{%s}lastmod' % xmlns
        for urlinfo in sitemap.findall('{%s}url' % xmlns) + sitemap.findall('url'):
            location = urlinfo.find(locpath)
            if location is None:
                location = urlinfo.find('loc')
            if location is None:
                continue
            location = location.text.strip()
            lastmod = urlinfo.find(lastmodpath)
            if lastmod is None:
                lastmod = urlinfo.find('lastmod')
            if lastmod is not None:
                try:
                    lastmod = lastmod.text.strip()
                    if len(lastmod) == 0:
                        lastmod = None
                except AttributeError:
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
            checker.parse(robots_txt.decode('utf-8'))
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

    def crawl_pngscriptures_org(self, out, language):
        urlprefix = 'https://png.bible/%s/' % language
        copy = self.fetch(urlprefix + 'copyright.htm')
        assert copy.status == 200, copy.status
        license_url = re.search(
            r"href='(https?://creativecommons.org/licenses/[^']+?)'",
            copy.content.decode('utf-8')).group(1)
        license_url = license_url.replace('http:', 'https:')
        for url in sorted(self._find_urls_on_pngscriptures_org(language)):
            doc = self.fetch(url)
            assert doc.status == 200, (doc.status, url)
            text = extract('<div class="main">', "<ul class='tnav'>",
                           doc.content.decode('utf-8'))
            text = text.replace('\n', ' ')
            text = re.sub(r'</(?:div|DIV|p|P|[hH][1-6]|table|TABLE)>', '\n',
                          text)
            text = re.sub(r'<(?:br|BR)\s*/?>', '\n', text)
            text = re.sub(r'<span class="verse".+?</span>', ' ', text,
                          flags=re.DOTALL)
            text = re.sub(r'<span class="popup".+?</span>', ' ', text,
                          flags=re.DOTALL)
            paras = filter(None, [cleantext(p) for p in text.splitlines()])
            if paras:
                out.write('# Location: %s\n' % url)
                out.write('# Genre: Religion\n')
                out.write('# License: %s\n' % license_url)
                out.write('\n'.join(paras) + '\n')

    def _find_urls_on_pngscriptures_org(self, language):
        urlprefix = 'https://png.bible/%s/' % language
        index = self.fetch(urlprefix)
        assert index.status == 200, index.status
        booklist = extract("class='bookList'>", "</div>",
                           index.content.decode('utf-8'))
        urls = set()
        for book in re.findall(r"class='nn' href='(.{3})\d*\.htm'", booklist):
            bookurl = urlprefix + book + '.htm'
            doc = self.fetch(bookurl)
            assert doc.status == 200, (doc.status, bookurl)
            for ref in re.findall(r"href='(%s\d+\.htm)'" % book,
                                  doc.content.decode('utf-8'))[1:]:
                urls.add(urlprefix + ref)
        return urls

    def crawl_abc_net_au(self, out, program_id):
        index_url = "https://www.abc.net.au/news/%s/" % program_id
        article_re = re.compile(r'href="(/%s/[^"]+)"' % program_id)
        next_re = re.compile(r'<a class="next" href="(\?page=[0-9]+)">')

        urls = set()
        current_url = index_url
        while True:
            response = self.fetch(current_url)
            if response.status != 200:
                continue
            html = response.content.decode('utf-8')
            for url in article_re.findall(html):
                urls.add("https://www.abc.net.au/news" + url)
            next = next_re.search(html)
            if not next:
                break
            current_url = index_url + next.group(1)
            break

        prefix = '/news/%s/' % program_id
        for url in sorted(urls):
            pubdate = re.search(r'/(20\d{2}-\d{2}-\d{2})/', url)
            if pubdate is None or not urlpath(url).startswith(prefix):
                continue
            pubdate = pubdate.group(1)
            doc = self.fetch(urlencode(url))
            if doc.status != 200:
                continue
            content = doc.content.decode('utf-8')
            title = extract('<h1 itemprop="name">', '</h1>', content)
            text = extract('itemprop=text >', '<div class="view-comments" >', content)
            if not title or not text:
                continue
            text = re.sub('<div.*', '', text, flags=re.DOTALL)
            paras = clean_paragraphs('<h1>%s</h1>%s' % (title, text))
            if not paras:
                continue
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')

    def crawl_churchio(self, out, bible_id):
        url = ('https://raw.githubusercontent.com/churchio/open-bibles/' +
               ('master/%s.usfx.xml' % bible_id))
        doc = etree.fromstring(self.fetch(url).content)
        for book in doc.findall('book'):
            paras = ''.join(book.itertext()).splitlines()
            paras = [' '.join(p.split()) for p in paras]
            out.write('# Location: %s#%s\n' % (url, book.attrib['id']))
            out.write('# Genre: Religion\n')
            out.write(
                '# License: '
                'https://creativecommons.org/publicdomain/mark/1.0/\n')
            out.write('\n'.join(paras) + '\n')

    def crawl_aps_dz(self, out, prefix):
        urls = set()
        if prefix in {'arb/'}:
            science_category = 'sante-science-tech'
        else:
            science_category = 'sante-sciences-tech'
        for category in ['algerie', 'economie', 'societe', 'culture', 'sport',
                       'monde', 'regions', science_category]:
            category_url = 'http://tamazight.aps.dz/' + prefix + category
            category_html = self.fetch_content(category_url)
            starts = re.findall(r'/%s\?start=(\d+)' % category, category_html)
            last_page = max([int(x) for x in starts])
            for p in range(0, last_page + 1, 10):
                html = self.fetch_content(category_url + '?start=%d' % p)
                for u in re.findall(
                        r'href="(/%s%s/[^"]+)"' % (prefix, category), html):
                    urls.add('http://tamazight.aps.dz' + u)
        for url in sorted(urls):
            doc = self.fetch(urlencode(url))
            if doc.status != 200:
                continue
            html = doc.content.decode('utf-8')
            pubdate = extract('<span class="itemDateCreated">',
                              '</span>', html)
            pubdate = re.search(
                '(\d{1,2}) ([a-zA-Zéû]+) (20\d{2}) (\d{2}):(\d{2})',
                pubdate or '')
            if pubdate:
                day, month, year, hour, minute = pubdate.groups()
                month = _FRENCH_MONTHS[month]
                pubdate = '%04d-%02d-%02dT%02d:%02d:00Z' % (
                    int(year), month, int(day), int(hour), int(minute))
            title = extract('<h2 class="itemTitle">', '</h2>', html) or ''
            content = extract('<div class="itemFullText">',
                              '<div class="itemContentFooter">', html) or ''
            paras = clean_paragraphs('<p/>'.join([title, content]))
            if paras:
                out.write('# Location: %s\n' % url)
                out.write('# Genre: News\n')
                if pubdate:
                    out.write('# Publication-Date: %s\n' % pubdate)
                out.write('\n'.join(paras) + '\n')

    def crawl_sverigesradio(self, out, program_id):
        sitemap = self.fetch_sitemap(
            'http://sverigesradio.se/sida/sitemap.aspx')
        urlpart = 'programid=%d&' % program_id
        for url in sorted(sitemap):
            if url.find(urlpart) < 0:
                continue
            page = self.fetch(url)
            if page.status != 200:
                continue
            html = page.content.decode('utf-8').replace('<P>', '<p>')
            title = re.search(r'<h1>(.+?)</h1>', html, re.DOTALL)
            title = title.group(1) if title else None
            if html.find('<div class="episode-details__body">') > 0:
                text = html.split('<div class="episode-details__body">', 1)[1]
            else:
                text = html.replace('<P>', '<p>').split('<p>', 1)[1]
            for separator in (
                    '<p class="byline"',
                    '<h2 class="label',
                    '<div class="article-details__buttons',
                    '<div class="article-details__menu',
                    '<div class="article-details__polls',
                    '<div class="article-details__related',
                    '<div class="article-details__share',
                    '<div class="episode-details__buttons"',
                    '<div class="episode-details__menu',
                    '<div class="episode-details__polls',
                    '<div class="article-details__related',
                    '<div class="episode-details__share"',
                    '<div class="puff-audio-medium__footer"',
                    '<div class="puff-medium__footer"'):
                text = text.split(separator, 1)[0]
            if text.find('function isValidBrowser') >= 0:
                continue
            text = text.replace('\n', ' ').replace('\r', ' ')
            for tag in ('</p>', '</div>', '</li>', '<br>', '<br/>', '<br />'):
                text = text.replace(tag, '\n').replace(tag.upper(), '\n')
            paras = [cleantext(p) for p in [title] + text.splitlines() if p]
            paras = filter(None, paras)
            if not paras:
                continue
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            out.write('\n'.join(paras) + '\n')

    def crawl_voice_of_america(self, out, host, ignore_ascii=False):
        site = 'https://%s' % host
        sitemap = self.fetch_sitemap(urljoin(site, 'sitemap.xml'))
        for url in sorted(sitemap.keys()):
            doc = self.fetch(url)
            if doc.status != 200:
                continue
            try:
                html = doc.content.decode('utf-8')
            except UnicodeDecodeError:
                print('Unicode Error:  %s' % url)
                continue
            title = re.search(r'<title>(.+?)</title>', html)
            title = title.group(1) if title else ''
            pubdate = re.search(
                r'<div class="published">\s*<span class="date"\s*>\s*'
                r'<time datetime="(.+?)"', html)
            pubdate = cleantext(pubdate.group(1)) if pubdate else ''
            if pubdate.startswith('1900'):
                pubdate = ''
            description = re.search(
                r'<meta name="description" content="(.+?)"', html)
            description = description.group(1) if description else ''
            if description == title:
                description = ''
            paragraphs = [title, description]
            if html.find('<div class="intro content-offset">') > 0:
                intro = html.split('<div class="intro content-offset">', 1)[1]
                intro = intro.split('</div')[0]
                intro = intro.replace('</p>', '\n').replace('</P>', '\n')
                paragraphs.extend(intro.splitlines())
            if html.find('<div class="wsw">') > 0:
                content = html.split('<div class="wsw">', 1)[1]
                content = content.split('<div')[0]
                content = content.replace('</p>', '\n').replace('</P>', '\n')
                paragraphs.extend(content.splitlines())
            paragraphs = filter(None, [cleantext(p) for p in paragraphs])
            paragraphs = [p for p in paragraphs if not p.startswith('VOA')]
            if ignore_ascii:
                paragraphs = [p for p in paragraphs
                              if not (ord(p[0]) >= 0x30 and ord(p[0]) <= 0xff)]
            if len(paragraphs) > 0:
                out.write('# Location: %s\n' % url)
                out.write('# Genre: News\n')
                if pubdate:
                    out.write('# Publication-Date: %s\n' % pubdate)
                out.write('\n'.join(paragraphs) + '\n')


    def set_context(self, context):
        self.context = context


# Normally we put site-specific logic into the language-specific scripts,
# but a couple sites have large amounts of text in many underserved languages,
# using the same site structure for all languages.
def crawl_bbc_news(crawler, out, urlprefix):
    # sitemap = {'http://www.bbc.com/burmese/world-41146701': None}
    sitemap = {}
    for s in ('http://www.bbc.com/sitemap.xml',
              'http://www.bbc.com/sitemaps/index-com-news.xml',
              'http://www.bbc.com/sitemaps/index-com-archive.xml',
              'https://www.bbc.com/sitemaps/https-index-com-archive.xml',
              'https://www.bbc.com/sitemaps/https-index-com-news.xml'):
        sitemap.update(crawler.fetch_sitemap(s))
    sitemap = {u.replace('http://', 'https://'): d for u, d in sitemap.items()}
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


def crawl_deutsche_welle(crawler, out, prefix, need_percent_in_url=False):
    urls = set()
    for url in crawler.fetch_sitemap(
        'http://www.dw.com/sitemap.xml',
        subsitemap_filter=lambda s: s.startswith('http://www.dw.com%s' % prefix),
    ):
        path = urlpath(url)
        if need_percent_in_url and '%' not in path:
            continue
        if path.startswith(prefix) and \
                (re.match(r'/[^/]+/\d{2}-.*', path) is None):  # German lessons
            urls.add(url)
    for url in sorted(urls):
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        try:
            html = doc.content.decode('utf-8')
        except UnicodeDecodeError:
            print('Unicode Error:  %s' % url)
            continue
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


def crawl_radio_free_asia(crawler, out, edition, start_year=1998):
    urls = set()
    article_re = re.compile(
        (r'href="(https://www.rfa.org/%s/.+?[0-9]{6,}\.html' +
         r'(?:\?encoding=simplified)?)"') % edition)
    for year in range(start_year, datetime.datetime.today().year + 1):
        for page_num in range(0, 100000, 30):
            archive_url = (
                'https://www.rfa.org/%s/story_archive?b_start:int=%d&year=%d'
                % (edition, page_num, year))
            response = crawler.fetch(archive_url)
            if response.status != 200:
                continue
            html = response.content.decode('utf-8')
            teaser = html.split('<nav class="pagination">')[0]
            for t in teaser.split('class="sectionteaser')[1:]:
                for url in article_re.findall(t):
                  if edition == 'cantonese':
                      url = url.replace('encoding=simplified',
                                        'encoding=traditional')
                  urls.add(url)
            if html.find('class="next"') < 0:
                break

    for url in sorted(urls):
        response = crawler.fetch(url)
        if response.status != 200:
            continue
        html = response.content.decode('utf-8')
        title = re.search(r'<title>(.+)</title>', html)
        pubdate = re.search(r'"datePublished": "([^"]+)"', html)
        if not title or not pubdate:
            continue
        title, pubdate = cleantext(title.group(1)), cleantext(pubdate.group(1))
        teaser = re.search(r'<div id="storyteaser">(.+?)</div>', html,
                           re.DOTALL)
        teaser = teaser.group(1).splitlines() if teaser else []
        text = html.split('<div id="storytext">', 1)[1]
        text = re.sub(r'<audio.+?</audio>', ' ', text)
        text = text.split('<ul class="audio">')[0]
        text = text.split('<div class="copyright">')[0]
        text = text.split('</div><!-- story_text -->')[0]
        text = text.replace('\n', ' ').replace('\r', ' ').replace('</p>', '\n')
        paras = [cleantext(p) for p in [title] + teaser + text.splitlines()]
        paras = [p for p in paras
                 if p and p.find('var ') < 0 and p.find('autoPlay') < 0
                 and p.find('playerFile') < 0]
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        out.write('# Publication-Date: %s\n' % pubdate)
        out.write('\n'.join(paras) + '\n')


def crawl_sputnik_news(crawler, out, host):
    sitemap_url = 'https://%s/sitemap_article_index.xml' % host
    for url in sorted(crawler.fetch_sitemap(sitemap_url)):
        response = crawler.fetch(urlencode(url))
        if response.status != 200:
            continue
        try:
            html = response.content.decode('utf-8')
        except UnicodeDecodeError:
            print('Unicode Error:  %s' % url)
            continue
        title = re.search(r'<title>(.+?)</title>', html)
        if title is None:
            continue
        title = title.group(1)
        pubdate = re.search(
            r'<meta content="([^"]+)" itemprop="datePublished"', html)
        if pubdate is None:
            continue
        pubdate = pubdate.group(1)
        lead = re.search(
            r'<div itemprop="description" class="b-article__lead">(.+?)</div>',
            html, re.DOTALL)
        lead = lead.group(1) if lead is not None else ''
        body = re.search(
            r'<div itemprop="articleBody" class="b-article__text">(.+?)</div>',
            html, re.DOTALL)
        if body is not None:
            body = body.group(1).replace('\n', ' ').replace('</p>', '\n')
        else:
            body = ''
        paras = [title, lead] + body.splitlines()
        paras = filter(None, [cleantext(p) for p in paras])
        if not paras:
            continue
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        out.write('# Publication-Date: %s\n' % cleantext(pubdate))
        out.write('\n'.join(paras) + '\n')


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


def crawl_voice_of_nigeria(crawler, out, urlprefix):
    assert urlprefix.startswith('/'), urlprefix
    assert urlprefix.endswith('/'), urlprefix
    site = urljoin('http://von.gov.ng/', urlprefix)
    for url in sorted(find_wordpress_urls(crawler, site)):
        if not url.endswith('/'):
            continue
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        html = doc.content.decode('utf-8')
        title = re.search(r'<h1[^>]*>(.+?)</h1>', html, re.DOTALL).group(1)
        pubdate = re.search(
            r'<meta itemprop="dateModified" content="(.+?)"', html)
        if pubdate is None:  # only a few pages with little content
            continue
        pubdate = cleantext(pubdate.group(1))
        content = re.split('<p[^>]*>', html, 1)[1].split('<footer', 1)[0]
        content = content.replace('\n', ' ').replace('</p>', '\n')
        paras = [title] + content.splitlines()
        paras = filter(None, [cleantext(p) for p in paras])
        if not paras:
            continue
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        out.write('\n'.join(paras) + '\n')


def crawl_bibleis(crawler, out, bible):
    firsturl = 'http://listen.bible.is/%s/Matt/1' % bible
    booklist = set()
    init = crawler.fetch(firsturl)
    if init.status != 200:
        return
    try:
        content = init.content.decode('utf-8')
    except UnicodeEncodeError:
        print('Unicode Error:  %s' % firsturl)
        return
    jsonraw = json.loads(content.split('__NEXT_DATA__ = ')[1].split(';__NEXT_LOADED_PAGES__')[0])
    for book in jsonraw.get('props').get('pageProps').get('books'):
        for chapter in book.get('chapters'):
            booklist.add('http://listen.bible.is/%s/%s/%d' % (bible, book['book_id'], chapter))

    for url in sorted(booklist):
        doc = crawler.fetch(url)
        pubdate = doc.headers.get('Last-Modified')
        if doc.status != 200:
            continue
        try:
            html = doc.content.decode('utf-8')
        except:
            print('Unicode Error:  %s' % url)
            continue
        if '<p>No text available for the selected Bible.</p>' in html:
            continue
        jsonraw = json.loads(html.split('__NEXT_DATA__ = ')[1].split(';__NEXT_LOADED_PAGES__')[0])
        chapter_text = jsonraw.get('props').get('pageProps').get('chapterText')
        verses = [verse.get('verse_text') for verse in chapter_text]
        out.write('# Location: %s\n' % url)
        out.write('# Genre: Religion\n')
        if pubdate: out.write('# Publication-Date: %s\n' % pubdate)
        out.write('\n'.join(verses) + '\n')


def crawl_tipitaka(crawler, out, script):
    tocs_to_crawl = []
    content_to_crawl = []
    tocs_to_crawl.append('https://tipitaka.org/%s/tipitaka_toc.xml' % script)
    while tocs_to_crawl:
        url = tocs_to_crawl.pop()
        fetchresult = crawler.fetch(url, fetch_encoding='utf-16')
        assert fetchresult.status == 200, (fetchresult.status, url)
        root = etree.fromstring(fetchresult.content.decode('utf-8'))
        for tree in root.findall('.//tree[@src]'):
            src = tree.get('src')
            tocs_to_crawl.append('https://tipitaka.org/%s/%s' % (script, src))
        for tree in root.findall('.//tree[@action]'):
            action = tree.get('action')
            content_to_crawl.append('https://tipitaka.org/%s/%s' % (script, action))
    for url in content_to_crawl:
        doc = crawler.fetch(url, fetch_encoding='utf-16')
        pubdate = doc.headers.get('Last-Modified')
        if doc.status != 200:
            continue
        try:
            root = etree.fromstring(doc.content.decode('utf-8'))
        except:
            print('Unicode Error:  %s' % url)
            continue
        paragraphs = root.findall('.//p')
        out.write('# Location: %s\n' % url)
        out.write('# Genre: Religion\n')
        if pubdate: out.write('# Publication-Date: %s\n' % pubdate)
        out.write('\n'.join(''.join(p.itertext()) for p in paragraphs) + '\n')


def find_wordpress_urls(crawler, site, **kwargs):
    urls = set()
    mainpage = crawler.fetch_content(site, **kwargs)
    for category in re.findall(r'/(category/[^/"]+)/?">', mainpage):
        caturl = urljoin(site, category) + '/'
        catdoc = crawler.fetch(caturl)
        assert catdoc.status == 200, (catdoc.status, caturl)
        pages = [int(n) for n in re.findall(r'/page/(\d)+/?', catdoc.content.decode('utf-8'))]
        for page in range(1, 1 + max([0] + pages)):
            pgurl = urljoin(caturl, 'page/%d/' % page) if page > 1 else caturl
            pgdoc = crawler.fetch(pgurl)
            if pgdoc.status != 200:
                print('Error %3d:      %s' % (pgdoc.status, pgurl))
                continue
            pgcontent = pgdoc.content.decode('utf-8')
            for url in re.findall(r'"(%s[^"]+)"' % site, pgcontent):
                url = replace_html_entities(url.split('#')[0])
                if url.find('/category/') < 0 and not url.endswith('/feed/'):
                    urls.add(url)
    return urls


def unichar(i):
    try:
        return unichr(i)
    except ValueError:
        # non-BMP codepoint in narrow Python build
        return struct.pack('i', i).decode('utf-32')


def replace_html_entities(html):
    entities = name2codepoint
    html = re.sub(r'&#([0-9]+);',
                  lambda z:unichar(int(z.group(1))), html)
    html = re.sub(r'&#[xX]([0-9a-fA-F]+);',
                  lambda z:unichar(int(z.group(1), 16)), html)
    html = re.sub(r'&([a-zA-Z]+);',
                  lambda z:unichar(entities.get(z.group(1).lower(), 0x20)), html)
    return html


def cleantext(html):
    html = re.sub(r'<script.+?</script>', ' ', html, flags=re.DOTALL)
    html = replace_html_entities(striptags(html))
    # Some web sites insert zero-width spaces, possibly as byte order marks
    # (from Microsoft Notepad) which their scripts failed to recognize as such.
    html = html.replace('\u200B', '')
    return unicodedata.normalize('NFC', ' '.join(html.split()))


def clean_paragraphs(html):
    text = html.replace('\n', ' ')
    text = re.sub(r'</(?:div|DIV|p|P|[hH][1-6]|table|TABLE|tr|td|article)>',
                  '\n', text)
    text = re.sub(r'<(?:br|BR)\s*/?>', '\n', text)
    return list(filter(None, [cleantext(p) for p in text.split('\n')]))


def extract(before, after, html):
    s = html.split(before, 1)
    return s[1].split(after)[0] if len(s) == 2 else None


def fixquotes(s):
    s = (' ' + s).replace(" '", " ‘").replace("'", "’")
    s = s.replace(' "', ' “').replace('"', '”')
    return s.strip()


_FRENCH_MONTHS = {
    'janvier': 1,
    'février': 2,
    'mars': 3,
    'avril': 4,
    'mai': 5,
    'juin': 6,
    'juillet': 7,
    'août': 8,
    'septembre': 9,
    'octobre': 10,
    'novembre': 11,
    'décembre': 12
}
