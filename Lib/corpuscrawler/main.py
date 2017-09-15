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
import argparse
import sys
from corpuscrawler import (
    crawl_ccp, crawl_gsw, crawl_gv, crawl_ha,
    crawl_mnw, crawl_my, crawl_rm, crawl_shn
)
from corpuscrawler.util import Crawler



def main():
    crawls = {
        'ccp': crawl_ccp.crawl,  # Chakma
        'gsw': crawl_gsw.crawl,  # Swiss German
        'gv': crawl_gv.crawl,    # Manx Gaelic
        'ha': crawl_ha.crawl,    # Hausa
        'mnw': crawl_mnw.crawl,  # Mon
        'my': crawl_my.crawl,    # Burmese
        'rm': crawl_rm.crawl,    # Romansh
    }
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--language', default='rm', choices=sorted(crawls.keys()),
        help='IETF BCP47 language code for the corpus to be crawled')
    parser.add_argument(
        '--output', default='./corpus',
        help='path to directory for writing output')
    parser.add_argument(
        '--cache', default='./cache-corpuscrawler',
        help='path to directory for caching fetched files')
    args = parser.parse_args()

    crawler = Crawler(language=args.language, output_dir=args.output,
                      cache_dir=args.cache)
    crawls[args.language](crawler)
    crawler.close()
