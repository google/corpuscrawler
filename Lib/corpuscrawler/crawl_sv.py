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
from corpuscrawler.util import crawl_udhr


def crawl(crawler):
    out = crawler.get_output(language='sv')
    crawl_udhr(crawler, out, filename='udhr_swe.txt')
    crawl_sverigesradio(crawler, out, program_id=4916)


def crawl_sverigesradio(crawler, out, program_id):
    sitemap = crawler.fetch_sitemap(
        'http://sverigesradio.se/sida/sitemap.aspx')
    urlpart = 'programid=%d&' % program_id
    for url in sorted(sitemap):
        if url.find(urlpart) < 0:
            continue
        page = crawler.fetch(url)
        if page.status != 200:
            continue
        html = page.content.decode('utf-8')
        # text = html.split('<p>', 1)[1]
        # text = text.split('<p class="byline"', 1)[0]
        # text = text.split('<h2 class="label', 1)[0]
        # text = text.replace('\n', ' ').replace('\r', ' ')
        # text = text.replace('</p>', '\n').replace('</div>', '\n')
        # paras = text.splitlines()
