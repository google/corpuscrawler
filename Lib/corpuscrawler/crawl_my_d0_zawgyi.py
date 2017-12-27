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

from corpuscrawler.util import (
    find_wordpress_urls, replace_html_entities, striptags
)


def crawl(crawler):
    out = crawler.get_output(language='my-t-d0-zawgyi')
    crawl_than_lwin_times(crawler, out)


def crawl_than_lwin_times(crawler, out):
    sitemap = crawler.fetch_sitemap('http://thanlwintimes.com/sitemap.xml')
    for url in sorted(sitemap.keys()):
        html = crawler.fetch(url).content.decode('utf-8')
        pubdate = re.search(r'<meta itemprop="datePublished" content="(.+?)"',
                            html)
        if pubdate is None:
            continue
        # prepare for split; some texts use different tags
        html = html.replace('</div><pre>', '</div><p>')
        html = html.replace(
            '</div><div class="td-post-content"><p>', '</div><p>')
        if html.find('</div><p>') < 0:
            continue
        text = html.split('</div><p>')[1]
        text = text.split('<div class=\'sfsi_Sicons ')[0]
        text = text.split('</noscript>')[0]
        text = text.replace('\n', ' ')
        text = text.replace('</p>', '\n').replace('</div>', '\n')
        paragraphs = []
        for p in text.splitlines():
            p = ' '.join(striptags(replace_html_entities(p)).split())
            if p and ('>' not in p) and (p.find('"caption":') < 0):
                paragraphs.append(p)
        if len(paragraphs) > 0:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            out.write('# Publication-Date: %s\n' % pubdate.groups(1))
            for p in paragraphs:
                out.write(p + '\n')
