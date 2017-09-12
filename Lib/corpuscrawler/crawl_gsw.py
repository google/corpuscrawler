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
import json
import re
from corpuscrawler.util import replace_html_entities, striptags, urljoin


def crawl(crawler):
    crawl_gsw_derbund(crawler)
    crawl_gsw_wettiger_nochrichte(crawler)
    crawl_gsw_seislerblog(crawler)


def crawl_gsw_derbund(crawler):
    urls = set()
    for i in range(1, 200):
        url = ('https://www.derbund.ch/ajax/tags.html?'
               'action=moreDossierStories&section_id=11127&page=%d'
               '&dossier_id=3069' % i)
        items = json.loads(crawler.fetch(url).content)['items']
        for path in re.findall(r'<a href="(.+?)"', ''.join(items)):
            if not path.startswith('/stichwort/autor/'):
                urls.add(urljoin('https://www.derbund.ch/', path))
        if len(items) == 0:
            break
    out = crawler.get_output('gsw-u-sd-chbe')
    for url in sorted(urls):
        text = crawler.fetch(url).content.decode('utf-8')
        pubdate = re.search(
            r'Erstellt: ([0-9]{1,2})\.([0-9]{2})\.([0-9]{4})', text)
        if pubdate is not None:
            day, month, year = pubdate.groups()
            pubdate = '%04d-%02d-%02d' % (int(year), int(month), int(day))
        out.write('# Location: %s\n' % url)
        out.write('# Genre: Blog\n')
        if pubdate is not None:
            out.write('# Publication-Date: %s\n' % pubdate)
        text = text.split('<div id="mainContent">')[1]
        text = text.split('<span class"idcode"')[0].split('(Der Bund)')[0]
        text = text.replace('***', ' ')
        if text.find('var badwordserch = 1;') >= 0:
            text = text.split('var badwordserch = 1;', 1)[1]
        paras = [' '.join(striptags(p).split()) for p in text.split('</p>')]
        for p in paras:
            if p:
                out.write(p + '\n')


def crawl_gsw_wettiger_nochrichte(crawler):
    urls = crawler.fetch_sitemap(
        'https://wettiger-nochrichte.net/sitemap.xml').keys()
    out = crawler.get_output('gsw-u-sd-chag')
    for url in sorted(urls):
        if url.find('//wettiger-nochrichte.net/20') < 0:
            continue
        html = crawler.fetch(url).content.decode('utf-8')
        pubdate = re.search(r'<time class="entry-date" datetime="(.+?)"', html)
        html = html.split('class="post-content">')
        html = html[1].split('<style')[0]
        paragraphs = []
        for p in re.split(r'</?(p|h1|h2).+?>', html):
            p = ' '.join(replace_html_entities(striptags(p)).split())
            if ((p not in ('', 'p', 'h2', 'h3')) and
                    (not p.startswith('http')) and ('<' not in p) and
                    (not p.endswith('by Wettiger Nochrichte')) and
                    (not p.endswith('by LuFiLa')) and
                    (not p.endswith('by Wettiger'))):
                paragraphs.append(p)
        if len(paragraphs) > 0:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate.group(1))
            for p in paragraphs:
                out.write(p + '\n')


def crawl_gsw_seislerblog(crawler):
    urls = set()
    for i in range(1, 16):
        indexurl = ('http://www.freiburger-nachrichten.ch/blogs/seislerblog'
                    '?page=%d' % i)
        html = crawler.fetch(indexurl).content.decode('utf-8')
        for url in re.findall(r'<a href="(/blogs/seislerblog/.+?)[\s"]', html):
            urls.add(urljoin(indexurl, url))
    out = crawler.get_output('gsw-u-sd-chfr')
    for url in sorted(urls):
        out.write('# Location: %s\n' % url)
        out.write('# Genre: Blog\n')
        text = crawler.fetch(url).content.decode('utf-8')
        pubdate = re.search(
            r'<span class="date-created">([0-9]{1,2})\.([0-9]{2})\.'
            '(20[0-9]{2})</span>', text)
        if pubdate != None:
            day, month, year = pubdate.groups()
            pubdate = '%04d-%02d-%02d' % (int(year), int(month), int(day))
            out.write('# Publication-Date: %s\n' % pubdate)
        text = text.split('<h1>', 1)[-1].split('<section')[0]
        text = text.replace('\n', ' ')
        for tag in ('</p>', '</h1>', '</div>'):
            text = text.replace(tag, '\n')
        for p in [' '.join(striptags(t).strip().split())
                  for t in text.splitlines()]:
            if p and p != 'Kommentare':
                out.write(p + '\n')
 
