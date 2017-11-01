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

def _scrape_maoritelevision(crawler, out):
    articlelist = set()
    articlelist.add('http://www.maoritelevision.com/mi/purongo/purongo-hou')
    for i in range(1, 100):
        articlelist.add('http://www.maoritelevision.com/mi/purongo/purongo-hou?page=%d' % i)
    links = set()
    for url in articlelist:
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        content = doc.content.decode('utf-8')
        for articlepiece in content.split('<article')[1:]:
            for link in re.findall('<a href="(/mi/purongo/[^"]*)"', articlepiece):
                links.add('http://www.maoritelevision.com%s' % link)
    for link in links:
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        html = doc.content.decode('utf-8')
        if '<html  lang="mi"' not in html:
            continue
        if 'itemprop="articleBody"' not in html:
            continue
        pubdate_match = pubdate_regex.search(html)
        pubdate = pubdate_match.group(1) if pubdate_match else None
        if pubdate is None: pubdate = doc.headers.get('Last-Modified')
        if pubdate is None: pubdate = sitemap[url]
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate: out.write('# Publication-Date: %s\n' % pubdate)
        # These news stories are a parallel (or at least comparable) corpus, so keeping
        # the link to the English article
        english = re.search(r'<a href="(/news/[^"]*)" class="language-link" lang="en">', html)
        if english: english = 'http://www.maoritelevision.com%s' % english.group(1)
        if english: out.write('English: %s\n' % english)
        tags = set()
        tagshtml = html.split('<ul class="tags">')[1].split('</ul>')[0]
        for tag in re.findall(r'<a href="(?:[^"]*)">([^<]*)</a>', tagshtml):
            tags.add(cleantext(tag))
        if len(tags) is not 0:
            out.write('Tags: %s' % ', '.join(tags))
        title = re.search(r'<title>(.+?)</title>', html)
        if title: title = striptags(title.group(1).split('| Māori')[0]).strip()
        if title: out.write(cleantext(title) + '\n')
        articlehtml = html.split('class="field-body"')[1].split('</div>')[0]
        for paragraph in re.findall(r'<p>(.+?)</p>', articlehtml):
            out.write(cleantext(paragraph) + '\n')
