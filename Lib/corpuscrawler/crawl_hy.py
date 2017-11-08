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
from datetime import date
import re
from corpuscrawler.util import cleantext, crawl_udhr, extract, daterange


def crawl(crawler):
    out = crawler.get_output(language='hy')
    crawl_udhr(crawler, out, filename='udhr_hye.txt')
    crawl_azg_am(crawler, out)


def crawl_azg_am(crawler, out):
    urls = set()
    for d in daterange(date(2001, 1, 9), date.today()):
        datestr = '%04d%02d%02d00' % (d.year, d.month, d.day)
        url = 'http://www.azg.am/AM/%s' % datestr
        doc = crawler.fetch(url)
        assert doc.status == 200, (doc.status, url)
        content = doc.content.decode('utf-8')
        articles = [a for a in re.findall(r'20\d{8}', content)
                    if not a.endswith('00')]
        for a in articles:
            urls.add('http://www.azg.am/wap/?nl=AM&id=%s&Base_PUB=0' % a)
        print(len(urls))
    for url in sorted(urls):
        pubdate = re.search(r'id=(20\d{6})', url).group(1)
        doc = crawler.fetch(url)
        assert doc.status == 200, (doc.status, url)
        content = doc.content.decode('utf-8')
        text = extract('<hr>', '<hr>', content)
        text = text.replace('\n', ' ')
        text = re.sub('</(p|h[1-9]|div)>', '\n', text)
        paras = filter(None, [cleantext(p) for p in text.splitlines()])
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            out.write('# Publication-Date: %s-%s-%s\n' %
                      (pubdate[:4], pubdate[4:6], pubdate[6:8]))
            out.write('\n'.join(paras) + '\n')
