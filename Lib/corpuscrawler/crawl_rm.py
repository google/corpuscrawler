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
from corpuscrawler.util import crawl_udhr, write_paragraphs

try:
    import xml.etree.cElementTree as etree
except ImportError:
    import xml.etree.ElementTree as etree


def crawl(crawler):
    crawl_rm_udhr(crawler)
    crawl_quotidiana(crawler)


def crawl_rm_udhr(crawler):
    for variant in 'puter rumgr surmiran sursilv sutsilv vallader'.split():
        out = crawler.get_output(language='rm-' + variant)
        crawl_udhr(crawler, out, filename='udhr_roh_%s.txt' % variant)


def crawl_quotidiana(crawler):
    for year in range(1997, 2009):
        url = ('https://raw.githubusercontent.com/ProSvizraRumantscha/'
               'corpora/master/la_quotidiana/rm_quotidiana_%d.xml' % year)
        root = etree.fromstring(crawler.fetch(url).content)
        for doc in root.findall('./DOC'):
            location = url + '#' + doc.attrib['id']
            lang = doc.attrib['{http://www.w3.org/XML/1998/namespace}lang']
            assert lang.split('-')[0] == 'rm', lang
            out = crawler.get_output(language=lang)
            out.write('# Location: %s\n' % location)
            out.write('# Genre: News\n')
            out.write('# Publication-Date: %s\n' % year)
            write_paragraphs(doc, out)
