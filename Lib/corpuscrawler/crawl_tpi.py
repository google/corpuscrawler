# coding: utf-8
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
from corpuscrawler.util import cleantext, crawl_udhr, extract


def crawl(crawler):
    out = crawler.get_output(language='tpi')
    crawl_udhr(crawler, out, filename='udhr_tpi.txt')
    crawler.crawl_pngscriptures_org(out, language='tpi')
    crawler.crawl_abc_net_au(out, program_id='tok-pisin')
    crawl_wantokniuspepa_com(crawler, out)


def crawl_wantokniuspepa_com(crawler, out):
    sections = {'abc-pasifik-nius', 'bisnis-nius', 'helt-nius', 'komentri',
                'laip-stail', 'meri-nius', 'nius', 'wantok'}
    seeds = set()
    for section in sorted(sections):
        section_url = 'http://wantokniuspepa.com/index.php/%s' % section
        seeds.add(section_url)
        section_index = crawler.fetch(section_url)
        assert section_index.status == 200, (section_index.status, section_url)
        last_page = re.search(
            '"End" href=".+?start=(\d+)" class="pagenav"',
            section_index.content.decode('utf-8'))
        if last_page is not None:
            for page in range(1, int(last_page.group(1)) + 1):
                seeds.add('http://wantokniuspepa.com/index.php/%s?start=%d' %
                          (section, page))
    urls = set()
    for seed in sorted(seeds):
        doc = crawler.fetch(seed)
        assert doc.status == 200, (doc.status, url)
        content = doc.content.decode('utf-8')
        for u in re.findall(r'(/index\.php/[^"]+?)"', content):
            p = u.split('/')
            if len(p) > 3 and p[1] == 'index.php' and p[2] in sections:
                if re.search(r'/\d{4,}', u) is not None:
                    urls.add('http://wantokniuspepa.com' + u.split('?')[0])
    for url in sorted(urls):
        doc = crawler.fetch(url)
        assert doc.status == 200, (doc.status, url)
        content = doc.content.decode('utf-8')
        title = extract('<title>', '</title>', content)
        pubdate = re.search(r'<time datetime="([^T]+?)T([^"]+?)" '
                            'itemprop="datePublished">', content)
        pubdate = cleantext(pubdate.group(1)) if pubdate else None
        body = extract('<div itemprop="articleBody">', '<ul class="pager',
                       content)
        if not body:
            continue
        body = body.split('<div class="clearfix"')[0]
        text = body.replace('\n', ' ')
        text = text.replace(' ,', ',').replace('“ ', '“')
        text = re.sub(r'</(?:div|DIV|p|P|[hH][1-6]|table|TABLE)>', '\n', text)
        text = re.sub(r'<(?:br|BR)\s*/?>', '\n', text)
        paras = [cleantext(p) for p in [title] + text.splitlines()]
        paras = filter(None, paras)
        if not paras:
            continue
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        out.write('\n'.join(paras) + '\n')
