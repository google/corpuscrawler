# coding: utf-8
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
import re
from corpuscrawler.util import clean_paragraphs, crawl_udhr, extract


def crawl(crawler):
    out = crawler.get_output(language='tt')
    crawl_udhr(crawler, out, filename='udhr_tat.txt')
    _crawl_vatantat_ru(crawler, out)


def _crawl_vatantat_ru(crawler, out):
    index = crawler.fetch_content('http://www.vatantat.ru/')
    last = max([int(p) for p in re.findall(r'index\.php\?pg=(\d+?)"', index)])
    for page in range(2, last + 1):
        url = 'http://www.vatantat.ru/index.php?pg=%d' % page
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        content = doc.content.decode('utf-8')
        html = extract('<p><span style="font-size: large;"><strong>',
                       '<span style="font-size: 80%; font-weight: bold;">',
                       content)
        if not html:
            continue
        html = html.split('(“Ватаным Татарстан”,')[0]
        html = html.split('<script>')[0]
        paras = clean_paragraphs(html)
        if not paras:
            continue
        pubdate = re.search(
            r'Татарстан”,&nbsp;&nbsp;&nbsp;/№&nbsp;(none|\d+),&nbsp;'
            r'(\d\d)\.(\d\d)\.(20\d\d)/', content)
        if pubdate is not None:
            pubdate = ('%s-%s-%s' %
                       (pubdate.group(4), pubdate.group(3), pubdate.group(2)))
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        out.write('\n'.join(paras) + '\n')
