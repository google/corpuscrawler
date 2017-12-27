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
    crawl_aai, crawl_aak, crawl_aau, crawl_aby, crawl_ace,
    crawl_ae, crawl_aey, crawl_agd, crawl_agg, crawl_agm,
    crawl_akh, crawl_am, crawl_amm, crawl_amp, crawl_aom,
    crawl_aon, crawl_ape, crawl_apr, crawl_apz, crawl_ar,
    crawl_aso, crawl_ata, crawl_auy, crawl_avt, crawl_awb,
    crawl_az, crawl_ba, crawl_bbb, crawl_bbr, crawl_bch,
    crawl_bdd, crawl_be, crawl_bef, crawl_bg, crawl_bhl,
    crawl_big, crawl_bjr, crawl_bm, crawl_bmh, crawl_bmu,
    crawl_bn, crawl_bnp, crawl_bo, crawl_boj, crawl_bon,
    crawl_bs, crawl_buk, crawl_byx, crawl_bzh, crawl_ccp,
    crawl_cjv, crawl_cs, crawl_cy, crawl_dad, crawl_dah,
    crawl_de, crawl_ded, crawl_dgz, crawl_dob, crawl_dww,
    crawl_dz, crawl_el, crawl_emi, crawl_enq, crawl_eri,
    crawl_es, crawl_et, crawl_fa, crawl_faa, crawl_fai, crawl_fi,
    crawl_fit, crawl_fo, crawl_for, crawl_fuv, crawl_ga,
    crawl_gah, crawl_gam, crawl_gaw, crawl_gd, crawl_gdn,
    crawl_gdr, crawl_gfk, crawl_ghs, crawl_gsw, crawl_gv,
    crawl_gvf, crawl_ha, crawl_haw, crawl_hi, crawl_hla,
    crawl_ho, crawl_hot, crawl_hr, crawl_hui, crawl_hy,
    crawl_ian, crawl_id, crawl_ig, crawl_imo, crawl_ino,
    crawl_iou, crawl_ipi, crawl_it, crawl_iu, crawl_iws, crawl_ja,
    crawl_jae, crawl_kab, crawl_kbm, crawl_kbq, crawl_kew,
    crawl_kgf, crawl_khz, crawl_kj, crawl_kjs, crawl_kk,
    crawl_km, crawl_kmg, crawl_kmo, crawl_kms, crawl_kmu,
    crawl_kpf, crawl_kpr, crawl_kpw, crawl_kpx, crawl_kqc,
    crawl_kqw, crawl_ksd, crawl_ksr, crawl_kto, crawl_ku,
    crawl_kud, crawl_kue, crawl_kup, crawl_kwj, crawl_ky,
    crawl_kyc, crawl_kyg, crawl_kze, crawl_la, crawl_lb,
    crawl_lcm, crawl_leu, crawl_lid, crawl_lo, crawl_lt,
    crawl_lv, crawl_mbh,
    crawl_mcq, crawl_med, crawl_mee, crawl_mek, crawl_meu,
    crawl_mhl, crawl_mi, crawl_mk, crawl_mlh, crawl_mlp,
    crawl_mmo, crawl_mmx, crawl_mna, crawl_mnw, crawl_mox,
    crawl_mpt, crawl_mpx, crawl_mr, crawl_msy, crawl_mt,
    crawl_mti, crawl_mux, crawl_mva, crawl_my,
    crawl_my_d0_zawgyi, crawl_myw,
    crawl_naf, crawl_nak, crawl_nas, crawl_nca, crawl_nho,
    crawl_nl, crawl_nop, crawl_nou, crawl_nsn, crawl_nvm,
    crawl_ny, crawl_okv, crawl_ong, crawl_opm, crawl_os,
    crawl_osa,
    crawl_pa, crawl_pcm, crawl_pl, crawl_ppo, crawl_ps,
    crawl_pt, crawl_pt_PT,
    crawl_ptp, crawl_pwg, crawl_rai, crawl_rm, crawl_ro,
    crawl_roo, crawl_rro, crawl_ru, crawl_rw, crawl_sah,
    crawl_sgz, crawl_shn, crawl_si, crawl_sim, crawl_sk,
    crawl_sl, crawl_sll, crawl_sn, crawl_snc, crawl_sny,
    crawl_so, crawl_soq, crawl_spl, crawl_sps, crawl_sq,
    crawl_sr, crawl_sr_Latn, crawl_ssd, crawl_ssg, crawl_ssx, crawl_sua,
    crawl_sue, crawl_sv, crawl_sw, crawl_swp, crawl_ta,
    crawl_taw, crawl_tbc, crawl_tbo, crawl_tgo, crawl_ti,
    crawl_tif, crawl_tim, crawl_tlf, crawl_tpi, crawl_tpz,
    crawl_tr, crawl_tt, crawl_tte, crawl_ubr, crawl_ug,
    crawl_uk, crawl_ur, crawl_usa, crawl_uvl, crawl_vec,
    crawl_vi,
    crawl_viv, crawl_waj, crawl_wer, crawl_wiu, crawl_wnc,
    crawl_wnu, crawl_wos, crawl_wrs, crawl_wsk, crawl_wuv,
    crawl_xla, crawl_xsi, crawl_yby, crawl_yle, crawl_yml,
    crawl_yo, crawl_yuj, crawl_yut, crawl_yuw, crawl_zia,
)
from corpuscrawler.util import Crawler


def main():
    crawls = {
        'aai': crawl_aai.crawl,  # Arifama-Miniafia
        'aak': crawl_aak.crawl,  # Ankave
        'aau': crawl_aau.crawl,  # Abau
        'aby': crawl_aby.crawl,  # Aneme Wake
        'ace': crawl_ace.crawl,  # Aceh/Acehnese
        'ae': crawl_ae.crawl,    # Avestan
        'aey': crawl_aey.crawl,  # Amele
        'agd': crawl_agd.crawl,  # Agarabi
        'agd': crawl_agd.crawl,  # Agarabi
        'agg': crawl_agg.crawl,  # Angor
        'agm': crawl_agm.crawl,  # Angaataha
        'akh': crawl_akh.crawl,  # Akha
        'am': crawl_am.crawl,    # Amharic
        'amm': crawl_amm.crawl,  # Ama (Papua New Guinea)
        'amp': crawl_amp.crawl,  # Alamblak
        'aom': crawl_aom.crawl,  # Ömie
        'aon': crawl_aon.crawl,  # Bumbita Arapesh
        'ape': crawl_ape.crawl,  # Bukiyip
        'apr': crawl_apr.crawl,  # Arop-Lokep
        'apz': crawl_apz.crawl,  # Safeyoka
        'ar': crawl_ar.crawl,    # Modern Standard Arabic
        'aso': crawl_aso.crawl,  # Dano
        'ata': crawl_ata.crawl,  # Pele-Ata
        'auy': crawl_auy.crawl,  # Awiyaana
        'avt': crawl_avt.crawl,  # Au
        'awb': crawl_awb.crawl,  # Awa (Papua New Guinea)
        'az': crawl_az.crawl,    # Azerbaijani
        'ba': crawl_ba.crawl,    # Bashkir
        'bbb': crawl_bbb.crawl,  # Barai
        'bbr': crawl_bbr.crawl,  # Girawa
        'bch': crawl_bch.crawl,  # Bariai
        'bdd': crawl_bdd.crawl,  # Bunama
        'be': crawl_be.crawl,    # Belarusian
        'bef': crawl_bef.crawl,  # Benabena
        'bg': crawl_bg.crawl,    # Bulgarian
        'bhl': crawl_bhl.crawl,  # Bimin
        'big': crawl_big.crawl,  # Biangai
        'bjr': crawl_bjr.crawl,  # Binumarien
        'bm': crawl_bm.crawl,    # Bambara
        'bmh': crawl_bmh.crawl,  # Kein
        'bmu': crawl_bmu.crawl,  # Somba-Siawari
        'bn': crawl_bn.crawl,    # Bangla
        'bnp': crawl_bnp.crawl,  # Bola
        'bo': crawl_bo.crawl,    # Tibetan
        'boj': crawl_boj.crawl,  # Anjam
        'bon': crawl_bon.crawl,  # Bine
        'bs': crawl_bs.crawl,    # Bosnian
        'buk': crawl_buk.crawl,  # Bugawac
        'byx': crawl_byx.crawl,  # Qaqet
        'bzh': crawl_bzh.crawl,  # Mapos Buang
        'ccp': crawl_ccp.crawl,  # Chakma
        'cjv': crawl_cjv.crawl,  # Chuave
        'cs': crawl_cs.crawl,    # Czech
        'cy': crawl_cy.crawl,    # Welsh
        'dad': crawl_dad.crawl,  # Marik
        'dah': crawl_dah.crawl,  # Gwahatike
        'de': crawl_de.crawl,    # German
        'ded': crawl_ded.crawl,  # Dedua
        'dgz': crawl_dgz.crawl,  # Daga
        'dob': crawl_dob.crawl,  # Dobu
        'dww': crawl_dww.crawl,  # Dawawa
        'dz': crawl_dz.crawl,    # Dzongkha
        'el': crawl_el.crawl,    # Greek
        'emi': crawl_emi.crawl,  # Mussau-Emira
        'enq': crawl_enq.crawl,  # Enga
        'eri': crawl_eri.crawl,  # Ogea
        'es': crawl_es.crawl,    # Spanish
        'et': crawl_et.crawl,    # Estonian
        'fa': crawl_fa.crawl,    # Persian
        'faa': crawl_faa.crawl,  # Fasu
        'fai': crawl_fai.crawl,  # Faiwol
        'fi': crawl_fi.crawl,    # Finnish
        'fit': crawl_fit.crawl,  # Tornedalen Finnish
        'fo': crawl_fo.crawl,    # Faroese
        'for': crawl_for.crawl,  # Fore
        'fuv': crawl_fuv.crawl,  # Nigerian Fulfulde
        'ga': crawl_ga.crawl,    # Irish (Gaelic)
        'gah': crawl_gah.crawl,  # Alekano
        'gam': crawl_gam.crawl,  # Kandawo
        'gaw': crawl_gaw.crawl,  # Nobonob
        'gd': crawl_gd.crawl,    # Scots Gaelic
        'gdn': crawl_gdn.crawl,  # Umanakaina
        'gdr': crawl_gdr.crawl,  # Wipi
        'gfk': crawl_gfk.crawl,  # Patpatar
        'ghs': crawl_ghs.crawl,  # Guhu-Samane
        'gsw': crawl_gsw.crawl,  # Swiss German
        'gv': crawl_gv.crawl,    # Manx Gaelic
        'gvf': crawl_gvf.crawl,  # Golin
        'ha': crawl_ha.crawl,    # Hausa
        'haw': crawl_haw.crawl,  # Hawaiian
        'hi': crawl_hi.crawl,    # Hindi
        'hla': crawl_hla.crawl,  # Halia
        'ho': crawl_ho.crawl,    # Hiri Motu
        'hot': crawl_hot.crawl,  # Hote
        'hr': crawl_hr.crawl,    # Croatian
        'hui': crawl_hui.crawl,  # Huli
        'hy': crawl_hy.crawl,    # Armenian
        'ian': crawl_ian.crawl,  # Iatmul
        'id': crawl_id.crawl,    # Indonesian
        'ig': crawl_ig.crawl,    # Igbo
        'imo': crawl_imo.crawl,  # Imbongu
        'ino': crawl_ino.crawl,  # Inoke-Yate
        'iou': crawl_iou.crawl,  # Tuma-Irumu
        'ipi': crawl_ipi.crawl,  # Ipili
        'it': crawl_it.crawl,    # Italian
        'iu': crawl_iu.crawl,    # Inuktitut
        'iws': crawl_iws.crawl,  # Sepik Iwam
        'ja': crawl_ja.crawl,    # Japanese
        'jae': crawl_jae.crawl,  # Yabem
        'kab': crawl_kab.crawl,  # Kabyle
        'kbm': crawl_kbm.crawl,  # Iwal
        'kbq': crawl_kbq.crawl,  # Kamano
        'kew': crawl_kew.crawl,  # West Kewa
        'kgf': crawl_kgf.crawl,  # Kube
        'khz': crawl_khz.crawl,  # Keapara
        'kj': crawl_kj.crawl,    # Kuanyama
        'kjs': crawl_kjs.crawl,  # East Kewa
        'kk': crawl_kk.crawl,    # Kazakh
        'km': crawl_km.crawl,    # Khmer
        'kmg': crawl_kmg.crawl,  # Kâte
        'kmo': crawl_kmo.crawl,  # Kwoma
        'kms': crawl_kms.crawl,  # Kamasau
        'kmu': crawl_kmu.crawl,  # Kanite
        'kpf': crawl_kpf.crawl,  # Komba
        'kpr': crawl_kpr.crawl,  # Korafe-Yegha
        'kpw': crawl_kpw.crawl,  # Kobon
        'kpx': crawl_kpx.crawl,  # Mountain Koiali
        'kqc': crawl_kqc.crawl,  # Doromu-Koki
        'kqw': crawl_kqw.crawl,  # Kandas
        'ksd': crawl_ksd.crawl,  # Kuanua
        'ksr': crawl_ksr.crawl,  # Borong
        'kto': crawl_kto.crawl,  # Kuot
        'ku': crawl_ku.crawl,    # Kurdish
        'kud': crawl_kud.crawl,  # ‘Auhelawa
        'kue': crawl_kue.crawl,  # Kuman (Papua New Guinea)
        'kup': crawl_kup.crawl,  # Kunimaipa
        'kwj': crawl_kwj.crawl,  # Kwanga
        'ky': crawl_ky.crawl,    # Kyrgyz
        'kyc': crawl_kyc.crawl,  # Kyaka
        'kyg': crawl_kyg.crawl,  # Keyagana
        'kze': crawl_kze.crawl,  # Kosena
        'la': crawl_la.crawl,    # Latin
        'lb': crawl_lb.crawl,    # Luxembourgish
        'lcm': crawl_lcm.crawl,  # Tungag
        'leu': crawl_leu.crawl,  # Kara (Papua New Guinea)
        'lid': crawl_lid.crawl,  # Nyindrou
        'lo': crawl_lo.crawl,    # Lao
        'lt': crawl_lt.crawl,    # Lithuanian
        'lv': crawl_lv.crawl,    # Latvian
        'mbh': crawl_mbh.crawl,  # Mangseng
        'mcq': crawl_mcq.crawl,  # Ese
        'med': crawl_med.crawl,  # Melpa
        'mee': crawl_mee.crawl,  # Mengen
        'mek': crawl_mek.crawl,  # Mekeo
        'meu': crawl_meu.crawl,  # Motu
        'mhl': crawl_mhl.crawl,  # Mauwake
        'mi': crawl_mi.crawl,    # Maori
        'mk': crawl_mk.crawl,    # Macedonian
        'mlh': crawl_mlh.crawl,  # Mape
        'mlp': crawl_mlp.crawl,  # Bargam
        'mmo': crawl_mmo.crawl,  # Mangga Buang
        'mmx': crawl_mmx.crawl,  # Madak
        'mna': crawl_mna.crawl,  # Mbula
        'mnw': crawl_mnw.crawl,  # Mon
        'mox': crawl_mox.crawl,  # Molima
        'mpt': crawl_mpt.crawl,  # Mian
        'mpx': crawl_mpx.crawl,  # Misima-Panaeati
        'mr': crawl_mr.crawl,    # Marathi
        'msy': crawl_msy.crawl,  # Aruamu
        'mt': crawl_mt.crawl,    # Maltese
        'mti': crawl_mti.crawl,  # Maiwa (Papua New Guinea)
        'mux': crawl_mux.crawl,  # Bo-Ung
        'mva': crawl_mva.crawl,  # Manam
        'my': crawl_my.crawl,    # Burmese
        'my-d0-zawgyi': crawl_my_d0_zawgyi.crawl,  # Burmese (Zawgyi)
        'myw': crawl_myw.crawl,  # Muyuw
        'naf': crawl_naf.crawl,  # Nabak
        'nak': crawl_nak.crawl,  # Nakanai
        'nas': crawl_nas.crawl,  # Naasioi
        'nca': crawl_nca.crawl,  # Iyo
        'nho': crawl_nho.crawl,  # Takuu
        'nl': crawl_nl.crawl,    # Dutch
        'nop': crawl_nop.crawl,  # Numanggang
        'nou': crawl_nou.crawl,  # Ewage-Notu
        'nsn': crawl_nsn.crawl,  # Nehan
        'nvm': crawl_nvm.crawl,  # Namiae
        'ny': crawl_ny.crawl,    # Nyanja
        'okv': crawl_okv.crawl,  # Orokaiva
        'ong': crawl_ong.crawl,  # Olo
        'opm': crawl_opm.crawl,  # Oksapmin
        'os': crawl_os.crawl,    # Ossetic
        'osa': crawl_osa.crawl,  # Osage
        'pa': crawl_pa.crawl,    # Punjabi
        'pcm': crawl_pcm.crawl,  # Nigerian Pidgin
        'pl': crawl_pl.crawl,    # Polish
        'ppo': crawl_ppo.crawl,  # Folopa
        'ps': crawl_ps.crawl,    # Pashto
        'pt': crawl_pt.crawl,    # Portuguese
        'pt-PT': crawl_pt_PT.crawl,      # Portuguese (Portugal)
        'ptp': crawl_ptp.crawl,  # Patep
        'pwg': crawl_pwg.crawl,  # Gapapaiwa
        'rai': crawl_rai.crawl,  # Ramoaaina
        'rm': crawl_rm.crawl,    # Romansh
        'ro': crawl_ro.crawl,    # Romanian
        'roo': crawl_roo.crawl,  # Rotokas
        'rro': crawl_rro.crawl,  # Waima
        'ru': crawl_ru.crawl,    # Russian
        'rw': crawl_rw.crawl,    # Kinyarwanda
        'sah': crawl_sah.crawl,  # Sakha
        'sgz': crawl_sgz.crawl,  # Sursurunga
        'shn': crawl_shn.crawl,  # Shan
        'si': crawl_si.crawl,    # Sinhala
        'sim': crawl_sim.crawl,  # Mende (Papua New Guinea)
        'sk': crawl_sk.crawl,    # Slovak
        'sl': crawl_sl.crawl,    # Slovenian
        'sll': crawl_sll.crawl,  # Salt-Yui
        'sn': crawl_sn.crawl,    # Shona
        'snc': crawl_snc.crawl,  # Sinaugoro
        'sny': crawl_sny.crawl,  # Saniyo-Hiyewe
        'so': crawl_so.crawl,    # Somali
        'soq': crawl_soq.crawl,  # Kanasi
        'spl': crawl_spl.crawl,  # Selepet
        'sps': crawl_sps.crawl,  # Saposa
        'sq': crawl_sq.crawl,    # Albanian
        'sr': crawl_sr.crawl,    # Serbian
        'sr-Latn': crawl_sr_Latn.crawl,  # Serbian (Latin)
        'ssd': crawl_ssd.crawl,  # Siroi
        'ssg': crawl_ssg.crawl,  # Seimat
        'ssx': crawl_ssx.crawl,  # Samberigi
        'sua': crawl_sua.crawl,  # Sulka
        'sue': crawl_sue.crawl,  # Suena
        'sv': crawl_sv.crawl,    # Swedish
        'sw': crawl_sw.crawl,    # Swahili
        'swp': crawl_swp.crawl,  # Suau
        'ta': crawl_ta.crawl,    # Tamil
        'taw': crawl_taw.crawl,  # Tai
        'tbc': crawl_tbc.crawl,  # Takia
        'tbo': crawl_tbo.crawl,  # Tawala
        'tgo': crawl_tgo.crawl,  # Sudest
        'ti': crawl_ti.crawl,    # Tigrinya
        'tif': crawl_tif.crawl,  # Tifal
        'tim': crawl_tim.crawl,  # Timbe
        'tlf': crawl_tlf.crawl,  # Telefol
        'tpi': crawl_tpi.crawl,  # Tok Pisin
        'tpz': crawl_tpz.crawl,  # Tinputz
        'tr': crawl_tr.crawl,    # Turkish
        'tt': crawl_tt.crawl,    # Tatar
        'tte': crawl_tte.crawl,  # Bwanabwana
        'ubr': crawl_ubr.crawl,  # Ubir
        'ug': crawl_ug.crawl,    # Uyghur
        'uk': crawl_uk.crawl,    # Ukrainian
        'ur': crawl_ur.crawl,    # Urdu
        'usa': crawl_usa.crawl,  # Usarufa
        'uvl': crawl_uvl.crawl,  # Lote
        'vec': crawl_vec.crawl,  # Venetian
        'vi': crawl_vi.crawl,    # Vietnamese
        'viv': crawl_viv.crawl,  # Iduna
        'waj': crawl_waj.crawl,  # Waffa
        'wer': crawl_wer.crawl,  # Weri
        'wiu': crawl_wiu.crawl,  # Wiru
        'wnc': crawl_wnc.crawl,  # Wantoat
        'wnu': crawl_wnu.crawl,  # Usan
        'wos': crawl_wos.crawl,  # Hanga Hundi
        'wrs': crawl_wrs.crawl,  # Waris
        'wsk': crawl_wsk.crawl,  # Waskia
        'wuv': crawl_wuv.crawl,  # Wuvulu-Aua
        'xla': crawl_xla.crawl,  # Kamula
        'xsi': crawl_xsi.crawl,  # Sio
        'yby': crawl_yby.crawl,  # Yaweyuha
        'yle': crawl_yle.crawl,  # Yele
        'yml': crawl_yml.crawl,  # Iamalele
        'yo': crawl_yo.crawl,    # Yoruba
        'yuj': crawl_yuj.crawl,  # Karkar-Yuri
        'yut': crawl_yut.crawl,  # Yopno
        'yuw': crawl_yuw.crawl,  # Yau (Morobe Province)
        'zia': crawl_zia.crawl,  # Zia
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
