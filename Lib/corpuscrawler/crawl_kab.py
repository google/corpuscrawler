# Copyright 2018 Google LLC
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
from corpuscrawler.util import cleantext, crawl_udhr, urlencode


def crawl(crawler):
    out = crawler.get_output(language='kab')
    crawler.crawl_aps_dz(out, prefix='tal/')
    crawl_tamurt(crawler, out)


def crawl_tamurt(crawler, out):
    for url in sorted(find_tamurt_urls(crawler)):
        doc = crawler.fetch(url)
        assert doc.status == 200, (doc.status, url)
        html = doc.content.decode('utf-8')
        title = re.search(r'<title>(.+?)</title>', html).group(1)
        title = title.rstrip(' - Tamurt')
        pubdate = re.search(
            r'<meta property="article:published_time" content="([^"]+)"', html)
        pubdate = pubdate.group(1).strip()
        content = '<div ' + html.split('<div class="entry-content"', 1)[1]
        content = content.split('<!-- .entry-content -->')[0]
        content = re.sub(r'<!--.+?-->', '', content)
        paras = [title] + content.replace('</p>', '\n').splitlines()
        paras = filter(None, [cleantext(p) for p in paras])
        out.write('# Location: %s\n' % url)
        out.write('# Genre: Blog\n')
        out.write('# Publication-Date: %s\n' % pubdate)
        for p in paras:
            out.write(p + '\n')


def find_tamurt_urls(crawler):
    urls = set()
    for author in ('akli2015', 'mack2015'):
        author_url = 'http://taq.tamurt.info/author/%s/' % author
        doc = crawler.fetch(author_url)
        assert doc.status == 200, (doc.status, url)
        html = doc.content.decode('utf-8')
        urls.update(extract_tamurt_urls(html))
        page_numbers = re.findall(author_url + r'page/(\d+)/', html)
        num_pages = max([1] + [int(n) for n in page_numbers])
        for page in range(2, num_pages + 1):
            page_url = author_url + 'page/%d/' % page
            page_doc = crawler.fetch(page_url)
            assert page_doc.status == 200, (page_doc.status, page_url)
            urls.update(extract_tamurt_urls(page_doc.content.decode('utf-8')))
    return urls


def extract_tamurt_urls(html):
    urls = set()
    for a in html.split('</article>')[:-1]:
        for url in re.findall(r'href="(https?://taq.tamurt.info/[^/"]+/)"', a):
            if not url.endswith('/feed/'):
                urls.add(url)
    return urls
