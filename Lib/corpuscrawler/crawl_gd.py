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

from corpuscrawler.util import crawl_bbc_news, crawl_udhr


def crawl(crawler):
    out = crawler.get_output(language='gd')
    crawl_udhr(crawler, out, filename='udhr_gla.txt')
    crawl_bbc_news(crawler, out, urlprefix='/naidheachdan/')
    _crawl_dasg(crawler, out)

def _crawl_dasg(crawler, out):
    base = 'https://dasg.ac.uk/text/'
    listdoc = crawler.fetch(base)
    assert listdoc.status() == 200
    listcontent = listdoc.content.decode('utf-8')
    links = set()
    for doclink in re.findall('<a href="([^\.]*).txt">', listcontent):
        links.add('%s%s.txt' % (base, doclink))
    for url in links:
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        text = doc.content.decode('utf-8')
        text = re.sub(r'<eng>([^<]*)<gai>', '', text)
        out.write('# Location: %s\n' % url)
        out.write('# Genre: Fiction\n')
        out.write(text + '\n')

