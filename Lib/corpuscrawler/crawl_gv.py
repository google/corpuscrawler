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
from corpuscrawler.util import crawl_korero_html, crawl_udhr


def crawl(crawler):
    out = crawler.get_output(language='gv')
    crawl_udhr(crawler, out, filename='udhr_glv.txt')
    crawl_korero_html(crawler, out, project='corpora-gv',
                      genre='News', filepath='gv_news_1821.html')
    for book in ('candide', 'coyrle_sodjey'):
        crawl_korero_html(crawler, out, project='corpora-gv',
                          genre='Literature', filepath='gv_%s.html' % book)
