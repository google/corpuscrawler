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
from corpuscrawler.util import clean_paragraphs, extract


def crawl(crawler):
    out = crawler.get_output(language='be-tarask')
    _crawl_svaboda_org(crawler, out)


def _crawl_svaboda_org(crawler, out):
    sitemap = crawler.fetch_sitemap('https://www.svaboda.org/sitemap.xml')
    for url in sorted(sitemap):
        if (url == 'https://www.svaboda.org/' or
                url.startswith('https://www.svaboda.org/z/')):  # index pages
            continue
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        html = doc.content.decode('utf-8')
        title = extract('<title>', '</title>', html) or ''
        pubdate = re.search(
            r'<div class="published">\s*<span class="date"\s*>'
            r'\s*<time datetime="([^"]+)"', html)
        pubdate = pubdate.group(1) if pubdate else None
        body = extract('<div class="body-container">', '<div id="comments"',
                       html) or ''
        paras = clean_paragraphs('%s<p/>%s' % (title, body))
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')
