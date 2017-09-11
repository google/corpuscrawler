# -*- coding: utf-8 -*-
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
from corpuscrawler.util import \
    crawl_korero_html, crawl_udhr, replace_html_entities, striptags
from datetime import datetime


def crawl(crawler):
    out = crawler.get_output(language='gv')
    crawl_udhr(crawler, out, filename='udhr_glv.txt')
    crawl_korero_html(crawler, out, project='corpora-gv',
                      genre='News', filepath='gv_news_1821.html')
    for book in ('candide', 'coyrle_sodjey'):
        crawl_korero_html(crawler, out, project='corpora-gv',
                          genre='Literature', filepath='gv_%s.html' % book)
    crawl_manxradio(crawler, out)


def crawl_manxradio(crawler, out):
    urls = set()
    for i in range(1, 100):
        url = 'http://www.manxradio.com/news/manx-gaelic/archive/?page=%d' % i
        r = crawler.fetch(url)
        if r.status != 200 or r.content.find(b'No stories to show.') > 0:
            break
        for p in re.findall(r'<a href="/(news/manx-gaelic/[^"]+)"', r.content):
            url = 'http://www.manxradio.com/' + p
            if url.find('?') < 0:
                urls.add(url)
    for url in urls:
        r = crawler.fetch(url)
        assert r.status == 200, r.status
        html = r.content.decode('utf-8')
        pubdate = _extract_manxradio_timestamp(html)
        text = html.split('<p class="news-abstract">')
        if len(text) < 2:
            continue
        text = text[1].split('<STRONG>')[0].split('<strong>')[0]
        text = text.split('<p><span lang=""><b>')[0]
        text = text.replace('<p>', '\n').replace('</p>', '\n')
        text = text.replace('<P>', '\n').replace('</P>', '\n')
        text = striptags(replace_html_entities(text))
        text = text.replace(' - ', ' – ').replace("'", '’')
        if text.find('Listen to this audio') >= 0:
            continue
        paras = [' '.join(s.split()) for s in text.splitlines()]
        paras = [p for p in paras if p]
        if len(paras) == 0:
            continue
        out.write('# Location: %s\n' % url)
        out.write('# Genre: News\n')
        if pubdate:
            out.write('# Publication-Date: %s\n' % pubdate)
        for p in paras:
            out.write(p + '\n')



ENGLISH_MONTH_NAMES = {name: i + 1 for i, name in enumerate(
    'January February March April May June '
    'July August September October November December'.split())}


MANX_TIMEZONE_SHIFTS = [
    (datetime(2000, 3, 26, 1, 0), 0), (datetime(2000, 10, 29, 1, 0), 1),
    (datetime(2001, 3, 25, 1, 0), 0), (datetime(2001, 10, 28, 1, 0), 1),
    (datetime(2002, 3, 31, 1, 0), 0), (datetime(2002, 10, 27, 1, 0), 1),
    (datetime(2003, 3, 30, 1, 0), 0), (datetime(2003, 10, 26, 1, 0), 1),
    (datetime(2004, 3, 28, 1, 0), 0), (datetime(2004, 10, 31, 1, 0), 1),
    (datetime(2005, 3, 27, 1, 0), 0), (datetime(2005, 10, 30, 1, 0), 1),
    (datetime(2006, 3, 26, 1, 0), 0), (datetime(2006, 10, 29, 1, 0), 1),
    (datetime(2007, 3, 25, 1, 0), 0), (datetime(2007, 10, 28, 1, 0), 1),
    (datetime(2008, 3, 30, 1, 0), 0), (datetime(2008, 10, 26, 1, 0), 1),
    (datetime(2009, 3, 29, 1, 0), 0), (datetime(2009, 10, 25, 1, 0), 1),
    (datetime(2010, 3, 28, 1, 0), 0), (datetime(2010, 10, 31, 1, 0), 1),
    (datetime(2011, 3, 27, 1, 0), 0), (datetime(2011, 10, 30, 1, 0), 1),
    (datetime(2012, 3, 25, 1, 0), 0), (datetime(2012, 10, 28, 1, 0), 1),
    (datetime(2013, 3, 31, 1, 0), 0), (datetime(2013, 10, 27, 1, 0), 1),
    (datetime(2014, 3, 30, 1, 0), 0), (datetime(2014, 10, 26, 1, 0), 1),
    (datetime(2015, 3, 29, 1, 0), 0), (datetime(2015, 10, 25, 1, 0), 1),
    (datetime(2016, 3, 27, 1, 0), 0), (datetime(2016, 10, 30, 1, 0), 1),
    (datetime(2017, 3, 26, 1, 0), 0), (datetime(2017, 10, 29, 1, 0), 1),
    (datetime(2018, 3, 25, 1, 0), 0), (datetime(2018, 10, 28, 1, 0), 1),
    (datetime(2019, 3, 31, 1, 0), 0), (datetime(2019, 10, 27, 1, 0), 1),
    (datetime(2020, 3, 29, 1, 0), 0), (datetime(2020, 10, 25, 1, 0), 1),
    (datetime(2021, 3, 28, 1, 0), 0), (datetime(2021, 10, 31, 1, 0), 1),
    (datetime(2022, 3, 27, 1, 0), 0), (datetime(2022, 10, 30, 1, 0), 1),
    (datetime(2023, 3, 26, 1, 0), 0), (datetime(2023, 10, 29, 1, 0), 1),
    (datetime(2024, 3, 31, 1, 0), 0), (datetime(2024, 10, 27, 1, 0), 1),
    (datetime(2025, 3, 30, 1, 0), 0), (datetime(2025, 10, 26, 1, 0), 1),
    (datetime(2026, 3, 29, 1, 0), 0), (datetime(2026, 10, 25, 1, 0), 1),
    (datetime(2027, 3, 28, 1, 0), 0), (datetime(2027, 10, 31, 1, 0), 1),
    (datetime(2028, 3, 26, 1, 0), 0), (datetime(2028, 10, 29, 1, 0), 1),
    (datetime(2029, 3, 25, 1, 0), 0), (datetime(2029, 10, 28, 1, 0), 1),
    (datetime(2030, 3, 31, 1, 0), 0), (datetime(2030, 10, 27, 1, 0), 1),
    (datetime(2031, 3, 30, 1, 0), 0), (datetime(2031, 10, 26, 1, 0), 1),
    (datetime(2032, 3, 28, 1, 0), 0), (datetime(2032, 10, 31, 1, 0), 1),
    (datetime(2033, 3, 27, 1, 0), 0), (datetime(2033, 10, 30, 1, 0), 1),
    (datetime(2034, 3, 26, 1, 0), 0), (datetime(2034, 10, 29, 1, 0), 1),
    (datetime(2035, 3, 25, 1, 0), 0), (datetime(2035, 10, 28, 1, 0), 1),
    (datetime(2036, 3, 30, 1, 0), 0), (datetime(2036, 10, 26, 1, 0), 1),
    (datetime(2037, 3, 29, 1, 0), 0), (datetime(2037, 10, 25, 1, 0), 1),
]


def _extract_manxradio_timestamp(html):
    timestamp_match = re.search(
        r'<p class="news-timestamp">[^,]+?, (.+?)<', html)
    if timestamp_match is None:
        return None
    match = re.match(
        r'^([A-Za-z]+)\s+([0-9]+)(?:st|nd|rd|th),\s+([0-9]+)\s+'
        '([0-9]+):([0-9]+)(am|pm)', timestamp_match.group(1))
    month = ENGLISH_MONTH_NAMES[match.group(1)]
    _, day, year, hour, minute, ampm = match.groups()
    day, year, hour, minute = int(day), int(year), int(hour), int(minute)
    if hour == 12 and ampm == 'am':
        hour = 0
    elif hour == 12 and ampm == 'pm':
        hour = 12
    elif ampm == 'pm':
        hour = hour + 12
    timestamp_dt = datetime(year, month, day, hour, minute, 0)
    return '%04d-%02d-%02dT%02d:%02d:00+%02d:00' % (
        year, month, day, hour, minute, manx_tzoffset(timestamp_dt))


def manx_tzoffset(timestamp):
    for i, offset in MANX_TIMEZONE_SHIFTS:
        if timestamp < i:
            return offset
    return 0
