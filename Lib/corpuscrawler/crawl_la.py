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
import json
import re
from corpuscrawler.util import crawl_udhr, cleantext, extract


def crawl(crawler):
    out = crawler.get_output(language='la')
    crawl_udhr(crawler, out, filename='udhr_lat.txt')
    crawl_areena_yle_fi(crawler, out)


def crawl_areena_yle_fi(crawler, out):
    for offset in range(0, 3000, 10):
        url = ('https://areena.yle.fi/api/programs/v1/items.json?'
               'series=1-1931339&type=program&availability=ondemand&'
               'order=episode.hash%3Adesc%2Cpublication.starttime%3Adesc%2C'
               'title.fi%3Aasc&app_id=89868a18&'
               'app_key=54bb4ea4d92854a2a45e98f961f0d7da&'
               'limit=10&offset=' + str(offset))
        doc = crawler.fetch(url)
        if doc.status != 200:
            continue
        content = json.loads(doc.content)
        data = content.get('data')
        if not data:
            return
        for item in data:
            title = item.get('itemTitle', {}).get('fi')
            description = item.get('description', {}).get('fi', '')
            paras = filter(None, [title] + description.splitlines())
            paras = filter(None, [cleantext(p) for p in paras])
            paras = [p for p in paras
                     if not (p.startswith('(') or
                             p.startswith('Nuntii Latini'))]
            publications = item.get('publicationEvent', [])
            pubdates = filter(None, [e.get('startTime') for e in publications])
            pubdate = min(pubdates) if pubdates else None
            if paras:
                out.write('# Location: %s\n' % item['@id'])
                out.write('# Genre: News\n')
                out.write('# Publication-Date: %s\n' % pubdate)
                out.write('\n'.join(paras) + '\n')
