# coding: utf-8
#
# Copyright 2017 Google LLC
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

from corpuscrawler.util import (crawl_udhr, clean_paragraphs, extract,
                                urlencode, urljoin)

BLACKLIST = {
    # Multi-lingual documents.
    'http://www.rtl.lu/auto/archiv/1044287.html',
    'http://www.rtl.lu/auto/archiv/1056059.html',
    'http://www.rtl.lu/auto/archiv/1061260.html',
}


def crawl(crawler):
    out = crawler.get_output(language='lb')
    crawl_udhr(crawler, out, filename='udhr_ltz.txt')
    _crawl_rtl_lu(crawler, out)


def _crawl_rtl_lu(crawler, out):
    urls = set()
    homepage = crawler.fetch_content('http://www.rtl.lu/')
    cats = extract('<!-- MAIN NAVIGATION -->', '</header>', homepage)
    for cat in re.findall(r'href="(https?://www\.rtl\.lu/[^"]+?)">', cats):
        caturl = cat + 'archiv/'
        if cat.find('/sport/') > 0:
            caturl = caturl + 'all/'
        doc = crawler.fetch(caturl)
        if doc.status != 200:
            continue
        content = doc.content.decode('utf-8')
        num_pages = re.search(r'archiv\?p=(\d+)" class="last">&raquo', content)
        num_pages = int(num_pages.group(1)) if num_pages else 0
        for p in range(1, num_pages + 1):
            page = crawler.fetch_content(caturl[:-1] + '?p=%d' % p)
            html = extract('<div class="teaser archive-header">',
                           '<div class="pager">', page)
            if not html:
                continue
            for url in re.findall(r'href="([^"]+?)"', html):
                urls.add(urlencode(urljoin('http://www.rtl.lu/', url)))
    for url in sorted(urls):
        if url in BLACKLIST:
            continue
        doc = crawler.fetch_content(url)
        header = extract('<header>', '</header>', doc) or ''
        if header:
            header = header.replace('</span>', ' ')
        pubdate = re.search(
            '(\d{1,2})\.(\d{1,2}).(20\d{2}), (\d\d):(\d\d):(\d\d)</li>', doc)
        if pubdate:
            pd = [int(x) for x in pubdate.groups()]
            pubdate = '%04d-%02d-%02dT%02d:%02d:%02d+02:00' % (
                pd[2], pd[1], pd[0], pd[3], pd[4], pd[5])
        if doc.find('<section class="mainbar-right omega body">') > 0:
            start_tag = '<section class="mainbar-right omega body">'
        else:
            start_tag = '<p>'
        content = extract(start_tag, '<!-- BEGIN Comments -->', doc) or ''
        content = re.sub(r'<script.+?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<form.+?</form>', '', content, flags=re.DOTALL)
        content = content.split('<footer')[0]
        content = content.split('<div class="pager"')[0]
        paras = clean_paragraphs(header + '<p/>' + content)
        paras = [p for p in paras
                 if (p.find('Vous souhaitez faire') < 0 and
                     p != 'äre Commentaire' and
                     not p.startswith('####'))]
        text = '\n'.join(paras)
        # Filter out some articles in French or German.
        if (text.find(' est ') >= 0 or text.find(' ist ') >= 0 or
            text.find(' Ist ') >= 0 or text.find(' dit ') >= 0 or
            text.find(' veut') >= 0):
                continue
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')
