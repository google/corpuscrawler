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
from corpuscrawler.util import crawl_udhr, cleantext, extract, replace_html_entities


def crawl(crawler):
    out = crawler.get_output(language='haw')
    crawl_udhr(crawler, out, filename='udhr_haw.txt')
    crawl_nupepa_org(crawler, out)


def crawl_nupepa_org(crawler, out):
    urls = set()
    for i in range(1, 104):
        url = ('http://nupepa.org/gsdl2.5/cgi-bin/nupepa?e=p-0nupepa--'
               '00-0-0--010---4-----text---0-1l--1en-Zz-1---20-about---'
               '0003-1-0000utfZz-8-00&a=d&cl=CL2.' + str(i))
        doc = crawler.fetch(url)
        assert doc.status == 200, url
        content = doc.content.decode('utf-8')
        for u in re.findall(r'href="(/gsdl2.5/cgi-bin/nupepa[^"]+)"', content):
            if u.endswith('gg=text'):
                urls.add('http://nupepa.org' + replace_html_entities(u))
    for url in sorted(urls):
        doc = crawler.fetch(url)
        assert doc.status == 200, url
        content = doc.content.decode('utf-8')
        if content.find('Document contains no data') >= 0:
            continue
        pubdate = re.search(r'tif_([0-9]{4})([01][0-9])([0123][0-9])\.tif"', content)
        pubdate = '%s-%s-%s' % (pubdate.group(1), pubdate.group(2), pubdate.group(3)) if pubdate else None
        paras = []
        while True:
            text = extract(
                "<p class=MsoNormal style='text-autospace:none'><span style='font-size:10.0pt'>",
                "</table>", content)
            if not text:
                break
            text = text.replace('\n', ' ').replace('<br>', '\n')
            text = replace_html_entities(text.replace('&nbsp;', ' '))
            paras.extend([cleantext(p) for p in text.splitlines()])
            nexturl = re.search(r'<a href="([^"]+)">next page', content)
            if nexturl is None:
                break
            nexturl = 'http://nupepa.org' + replace_html_entities(nexturl.group(1))
            doc = crawler.fetch(nexturl)
            assert doc.status == 200, (doc.status, nexturl)
            content = doc.content.decode('utf-8')
        text = '\n'.join(filter(None, paras))
        text = re.sub(
            r'DEATH OF MR\. DOUGLAS.+?has not been heard of since\.', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'IV\. "Their Majesties do further agree.+?by the parties\.', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'1 Oh, come, come away, from labor now reposing,.+?'
            r'Honolulu, Nov\. 25, 1861\. J\. L\. N\.\*', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'Died at sea, August 14.+?after a passage of about a month\.', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'On the 26th ult\. the Rev\. J.+?best wishes to you all\."', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'The subscriber avails himself.+?agreeable circumstances\.', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'NOTICE\. The publishing of.+for want of paper\.', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'ARRIVALS AT OAHU, SANDWICH ISLANDS,.+Sold here to the Government\.',
            '', text, flags=re.DOTALL)
        text = re.sub(
            r'NOTICE\. NOTICE is hereby given,.+by the subscriber\.', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'Articles made and agreed.+?upon the Sandwich Islands\.', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'MRS\. MARIA M\. DIBBLE\. Died at Lahainaluna.+?SHELDON DIBBLE\.',
            '', text, flags=re.DOTALL)
        text = re.sub(
            r'DEATH OF MRS\. BETSEY C\. LYONS.+?the son of man cometh\.\"', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'CARD\. The Missionary Company.+?April 20th 1837\.', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'DISTRESS OF THE WHALE SHIP GEORGE.+?who is now master of her\.', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'KNOW ALL MEN, That according.+?especially those above re-', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'cited, of the said Commissioners.+?and acknowledge the Protest', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'and withdrawal of our Deputy as our own.+?in the dominions of the Queen of',
            '', text, flags=re.DOTALL)
        text = re.sub(
            r'Taheite that I have received instructions.+?Commodore\. \[Official Copy\]',
            '', text, flags=re.DOTALL)
        text = re.sub(
            r'TO HIS MAJ\. KAMEHAMEHA.+?Naval Force in the E\. Indies\.', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'To the House of Representatives of the United States.+?'
            r'the arts of civilized life\.', '', text, flags=re.DOTALL)
        text = re.sub(
            r'It cannot but be in conformity.+?right to complain\.', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'The Committee on Foreign Affairs, to whom was.+?peace and love\.',
            '', text, flags=re.DOTALL)
        text = re.sub(
            r'WASHINGTON, June 25th, 1843.+?treat upon all occassions, the', '',
            text, flags=re.DOTALL)
        text = re.sub(
            r'native rulers of the Sandwich.+?P\. Upshur, &c\. &c\.', '',
            text, flags=re.DOTALL)
        if text.startswith('TERMS. One copy'):  # Article entirely in English.
            continue
        paras = filter(None, [cleantext(p) for p in text.splitlines()])
        if paras:
            out.write('# Location: %s\n' % url)
            out.write('# Genre: News\n')
            if pubdate:
                out.write('# Publication-Date: %s\n' % pubdate)
            out.write('\n'.join(paras) + '\n')
