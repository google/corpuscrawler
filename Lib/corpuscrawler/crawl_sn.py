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

from corpuscrawler.util import crawl_udhr, cleantext, find_wordpress_urls


def crawl(crawler):
    out = crawler.get_output(language='sn')
    crawl_udhr(crawler, out, filename='udhr_sna.txt')
    crawler.crawl_voice_of_america(out, host='www.voashona.com')
    crawl_kwayedza(crawler, out)


def crawl_kwayedza(crawler, out):
    urls = find_wordpress_urls(crawler, site='http://www.kwayedza.co.zw/')
    for url in sorted(urls):
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        try:
            html = doc.content.decode('utf-8')
        except UnicodeDecodeError:
            continue
        title = re.search(r'<title>(.+?)</title>', html)
        title = title.group(1) if title else None
        if html.find('itemprop="articleBody"') < 0:
            continue
        pubdate = re.search(r'datetime="(.+?)" itemprop="datePublished"', html)
        if pubdate:
            pubdate = cleantext(pubdate.group(1))
        body = html.split('itemprop="articleBody"', 1)[1].split('>', 1)[1]
        body = body.split('<!-- .post-content -->')[0]
        body = body.split('<div class="post-share">')[0]
        body = body.replace('</p>', '\n').replace('</div>', '\n')
        paras = [title] + body.splitlines()
        paras = filter(None, [cleantext(p) for p in paras])
        if not paras:
            continue
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        out.write('\n'.join(paras) + '\n')
