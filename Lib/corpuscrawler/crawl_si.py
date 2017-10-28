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

from corpuscrawler.util import crawl_bbc_news, crawl_udhr


def crawl(crawler):
    out = crawler.get_output(language='si')
    crawl_udhr(crawler, out, filename='udhr_sin.txt')
    crawl_bbc_news(crawler, out, urlprefix='/sinhala/')
