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
from corpuscrawler.util import cleantext, crawl_udhr, extract, urlencode


def crawl(crawler):
    out = crawler.get_output(language='pa')
    crawl_udhr(crawler, out, filename='udhr_pan.txt')
    crawl_jagbani_punjabkesari_in(crawler, out)


def crawl_jagbani_punjabkesari_in(crawler, out):
    urls = set()
    main = crawler.fetch('http://jagbani.punjabkesari.in/')
    assert main.status == 200, main.status
    menu = extract('<nav id="menu" class="menu">', '</nav>',
                   main.content.decode('utf-8'))
    urls_re = re.compile(r'href="(https?://jagbani\.punjabkesari\.in/[^"]+?)"')
    category_urls = urls_re.findall(menu)
    for category_url in sorted(set([x.strip() for x in category_urls])):
        for page in range(1, 1000):
            doc = crawler.fetch(category_url + '/page/%d' % page)
            content = doc.content.decode('utf-8') if doc.status == 200 else ''
            if content.find('class="story"') < 0:
                break
            for u in urls_re.findall(
                    extract('<span class="story">', '<div class="kjpage"',
                            content)):
                urls.add(urlencode(u.strip()))
    for url in sorted(urls):
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        try:
            content = doc.content.decode('utf-8')
        except UnicodeDecodeError:
            continue
        title = extract('<title>', '</title>', content)
        text = extract('<article>', '</article>', content)
        if not text:
            continue
        text = re.sub(r'<br[^a-zA-Z][^>]*>', '<br>', text)
        text = text.replace('\n', ' ').replace('<br>', '\n')
        paras = [title] + text.splitlines()
        paras = filter(None, [cleantext(p) for p in paras])
        pubdate = re.search(
            '<meta property="article:published_time" content="([^"]+?)"',
            content)
        pubdate = pubdate.group(1) if pubdate else None
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write(('\n'.join(paras) + '\n'))
