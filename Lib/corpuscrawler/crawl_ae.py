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
import unicodedata


def crawl(crawler):
    out = crawler.get_output(language='ae')
    out_latin = crawler.get_output(language='ae-Latn')
    crawl_titus_avestan(crawler, out, out_latin)


def crawl_titus_avestan(crawler, out, out_latin):
    for page in range(1, 249):
        url = ('http://titus.uni-frankfurt.de/texte/etcs/iran/airan/avesta/' +
               'avest%03d.htm' % page)
        doc = crawler.fetch(url)
        assert doc.status == 200, (doc.status, url)
        html = doc.content.decode('utf-8')
        for docid, doc in enumerate(html.split('<span id=subtitle>')[2:]):
            doc = doc.replace('<SUP>\u030A</SUP>', '\u030A')
            doc = doc.replace('<SUP>v</SUP>', '\u1D5B')
            title = re.search(r'<a id=subtitle[^>]*>(.+?)</a>', doc).group(1)
            out.write('# Location: %s#%d\n' % (url, docid + 1))
            out_latin.write('# Location: %s#%d\n' % (url, docid + 1))
            paras = [unicodedata.normalize('NFC', title.strip())]
            for text in doc.split('<span id=h4>')[1:]:
                words = []
                for word in re.findall(r'<[aA] [^>]+>(.+?)</[aA]>', text):
                    if ('<' not in word and ' ' not in word
                            and word != '&nbsp;'):  # and word != 'TITUS'):
                        word = unicodedata.normalize('NFC', word.strip())
                        words.append(word)
                words = filter(None, words)
                if words:
                    paras.append(' '.join(words))
            out.write(untransliterate('\n'.join(paras)) + '\n')
            latin = '\n'.join(paras) 
            latin = latin.replace('β', '\uA7B5')  # LATIN SMALL LETTER BETA
            latin = latin.replace('δ', 'ẟ')  # LATIN SMALL LETTER DELTA
            out_latin.write(latin + '\n')


_TRANSLIT = {
    ' ': ' ',
    '[': '[',
    ']': ']',
    'a': '\U00010B00',
    'ā': '\U00010B01',
    'å': '\U00010B02',
    'ā̊': '\U00010B03',
    'ą': '\U00010B04',
    'ą̇': '\U00010B05',
    'ə': '\U00010B06',
    'ə̄': '\U00010B07',
    'e': '\U00010B08',
    'ē': '\U00010B09',
    'o': '\U00010B0A',
    'ō': '\U00010B0B',
    'i': '\U00010B0C',
    'ī': '\U00010B0D',
    'u': '\U00010B0E',
    'ū': '\U00010B0F',
    'k': '\U00010B10',
    'x': '\U00010B11',
    'x́': '\U00010B12',
    'xᵛ': '\U00010B13',
    'g': '\U00010B14',
    'ġ': '\U00010B15',
    'γ': '\U00010B16',
    'c': '\U00010B17',
    'j': '\U00010B18',
    't': '\U00010B19',
    'ϑ': '\U00010B1A',
    'd': '\U00010B1B',
    'ẟ': '\U00010B1C',  # LATIN SMALL LETTER DELTA
    'δ': '\U00010B1C',  # GREEK SMALL LETTER DELTA
    't̰': '\U00010B1D',
    'p': '\U00010B1E',
    'f': '\U00010B1F',
    'b': '\U00010B20',
    '\uA7B5': '\U00010B21',  # LATIN SMALL LETTER BETA
    'β': '\U00010B21',  # GREEK SMALL LETTER BETA
    'ŋ': '\U00010B22',
    'ŋ́': '\U00010B23',
    'ŋᵛ': '\U00010B24',
    'n': '\U00010B25',
    'ń': '\U00010B26',
    'ṇ': '\U00010B27',
    'm': '\U00010B28',
    'm̨': '\U00010B29',
    'ẏ': '\U00010B2A',
    'y': '\U00010B2B',
    'ii': '\U00010B0C\U00010B0C',
    'v': '\U00010B2C',
    'uu': '\U00010B0E\U00010B0E',
    'r': '\U00010B2D',
    'l': '\U00010B2E',
    's': '\U00010B2F',
    'z': '\U00010B30',
    'š': '\U00010B31',
    'ž': '\U00010B32',
    'š́': '\U00010B33',
    'ṣ̌': '\U00010B34',
    'h': '\U00010B35',
    '.': '\U00010B39',  # AVESTAN ABBREVIATION MARK
}


# Sort by reverse length.
_TRANSLITS = sorted(_TRANSLIT.items(), key=lambda x:(-len(x[0]), x[0]))
for latin, _ in _TRANSLITS:
    assert latin == unicodedata.normalize('NFC', latin), latin


def untransliterate(s):
    s = s.lower()
    for latin, avestan in _TRANSLITS:
        s = s.replace(latin, avestan)
    return s
