# coding: utf-8
#
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
from corpuscrawler.util import cleantext, extract


def crawl(crawler):
    out = crawler.get_output(language='osa')
    _crawl_osagelanguagetools(crawler, out)


def _crawl_osagelanguagetools(crawler, out):
    for database in ('578', 'Approved+Words'):
        url = ('http://osagelanguagetools.appspot.com/words/getPhrases/'
               '?filterStatus=&databases=%s&sortCriteria=index' % database)
        html = crawler.fetch_content(url)
        out.write('# Location: %s\n' % url)
        out.write('# Genre: Dictionary\n')
        out.write('# Publication-Date: 2017\n')
        for row in re.findall(r'<tr.+?</tr>', html, flags=re.DOTALL):
            row = row.replace('\n', ' ')
            text = re.search('<td class="unicodeOsageText.+?>(.+?)</td>', row)
            if not text:
                continue
            text = text.group(1)
            text = text.replace('(Myrtle)', ' ').replace('(Mogri)', ' ')
            text = cleantext(text)
            if text.startswith('Teach'):
                continue
            out.write('%s\n' % text)
