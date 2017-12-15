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
import argparse
import sys
from corpuscrawler import (
    crawl_aau, crawl_ace, crawl_ae, crawl_agd, crawl_am,
    crawl_az, crawl_ar,
    crawl_ba, crawl_be, crawl_bg,
    crawl_bm, crawl_bn, crawl_bo, crawl_bs,
    crawl_ccp, crawl_cs, crawl_cy,
    crawl_de, crawl_dz, crawl_el, crawl_es,
    crawl_fa, crawl_fi, crawl_fit, crawl_fo, crawl_fuv,
    crawl_ga, crawl_gd, crawl_gsw, crawl_gv, crawl_ha,
    crawl_haw,
    crawl_hi, crawl_hr, crawl_hy, crawl_id, crawl_ig,
    crawl_iu, crawl_ja,
    crawl_kab, crawl_kj, crawl_kk, crawl_km, crawl_ku, crawl_ky,
    crawl_la, crawl_lb,
    crawl_lo, crawl_mi, crawl_mnw, crawl_mk, crawl_mr,
    crawl_mt, crawl_my, crawl_nl, crawl_ny,
    crawl_osa, crawl_pa, crawl_pcm, crawl_pl, crawl_ps,
    crawl_rm,
    crawl_ro, crawl_ru, crawl_rw, crawl_sah, crawl_shn, crawl_si,
    crawl_sk, crawl_sl,
    crawl_sn, crawl_so, crawl_sq, crawl_sr, crawl_sv,
    crawl_sw, crawl_ta, crawl_ti, crawl_tpi,
    crawl_tt, crawl_tr,
    crawl_ug, crawl_uk, crawl_ur, crawl_vec, crawl_yo,
)
from corpuscrawler.util import Crawler


def main():
    crawls = {
        'aau': crawl_aau.crawl,  # Abau
        'ace': crawl_ace.crawl,  # Aceh/Acehnese
        'ae': crawl_ae.crawl,    # Avestan
        'agd': crawl_agd.crawl,  # Agarabi
        'am': crawl_am.crawl,    # Amharic
        'ar': crawl_ar.crawl,    # Modern Standard Arabic
        'az': crawl_az.crawl,    # Azerbaijani
        'ba': crawl_ba.crawl,    # Bashkir
        'be': crawl_be.crawl,    # Belarusian
        'bg': crawl_bg.crawl,    # Bulgarian
        'bm': crawl_bm.crawl,    # Bambara
        'bn': crawl_bn.crawl,    # Bangla
        'bo': crawl_bo.crawl,    # Tibetan
        'bs': crawl_bs.crawl,    # Bosnian
        'ccp': crawl_ccp.crawl,  # Chakma
        'cs': crawl_cs.crawl,    # Czech
        'cy': crawl_cy.crawl,    # Welsh
        'de': crawl_de.crawl,    # German
        'dz': crawl_dz.crawl,    # Dzongkha
        'el': crawl_el.crawl,    # Greek
        'es': crawl_es.crawl,    # Spanish
        'fa': crawl_fa.crawl,    # Persian
        'fi': crawl_fi.crawl,    # Finnish
        'fit': crawl_fit.crawl,  # Tornedalen Finnish
        'fo': crawl_fo.crawl,    # Faroese
        'fuv': crawl_fuv.crawl,  # Nigerian Fulfulde
        'gsw': crawl_gsw.crawl,  # Swiss German
        'ga': crawl_ga.crawl,    # Irish (Gaelic)
        'gd': crawl_gd.crawl,    # Scots Gaelic
        'gv': crawl_gv.crawl,    # Manx Gaelic
        'ha': crawl_ha.crawl,    # Hausa
        'haw': crawl_haw.crawl,  # Hawaiian
        'hi': crawl_hi.crawl,    # Hindi
        'hr': crawl_hr.crawl,    # Croatian
        'hy': crawl_hy.crawl,    # Armenian
        'id': crawl_id.crawl,    # Indonesian
        'ig': crawl_ig.crawl,    # Igbo
        'iu': crawl_iu.crawl,    # Inuktitut
        'ja': crawl_ja.crawl,    # Japanese
        'kab': crawl_kab.crawl,  # Kabyle
        'kj': crawl_kj.crawl,    # Kuanyama
        'kk': crawl_kk.crawl,    # Kazakh
        'km': crawl_km.crawl,    # Khmer
        'ku': crawl_ku.crawl,    # Kurdish
        'ky': crawl_ky.crawl,    # Kyrgyz
        'la': crawl_la.crawl,    # Latin
        'lb': crawl_lb.crawl,    # Luxembourgish
        'lo': crawl_lo.crawl,    # Lao
        'mi': crawl_mi.crawl,    # Maori
        'mk': crawl_mk.crawl,    # Macedonian
        'mnw': crawl_mnw.crawl,  # Mon
        'mr': crawl_mr.crawl,    # Marathi
        'mt': crawl_mt.crawl,    # Maltese
        'my': crawl_my.crawl,    # Burmese
        'nl': crawl_nl.crawl,    # Dutch
        'ny': crawl_ny.crawl,    # Nyanja
        'osa': crawl_osa.crawl,  # Osage
        'pa': crawl_pa.crawl,    # Punjabi
        'pcm': crawl_pcm.crawl,  # Nigerian Pidgin
        'pl': crawl_pl.crawl,    # Polish
        'ps': crawl_ps.crawl,    # Pashto
        'rm': crawl_rm.crawl,    # Romansh
        'ro': crawl_ro.crawl,    # Romanian
        'ru': crawl_ru.crawl,    # Russian
        'rw': crawl_rw.crawl,    # Kinyarwanda
        'sah': crawl_sah.crawl,  # Sakha
        'shn': crawl_shn.crawl,  # Shan
        'si': crawl_si.crawl,    # Sinhala
        'sk': crawl_sk.crawl,    # Slovak
        'sl': crawl_sl.crawl,    # Slovenian
        'sn': crawl_sn.crawl,    # Shona
        'so': crawl_so.crawl,    # Somali
        'sq': crawl_sq.crawl,    # Albanian
        'sr': crawl_sr.crawl,    # Serbian
        'sv': crawl_sv.crawl,    # Swedish
        'sw': crawl_sw.crawl,    # Swahili
        'ta': crawl_ta.crawl,    # Tamil
        'ti': crawl_ti.crawl,    # Tigrinya
        'tpi': crawl_tpi.crawl,  # Tok Pisin
        'tr': crawl_tr.crawl,    # Turkish
        'tt': crawl_tt.crawl,    # Tatar
        'ug': crawl_ug.crawl,    # Uyghur
        'uk': crawl_uk.crawl,    # Ukrainian
        'ur': crawl_ur.crawl,    # Urdu
        'vec': crawl_vec.crawl,  # Venetian
        'yo': crawl_yo.crawl,    # Yoruba
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
