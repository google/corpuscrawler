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
import os.path
import re

from corpuscrawler.util import clean_paragraphs, extract, find_wordpress_urls


def crawl(crawler):
    out = crawler.get_output(language='my-t-d0-zawgyi')
    _crawl_than_lwin_times(crawler, out)


def _crawl_than_lwin_times(crawler, out):
    urls = find_wordpress_urls(crawler, 'http://thanlwintimes.com/')
    for url in sorted(urls):
        if not url.endswith('/'):
            continue
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        html = doc.content.decode('utf-8')
        pubdate = re.search(
            r'<time class="entry-date updated td-module-date" '
            r'datetime="([^"]+)"', html)
        pubdate = pubdate.group(1) if pubdate else ''
        title = (extract('<title>', '</title>', html) or '').split('|')[0]
        body = extract('<div class="td-post-content">',
                       "<div class='sfsi_Sicons'", html) or ''
        body = body.split('Please follow and like us')[0]
        paragraphs = clean_paragraphs('%s<br/>%s' % (title, body))
        if len(paragraphs) > 0:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paragraphs) + '\n')
