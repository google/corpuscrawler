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
    crawl_ainm_ie(crawler, out)
    crawl_blogspot(crawler, out, host='gaeltacht21.blogspot.com')
    crawl_blogspot(crawler, out, host='aonghus.blogspot.com')
    crawl_blogspot(crawler, out, host='nimill.blogspot.com')
    crawl_blogspot(crawler, out, host='turasailse.blogspot.com')
    crawl_blogspot(crawler, out, host='caomhach.blogspot.com')
    crawl_blogspot(crawler, out, host='breacleabhar.blogspot.com')
    crawl_blogspot(crawler, out, host='gearoid.blogspot.com')
    crawl_blogspot(crawler, out, host='philo-celtic.blogspot.com')
    crawl_blogspot(crawler, out, host='iomhannablag.blogspot.com')
    crawl_blogspot(crawler, out, host='smaointefanacha.blogspot.com')
    crawl_blogspot(crawler, out, host='imeall.blogspot.com')
    crawl_coislife_ie(crawler, out)
    crawl_meoneile_ie(crawler, out)
    crawl_peig_ie(crawler, out)
    crawl_forasnagaeilge_ie(crawler, out)

# RTE has news sites both for its own Irish language news programme
# and for Raidió na Gaeltachta
def _rtenuacht_path(url):
    rtenuacht = urlpath(url).startswith('/news/nuacht/')
    rnag = '/rnag/nuacht' in url or '/rnag/articles' in url
    return rtenuacht or rnag


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
    if re.match('^[\*\+]+$', text):
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

def _rte_cleanall(html):
    section_article_regex = re.compile(r'<section[^>]+itemprop="articleBody"[^>]*>')
    search = section_article_regex.search(html)
    out = []
    if search:
        body = extract(search.group(0), '</section>', html)
        for para in clean_paragraphs(body):
            if _rte_writable_paragraph(para):
                out.append(para)
        return '\n'.join(out)
    for paragraph in re.findall(r'<p>(.+?)</p>', html):
        cleaned = cleantext(paragraph)
        if _rte_writable_paragraph(cleaned):
            out.append(cleaned)
        else:
            continue
    return '\n'.join(out)

def crawl_nuachtrte(crawler, out):
    sitemap = crawler.fetch_sitemap(
        'https://www.rte.ie/sitemap.xml',
        subsitemap_filter=lambda x: _check_rte_sitemap(x)
        )
    pubdate_regex = re.compile(r'name="DC.date" (?:scheme="DCTERMS.URI" )?content="([0-9T:+\-]{19,25})"')
    for url in sorted(sitemap.keys()):
        if not _rtenuacht_path(url):
            continue
        if '/programmes' in url:
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
        if 'nuacht' in url:
            out.write('# Genre: News\n')
        if pubdate: out.write('# Publication-Date: %s\n' % pubdate)
        title = re.search(r'<title>(.+?)</title>', html)
        if title: title = striptags(title.group(1).split('- RTÉ')[0]).strip()
        if title: out.write(cleantext(title) + '\n')
        cleaned = _rte_cleanall(html)
        if '/sceala/' in url and '\n____' in cleaned:
            cleaned = cleaned.split('\n____')[0]
        out.write(cleaned + '\n')

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
    start = 'https://www.irishtimes.com/culture/tuarasc%C3%A1il'
    pubdatere1 = re.compile(
        r'<meta itemprop="datePublished" content="([^"]*)"/>')
    pubdatere2 = re.compile(r'"datePublished": "([^"])"')
    links = set()
    for contents in _irishtimes_section_list(crawler, out, start):
        init = crawler.fetch(contents)
        if init.status != 200:
            continue
        shtml = init.content.decode('utf-8')
        for doclink in re.findall('<a href="/culture/tuarasc%C3%A1il/([^"]*)"', shtml):
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
        if post == None:
            post = extract("<div class='post-header'>",
                           "<div class='post-footer'>", html)
        if post == None:
            post = extract('<div class="post-body">',
                           '<p class="post-footer">', html)
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

def crawl_coislife_ie(crawler, out):
    links = set()
    for num in range(1, 12):
        if num > 1:
            listurl = 'https://www.coislife.ie/product-category/ga/page/%s/' % num
        else:
            listurl = 'https://www.coislife.ie/product-category/ga/'
        idxres = crawler.fetch(listurl)
        if idxres.status != 200:
            continue
        idxhtml = idxres.content.decode('utf-8')
        index = extract('<div class="products-archive--products">',
                        '<nav class="woocommerce-pagination">', idxhtml)
        for link in re.findall(r'<a href="(https://coislife.ie/product/[^"]+)"', index):
            links.add(link)
    for url in sorted(links):
        fetchresult = crawler.fetch(url)
        if fetchresult.status != 200:
            continue
        html = fetchresult.content.decode('utf-8')
        title = re.search(r'<title>(.+?)</title>', html)
        title = title.group(1).split('&#8211;')[0].strip() if title else ''
        desc = re.search(r'<meta property="og:description" content="([^"]+?)"', html)
        desc = cleantext(desc.group(1))
        body = extract('<div class="tab-content">',
                       '<div class="entry-content in fade tab-pane" id="tab-additional_information">', html) or ''
        paras = clean_paragraphs(title + '<br/>' + body)
        pubdate = fetchresult.headers.get('Last-Modified')
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: Commerce\n')
            if desc:
                out.write ('# Description: %s\n' % desc)
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            for para in paras:
                if para.find('Léigh sliocht as an leabhar') >= 0:
                    continue
                else:
                    out.write(para + '\n')

_ENGLISH_MONTHS = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 12
}

def _byline_to_pubdate(byline):
    date = re.search(r'(\d{1,2}) ([^ ]+?) (\d{4})', byline)
    if not date:
        return None
    day = int(date.group(1))
    year = int(date.group(3))
    month = _ENGLISH_MONTHS[date.group(2).lower()]
    if not month:
        return None
    out = "{}-{:0>2d}-{:0>2d}".format(year, month, day)
    return out

def crawl_meoneile_ie(crawler, out):
    sitemap = crawler.fetch_sitemap('https://meoneile.ie/sitemap.xml')
    for url in sorted(sitemap.keys()):
        if url == 'https://meoneile.ie/':
            continue
        fetchresult = crawler.fetch(url)
        if fetchresult.status != 200:
            continue
        html = fetchresult.content.decode('utf-8')
        title = extract(r'<title>', '</title>', html).strip()
        title = title.split('&lt;')[0].strip() if title else ''
        video = re.search(r"<iframe.*src='(//player.vimeo.com/video/[0-9]+)[^>]*></iframe>", html)
        body = extract("<div class='article-content'>", '</article>', html) or ''
        byline = extract("<div class='byline'>", '</span>', html) or ''
        byline = _byline_to_pubdate(byline)
        if body.find('<strong>%s</strong>' % title) >= 0:
            title = ''
        paras = clean_paragraphs(title + '<br/>' + body)
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if video:
                out.write ('# Video: https:%s\n' % video.group(1))
            if byline:
                out.write('# Publication-Date: %s\n' % byline)
            for para in paras:
                if para == 'Roinn':
                    continue
                else:
                    out.write(para + '\n')

def _peig_filter_robots(page):
    if page.find('/wp-') >= 0:
        return False
    elif page.find('/tuairisc/') >= 0:
        return False
    elif page.find('/nuacht/') >= 0:
        return False
    elif page.find('/nos/') >= 0:
        return False
    else:
        return True

def crawl_peig_ie(crawler, out):
    crawler.set_context(ssl.SSLContext(ssl.PROTOCOL_TLSv1_2))
    sitemap = crawler.fetch_sitemap('https://peig.ie/sitemap_index.xml', subsitemap_filter=_peig_filter_robots)
    def peig_cat(page):
        if page.find('/imeachtai/') >= 0:
            return 'Events'
        elif page.find('peig.ie/20') >= 0:
            return 'News'
        elif page.find('/fol%C3%BAntais/') >= 0:
            return 'Job listings'
        else:
            return ''
    # Peig.ie has a lot of posts from other sites
    def skip_page(site):
        if site.find('//nos.ie/') >= 0:
            return True
        elif site.find('//tuairisc.ie/') >= 0:
            return True
        elif site.find('//meoneile.ie/') >= 0:
            return True
        else:
            return False
    for url in sorted(sitemap.keys()):
        if url == 'https://peig.ie/':
            continue
        fetchresult = crawler.fetch(url)
        if fetchresult.status != 200:
            continue
        html = fetchresult.content.decode('utf-8')
        title = re.search(r'<title>(.+?)</title>', html)
        title = title.group(1).split('|')[0].strip() if title else ''
        read_more = re.search(r'<a.*href="([^"]+")[^>]*>Níos mó</a>', html)
        if read_more and skip_page(read_more.group(1)):
            continue
        if '<meta property="article:modified_time"' in html:
            date = re.search(r'<meta property="article:modified_time" content="([^"]+)"', html).group(1)
        else:
            date = re.search(r'"datePublished":"([^"]+)"', html).group(1)
        body = extract('<div class="uk-margin-medium-top" property="text">', '<ul class="uk-pagination', html) or ''
        paras = clean_paragraphs(title + '<br/>' + body)
        genre = peig_cat(url)
        if paras:
            out.write('# Location: %s\n' % url)
            if genre:
                out.write('# Genre: %s\n' % genre)
            if date:
                out.write('# Publication-Date: %s\n' % date)
            out.write('\n'.join(paras) + '\n')
    crawler.set_context(ssl.SSLContext(ssl.PROTOCOL_TLSv1))

def crawl_forasnagaeilge_ie(crawler, out):
    sitemap = crawler.fetch_sitemap('https://www.forasnagaeilge.ie/sitemap_index.xml')
    pubdate_regex = re.compile(r'"datePublished":"([^"]+)",')
    for url in sorted(sitemap.keys()):
        orig_url = url
        if '?lang=en' in url:
            ga_url = url.replace('?lang=en', '')
            if ga_url in sitemap.keys():
                continue
        if '/blog-en/' in url:
            continue
        if '/corporate-information/' in url:
            continue
        if '/torthai-cuardaigh/' in url:
            continue
        fetchresult = crawler.fetch(url)
        if fetchresult.status != 200:
            continue
        html = fetchresult.content.decode('utf-8')
        if '<html class="no-js" lang="en">' in html:
            continue
        title = extract('<title>', ' - www.forasnagaeilge.ie</title>',
                        html) or ''
        pubdate_match = pubdate_regex.search(html)
        if pubdate_match:
            pubdate = pubdate_match.group(1)
        else:
            pubdate = sitemap.get(url) or sitemap[orig_url]
        body = extract(
            '<div id="main" class="container">',
            '</div><!-- /.content -->', html)
        if not body:
            continue
        paras = clean_paragraphs(body)
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            out.write('# Title: %s\n' % title)
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')


