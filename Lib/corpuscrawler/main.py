# coding: utf-8
#
# Copyright 2018 Google LLC
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
    crawl_aai, crawl_aak, crawl_aau, crawl_aaz, crawl_abt,
    crawl_aby, crawl_acd, crawl_ace, crawl_acf, crawl_ach,
    crawl_acn, crawl_acr, crawl_acu, crawl_ade, crawl_adh,
    crawl_adj, crawl_ae, crawl_aey, crawl_agd, crawl_agg,
    crawl_agm, crawl_agn, crawl_agr, crawl_ahk, crawl_aia,
    crawl_akb, crawl_ake, crawl_akh, crawl_akp, crawl_alj,
    crawl_alp, crawl_alt, crawl_alz, crawl_am, crawl_ame,
    crawl_amf, crawl_amk, crawl_amm, crawl_amn, crawl_amp,
    crawl_amr, crawl_amu, crawl_ann, crawl_anv, crawl_aoj,
    crawl_aom, crawl_aon, crawl_aoz, crawl_ape, crawl_apr,
    crawl_apz, crawl_ar, crawl_arl, crawl_asg, crawl_aso,
    crawl_ata, crawl_atb, crawl_atg, crawl_atq, crawl_auy,
    crawl_av, crawl_avn, crawl_avt, crawl_avu, crawl_awa,
    crawl_awb, crawl_ay, crawl_ayo, crawl_az, crawl_azg,
    crawl_azz, crawl_ba, crawl_ban, crawl_bao, crawl_bav,
    crawl_bba, crawl_bbb, crawl_bbo, crawl_bbr, crawl_bch,
    crawl_bcw, crawl_bdd, crawl_be, crawl_be_tarask, crawl_bef,
    crawl_bep, crawl_bex, crawl_bfd, crawl_bfo, crawl_bg,
    crawl_bgr, crawl_bgz, crawl_bhl, crawl_bhw, crawl_bi,
    crawl_bib, crawl_big, crawl_bik, crawl_bim, crawl_biv,
    crawl_bjr, crawl_bjv, crawl_bkl, crawl_bku, crawl_bkv,
    crawl_blh, crawl_blt, crawl_blt_Latn, crawl_blz, crawl_bm,
    crawl_bmh, crawl_bmq, crawl_bmr, crawl_bmu, crawl_bmv,
    crawl_bn, crawl_bnj, crawl_bnp, crawl_bo, crawl_boa,
    crawl_boj, crawl_bon, crawl_bov, crawl_box, crawl_bpr,
    crawl_bps, crawl_bqc, crawl_bqj, crawl_bqp, crawl_bru,
    crawl_bs, crawl_bsn, crawl_bss, crawl_btd, crawl_bts,
    crawl_btt, crawl_btx, crawl_bua, crawl_bud, crawl_buk,
    crawl_bus, crawl_bvc, crawl_bvz, crawl_bwq, crawl_bwu,
    crawl_byr, crawl_byx, crawl_bzh, crawl_bzi, crawl_bzj,
    crawl_ca_valencia,
    crawl_caa, crawl_cab, crawl_cac, crawl_cak, crawl_cap,
    crawl_car, crawl_cax, crawl_cbc, crawl_cbi, crawl_cbl,
    crawl_cbr, crawl_cbs, crawl_cbt, crawl_cbv, crawl_cce,
    crawl_ccp, crawl_cdf, crawl_ce, crawl_ceb, crawl_ceg,
    crawl_cfm, crawl_cgc, crawl_chj, crawl_chm, crawl_chr,
    crawl_chz, crawl_cjo, crawl_cjp, crawl_cjv, crawl_cko,
    crawl_cle, crawl_cme, crawl_cmr, crawl_cnh, crawl_cni,
    crawl_cnk, crawl_cnl, crawl_cnt, crawl_coe, crawl_cof,
    crawl_cok, crawl_con, crawl_cot, crawl_crh, crawl_cs,
    crawl_csk, crawl_cso, crawl_ctd_Latn, crawl_ctu, crawl_cub,
    crawl_cuc, crawl_cui, crawl_cuk, crawl_cul, crawl_cv,
    crawl_cwe, crawl_cwt, crawl_cy, crawl_cya, crawl_czt,
    crawl_da, crawl_daa, crawl_dad, crawl_dah, crawl_ddn,
    crawl_de, crawl_ded, crawl_des, crawl_dga, crawl_dgi,
    crawl_dgz, crawl_din, crawl_dip, crawl_djk, crawl_dln,
    crawl_dnw, crawl_dob, crawl_dop, crawl_dsh, crawl_dtb,
    crawl_dtp, crawl_dts, crawl_due, crawl_dug, crawl_duo,
    crawl_dwr, crawl_dww, crawl_dyi, crawl_dyo, crawl_dyu,
    crawl_dz, crawl_ee, crawl_eka, crawl_el, crawl_emi,
    crawl_emp, crawl_enb, crawl_enq, crawl_enx, crawl_eri,
    crawl_es, crawl_ese, crawl_et, crawl_eu, crawl_ewo,
    crawl_eza, crawl_fa, crawl_fa_AF, crawl_faa, crawl_fai,
    crawl_fal,
    crawl_far, crawl_fi, crawl_fil, crawl_fip, crawl_fit,
    crawl_fj, crawl_fo, crawl_fon, crawl_for, crawl_fr,
    crawl_fue, crawl_fuf, crawl_fuq, crawl_fuv, crawl_ga,
    crawl_gag, crawl_gah, crawl_gam, crawl_gaw, crawl_gbi,
    crawl_gd, crawl_gde, crawl_gdn, crawl_gdr, crawl_gej,
    crawl_gfk, crawl_ghs, crawl_gil, crawl_gkn, crawl_gmv_Latn,
    crawl_gn, crawl_gnd, crawl_gng, crawl_gnw, crawl_gof,
    crawl_gog, crawl_gor, crawl_gqr, crawl_grb, crawl_grt,
    crawl_gso, crawl_gsw, crawl_gu, crawl_gub, crawl_guc,
    crawl_gud, crawl_guh, crawl_gui, crawl_gum, crawl_gun,
    crawl_guo, crawl_guq, crawl_gur, crawl_gux, crawl_gv,
    crawl_gvc, crawl_gvf, crawl_gvl, crawl_gwr, crawl_gym,
    crawl_gyr, crawl_ha, crawl_hae, crawl_hag, crawl_haw,
    crawl_hay, crawl_heh, crawl_hi, crawl_hif, crawl_hig,
    crawl_hil, crawl_hla, crawl_hne, crawl_hnn, crawl_hns,
    crawl_ho, crawl_hot, crawl_hr, crawl_ht, crawl_hto,
    crawl_hu, crawl_hub, crawl_hui, crawl_hus, crawl_huu,
    crawl_huv, crawl_hvn, crawl_hy, crawl_ian, crawl_iba,
    crawl_icr, crawl_id, crawl_ifa, crawl_ifb, crawl_ife,
    crawl_ifk, crawl_ifu, crawl_ify, crawl_ig, crawl_ign,
    crawl_ik, crawl_ilo, crawl_imo, crawl_inb, crawl_ino,
    crawl_iou, crawl_ipi, crawl_iri, crawl_irk, crawl_iry,
    crawl_it, crawl_itv, crawl_iu, crawl_iws, crawl_izr,
    crawl_izz, crawl_ja, crawl_jac, crawl_jae, crawl_jam,
    crawl_jbu, crawl_jic, crawl_jiv, crawl_jmc, crawl_jun,
    crawl_jv, crawl_jvn, crawl_ka, crawl_kaa, crawl_kab,
    crawl_kab_Arab, crawl_kab_Tfng,
    crawl_kac, crawl_kao, crawl_kaq, crawl_kar,
    crawl_kbh, crawl_kbm,
    crawl_kbp, crawl_kbq, crawl_kbr, crawl_kcg, crawl_kdc,
    crawl_kdi, crawl_kdj, crawl_kdn, crawl_kek, crawl_ken,
    crawl_keo, crawl_ker, crawl_kew, crawl_kez, crawl_kgf,
    crawl_kgr, crawl_khz, crawl_kia, crawl_kij, crawl_kj,
    crawl_kjb, crawl_kje, crawl_kjh, crawl_kjs, crawl_kk,
    crawl_kki, crawl_kkj, crawl_kln, crawl_km, crawl_kma,
    crawl_kmg, crawl_kmo, crawl_kms, crawl_kmu, crawl_kn,
    crawl_kne, crawl_knf, crawl_knj, crawl_knk, crawl_kno,
    crawl_knv, crawl_kog, crawl_kpf, crawl_kpg, crawl_kpr,
    crawl_kpw, crawl_kpx, crawl_kpz, crawl_kqc, crawl_kqe,
    crawl_kqp, crawl_kqw, crawl_kqy, crawl_krc, crawl_kri,
    crawl_krj, crawl_kru, crawl_ksd, crawl_ksr, crawl_ktb,
    crawl_ktj, crawl_kto, crawl_ku, crawl_kub, crawl_kud,
    crawl_kue, crawl_kum, crawl_kup, crawl_kus, crawl_kv,
    crawl_kvn, crawl_kwf, crawl_kwi, crawl_kwj, crawl_kxc,
    crawl_kxm, crawl_ky, crawl_kyc, crawl_kyf, crawl_kyg,
    crawl_kyq, crawl_kyu, crawl_kyz, crawl_kze, crawl_kzf,
    crawl_kzj, crawl_la, crawl_laj, crawl_las, crawl_law,
    crawl_lb, crawl_lcm, crawl_lee, crawl_lef, crawl_lem,
    crawl_leu, crawl_lew, crawl_lex, crawl_lgg, crawl_lhu,
    crawl_lia, crawl_lid, crawl_lif, crawl_lip, crawl_lis,
    crawl_ljp, crawl_lln, crawl_lme, crawl_lmk, crawl_lnd,
    crawl_lo, crawl_lob, crawl_loe, crawl_lok, crawl_lon,
    crawl_lsi, crawl_lsm, crawl_lt, crawl_luc, crawl_lus,
    crawl_lv, crawl_lwo, crawl_maa, crawl_mad, crawl_mag,
    crawl_mai, crawl_maj, crawl_mak, crawl_mam, crawl_maw,
    crawl_maz, crawl_mbb, crawl_mbc, crawl_mbh, crawl_mbt,
    crawl_mca, crawl_mcb, crawl_mcd, crawl_mco, crawl_mcp,
    crawl_mcq, crawl_mcu, crawl_mda, crawl_mdy, crawl_med,
    crawl_mee, crawl_mej, crawl_mek, crawl_men, crawl_meq,
    crawl_meu, crawl_mfe, crawl_mfh, crawl_mfi, crawl_mfk,
    crawl_mfq, crawl_mfy, crawl_mfz, crawl_mg, crawl_mgd,
    crawl_mgh, crawl_mgo, crawl_mh, crawl_mhi, crawl_mhl,
    crawl_mhx, crawl_mhy, crawl_mi, crawl_mib, crawl_mif,
    crawl_mil, crawl_min, crawl_mio, crawl_miq, crawl_mir,
    crawl_mit, crawl_mk, crawl_mkl, crawl_ml, crawl_mlh,
    crawl_mlp, crawl_mmo, crawl_mmx,
    crawl_mn_Mong, crawl_mna, crawl_mnb,
    crawl_mnf, crawl_mnw, crawl_moa, crawl_mog, crawl_mop,
    crawl_mor, crawl_mox, crawl_mpg, crawl_mpm, crawl_mps,
    crawl_mpt, crawl_mpx, crawl_mqb, crawl_mqj, crawl_mqn,
    crawl_mr, crawl_mrw, crawl_ms, crawl_msm, crawl_msy,
    crawl_mt, crawl_mta, crawl_mti, crawl_mtj, crawl_mto,
    crawl_mtp, crawl_muh, crawl_mur, crawl_mux, crawl_muy,
    crawl_mva, crawl_mvp, crawl_mwv, crawl_mxb, crawl_mxt,
    crawl_my, crawl_my_t_d0_zawgyi, crawl_myb, crawl_myk, crawl_myv,
    crawl_myw, crawl_myx, crawl_myy, crawl_mza, crawl_mzi,
    crawl_mzk, crawl_mzm, crawl_naf, crawl_nak, crawl_nan,
    crawl_nan_Latn, crawl_nas, crawl_nca, crawl_nch, crawl_ncj,
    crawl_ncu, crawl_ndj, crawl_ndy, crawl_ndz, crawl_neb,
    crawl_new, crawl_nfr, crawl_ngp, crawl_nho, crawl_nhu,
    crawl_nhw, crawl_nhy, crawl_nia, crawl_nii, crawl_nij,
    crawl_nim, crawl_nin, crawl_nkf, crawl_nko, crawl_nl,
    crawl_nlc, crawl_nmz, crawl_nnb, crawl_nnq, crawl_nnw,
    crawl_noa, crawl_nog, crawl_nop, crawl_not, crawl_nou,
    crawl_npl, crawl_npy, crawl_nsn, crawl_nsu, crawl_ntm,
    crawl_ntp, crawl_ntr, crawl_nuj, crawl_nus, crawl_nvm,
    crawl_nwb, crawl_nwi, crawl_ny, crawl_nyf, crawl_nyn,
    crawl_nyo, crawl_nyy, crawl_nzi, crawl_obo, crawl_oc,
    crawl_oku,
    crawl_okv, crawl_old, crawl_ong, crawl_opm, crawl_or,
    crawl_os, crawl_osa, crawl_otd, crawl_ote, crawl_ozm,
    crawl_pa, crawl_pab, crawl_pad, crawl_pag, crawl_pah,
    crawl_pam, crawl_pau, crawl_pbc, crawl_pbi, crawl_pck,
    crawl_pcm, crawl_pez,
    crawl_pi_Mymr, crawl_pib, crawl_pir, crawl_pis,
    crawl_pjt, crawl_pkb, crawl_pl, crawl_plw, crawl_pmf,
    crawl_pny, crawl_poh, crawl_poi, crawl_poy, crawl_ppk,
    crawl_ppo, crawl_prf, crawl_prk, crawl_ps, crawl_pss,
    crawl_pt, crawl_pt_PT, crawl_ptp, crawl_ptu, crawl_pwg,
    crawl_pww, crawl_pxm, crawl_qu, crawl_qub, crawl_quc,
    crawl_quf, crawl_quh, crawl_qul, crawl_qup, crawl_quw,
    crawl_quy, crawl_qvc, crawl_qve, crawl_qvi, crawl_qvm,
    crawl_qvn, crawl_qvo, crawl_qvs, crawl_qvw, crawl_qvz,
    crawl_qwh, crawl_qxh, crawl_qxl, crawl_qxn, crawl_qxo,
    crawl_qxr, crawl_rai, crawl_raj, crawl_rav, crawl_rej,
    crawl_rim, crawl_rm, crawl_rmc, crawl_rmo, crawl_rn,
    crawl_rnl, crawl_ro, crawl_ro_MD, crawl_rom, crawl_roo,
    crawl_rro,
    crawl_ru, crawl_ruf, crawl_rug, crawl_rw, crawl_rwo,
    crawl_sab, crawl_sah, crawl_sas, crawl_sat,
    crawl_sba, crawl_sbl,
    crawl_sck, crawl_sda, crawl_seh, crawl_sey, crawl_sg,
    crawl_sgb, crawl_sgw, crawl_sgz, crawl_shk, crawl_shn,
    crawl_shp, crawl_si, crawl_sig, crawl_sil, crawl_sim,
    crawl_sja, crawl_sk, crawl_sl, crawl_sld, crawl_sll,
    crawl_sm, crawl_smt, crawl_sn, crawl_snc, crawl_snn,
    crawl_snp, crawl_snw, crawl_sny, crawl_so, crawl_soq,
    crawl_soy, crawl_spl, crawl_spp, crawl_sps, crawl_sq,
    crawl_sr, crawl_sr_Latn, crawl_sri, crawl_srm, crawl_srn,
    crawl_ssd, crawl_ssg, crawl_ssx, crawl_stn, crawl_su,
    crawl_sua, crawl_sue, crawl_sur, crawl_sus, crawl_suz,
    crawl_sv, crawl_sw, crawl_swp, crawl_sxn, crawl_ta,
    crawl_tab, crawl_taj, crawl_tap, crawl_taq, crawl_tav,
    crawl_taw, crawl_tbc, crawl_tbg, crawl_tbo, crawl_tby,
    crawl_tbz, crawl_tca, crawl_tcc, crawl_te, crawl_ted,
    crawl_tem, crawl_teo, crawl_ter, crawl_tfr, crawl_tgo,
    crawl_tgp, crawl_th, crawl_thk, crawl_ti, crawl_tif,
    crawl_tih, crawl_tik, crawl_tim, crawl_tk, crawl_tlb,
    crawl_tlf, crawl_tlj, crawl_tmc, crawl_tna, crawl_tnr,
    crawl_to, crawl_tob, crawl_toc, crawl_toh, crawl_top,
    crawl_tos, crawl_tpi, crawl_tpm, crawl_tpp, crawl_tpt,
    crawl_tpz, crawl_tqo, crawl_tr, crawl_trs, crawl_tsz,
    crawl_tt, crawl_ttc, crawl_tte, crawl_tue, crawl_tuf,
    crawl_twb, crawl_twu, crawl_txa, crawl_txu, crawl_tyv,
    crawl_tyz, crawl_tzh, crawl_tzj, crawl_ubr, crawl_ubu,
    crawl_udm, crawl_udu, crawl_ug, crawl_uk, crawl_ur,
    crawl_ura, crawl_urb, crawl_urk, crawl_ury, crawl_usa,
    crawl_usp, crawl_uvl, crawl_uz, crawl_vag, crawl_vec,
    crawl_vi, crawl_vid, crawl_viv, crawl_vmw, crawl_vun,
    crawl_vut, crawl_waj, crawl_wap, crawl_war, crawl_way,
    crawl_wer, crawl_wiu, crawl_wlx, crawl_wmw, crawl_wnc,
    crawl_wnu, crawl_wob, crawl_wos, crawl_wrs, crawl_wsk,
    crawl_wuv, crawl_wwa, crawl_xal, crawl_xav, crawl_xed,
    crawl_xla, crawl_xog, crawl_xrb, crawl_xsb, crawl_xsi,
    crawl_xsm, crawl_xsr, crawl_xsu, crawl_xtd, crawl_xtm,
    crawl_xuo, crawl_yaa, crawl_yad, crawl_yal, crawl_yam,
    crawl_yaz, crawl_yby, crawl_ycn, crawl_yle, crawl_yli,
    crawl_yml, crawl_yo, crawl_yon, crawl_yrb, crawl_yre,
    crawl_yss, crawl_yua, crawl_yue, crawl_yuj, crawl_yut,
    crawl_yuw, crawl_yva, crawl_zaa, crawl_zab, crawl_zac,
    crawl_zad, crawl_zae, crawl_zap, crawl_zar, crawl_zas,
    crawl_zaw, crawl_zca, crawl_zia, crawl_ziw, crawl_zlm,
    crawl_zne, crawl_zpc, crawl_zpi, crawl_zpq, crawl_zpt,
    crawl_zpz, crawl_zyp
)
from corpuscrawler.util import Crawler


def main():
    crawls = {
        'aai': crawl_aai.crawl,  # Arifama-Miniafia
        'aak': crawl_aak.crawl,  # Ankave
        'aau': crawl_aau.crawl,  # Abau
        'aaz': crawl_aaz.crawl,  # Amarasi
        'abt': crawl_abt.crawl,  # Ambulas
        'aby': crawl_aby.crawl,  # Aneme Wake
        'acd': crawl_acd.crawl,  # Gikyode
        'ace': crawl_ace.crawl,  # Aceh/Acehnese
        'acf': crawl_acf.crawl,  # Saint Lucian Creole French
        'ach': crawl_ach.crawl,  # Acoli
        'acn': crawl_acn.crawl,  # Achang
        'acr': crawl_acr.crawl,  # Achi
        'acu': crawl_acu.crawl,  # Achuar-Shiwiar
        'ade': crawl_ade.crawl,  # Adele
        'adh': crawl_adh.crawl,  # Adhola
        'adj': crawl_adj.crawl,  # Adioukrou
        'ae': crawl_ae.crawl,    # Avestan
        'aey': crawl_aey.crawl,  # Amele
        'agd': crawl_agd.crawl,  # Agarabi
        'agd': crawl_agd.crawl,  # Agarabi
        'agg': crawl_agg.crawl,  # Angor
        'agm': crawl_agm.crawl,  # Angaataha
        'agn': crawl_agn.crawl,  # Agutaynen
        'agr': crawl_agr.crawl,  # Aguaruna
        'ahk': crawl_ahk.crawl,  # Akha
        'aia': crawl_aia.crawl,  # Arosi
        'akb': crawl_akb.crawl,  # Batak Angkola
        'ake': crawl_ake.crawl,  # Akawaio
        'akh': crawl_akh.crawl,  # Akha
        'akp': crawl_akp.crawl,  # Siwu
        'alj': crawl_alj.crawl,  # Alangan
        'alp': crawl_alp.crawl,  # Alune
        'alt': crawl_alt.crawl,  # Southern Altai
        'alz': crawl_alz.crawl,  # Alur
        'am': crawl_am.crawl,    # Amharic
        'ame': crawl_ame.crawl,  # Yanesha'
        'amf': crawl_amf.crawl,  # Hamer-Banna
        'amk': crawl_amk.crawl,  # Ambai
        'amm': crawl_amm.crawl,  # Ama
        'amn': crawl_amn.crawl,  # Amanab
        'amp': crawl_amp.crawl,  # Alamblak
        'amr': crawl_amr.crawl,  # Amarakaeri
        'amu': crawl_amu.crawl,  # Guerrero Amuzgo
        'ann': crawl_ann.crawl,  # Obolo
        'anv': crawl_anv.crawl,  # Denya
        'aoj': crawl_aoj.crawl,  # Mufian
        'aom': crawl_aom.crawl,  # Ömie
        'aon': crawl_aon.crawl,  # Bumbita Arapesh
        'aoz': crawl_aoz.crawl,  # Uab Meto
        'ape': crawl_ape.crawl,  # Bukiyip
        'apr': crawl_apr.crawl,  # Arop-Lokep
        'apz': crawl_apz.crawl,  # Safeyoka
        'ar': crawl_ar.crawl,    # Modern Standard Arabic
        'arl': crawl_arl.crawl,  # Arabela
        'asg': crawl_asg.crawl,  # Cishingini
        'aso': crawl_aso.crawl,  # Dano
        'ata': crawl_ata.crawl,  # Pele-Ata
        'atb': crawl_atb.crawl,  # Zaiwa
        'atg': crawl_atg.crawl,  # Ivbie North-Okpela-Arhe
        'atq': crawl_atq.crawl,  # Aralle-Tabulahan
        'auy': crawl_auy.crawl,  # Awiyaana
        'av': crawl_av.crawl,    # Avaric
        'avn': crawl_avn.crawl,  # Avatime
        'avt': crawl_avt.crawl,  # Au
        'avu': crawl_avu.crawl,  # Avokaya
        'awa': crawl_awa.crawl,  # Awadhi
        'awb': crawl_awb.crawl,  # Awa
        'ay': crawl_ay.crawl,    # Aymara
        'ayo': crawl_ayo.crawl,  # Ayoreo
        'az': crawl_az.crawl,    # Azerbaijani
        'azg': crawl_azg.crawl,  # San Pedro Amuzgos Amuzgo
        'azz': crawl_azz.crawl,  # Highland Puebla Nahuatl
        'ba': crawl_ba.crawl,    # Bashkir
        'ban': crawl_ban.crawl,  # Balinese
        'bao': crawl_bao.crawl,  # Waimaha
        'bav': crawl_bav.crawl,  # Vengo
        'bba': crawl_bba.crawl,  # Baatonum
        'bbb': crawl_bbb.crawl,  # Barai
        'bbo': crawl_bbo.crawl,  # Northern Bobo Madaré
        'bbr': crawl_bbr.crawl,  # Girawa
        'bch': crawl_bch.crawl,  # Bariai
        'bcw': crawl_bcw.crawl,  # Bana
        'bdd': crawl_bdd.crawl,  # Bunama
        'be': crawl_be.crawl,    # Belarusian
        'be-tarask': crawl_be_tarask.crawl,    # Belarusian (Taraškievica)
        'bef': crawl_bef.crawl,  # Benabena
        'bep': crawl_bep.crawl,  # Besoa
        'bex': crawl_bex.crawl,  # Jur Modo
        'bfd': crawl_bfd.crawl,  # Bafut
        'bfo': crawl_bfo.crawl,  # Malba Birifor
        'bg': crawl_bg.crawl,    # Bulgarian
        'bgr': crawl_bgr.crawl,  # Bawm Chin
        'bgz': crawl_bgz.crawl,  # Banggai
        'bhl': crawl_bhl.crawl,  # Bimin
        'bhw': crawl_bhw.crawl,  # Biak
        'bi': crawl_bi.crawl,    # Bislama
        'bib': crawl_bib.crawl,  # Bissa
        'big': crawl_big.crawl,  # Biangai
        'bik': crawl_bik.crawl,  # Central Bikol
        'bim': crawl_bim.crawl,  # Bimoba
        'biv': crawl_biv.crawl,  # Southern Birifor
        'bjr': crawl_bjr.crawl,  # Binumarien
        'bjv': crawl_bjv.crawl,  # Bedjond
        'bkl': crawl_bkl.crawl,  # Berik
        'bku': crawl_bku.crawl,  # Buhid
        'bkv': crawl_bkv.crawl,  # Bekwarra
        'blh': crawl_blh.crawl,  # Kuwaa
        'blt': crawl_blt.crawl,  # Tai Dam
        'blt-Latn': crawl_blt_Latn.crawl,  # Tai Dam (Latin)
        'blz': crawl_blz.crawl,  # Balantak
        'bm': crawl_bm.crawl,    # Bambara
        'bmh': crawl_bmh.crawl,  # Kein
        'bmq': crawl_bmq.crawl,  # Bomu
        'bmr': crawl_bmr.crawl,  # Muinane
        'bmu': crawl_bmu.crawl,  # Somba-Siawari
        'bmv': crawl_bmv.crawl,  # Bum
        'bn': crawl_bn.crawl,    # Bangla
        'bnj': crawl_bnj.crawl,  # Eastern Tawbuid
        'bnp': crawl_bnp.crawl,  # Bola
        'bo': crawl_bo.crawl,    # Tibetan
        'boa': crawl_boa.crawl,  # Bora
        'boj': crawl_boj.crawl,  # Anjam
        'bon': crawl_bon.crawl,  # Bine
        'bov': crawl_bov.crawl,  # Tuwuli
        'box': crawl_box.crawl,  # Buamu
        'bpr': crawl_bpr.crawl,  # Koronadal Blaan
        'bps': crawl_bps.crawl,  # Sarangani Blaan
        'bqc': crawl_bqc.crawl,  # Boko
        'bqj': crawl_bqj.crawl,  # Bandial
        'bqp': crawl_bqp.crawl,  # Busa
        'bru': crawl_bru.crawl,  # Eastern Bru
        'bs': crawl_bs.crawl,    # Bosnian
        'bsn': crawl_bsn.crawl,  # Barasana-Eduria
        'bss': crawl_bss.crawl,  # Akoose
        'btd': crawl_btd.crawl,  # Batak Dairi
        'bts': crawl_bts.crawl,  # Batak Simalungun
        'btt': crawl_btt.crawl,  # Bete-Bendi
        'btx': crawl_btx.crawl,  # Batak Karo
        'bua': crawl_bua.crawl,  # Buriat
        'bud': crawl_bud.crawl,  # Ntcham
        'buk': crawl_buk.crawl,  # Bugawac
        'bus': crawl_bus.crawl,  # Bokobaru
        'bvc': crawl_bvc.crawl,  # Baelelea
        'bvz': crawl_bvz.crawl,  # Bauzi
        'bwq': crawl_bwq.crawl,  # Southern Bobo Madaré
        'bwu': crawl_bwu.crawl,  # Buli
        'byr': crawl_byr.crawl,  # Baruya
        'byx': crawl_byx.crawl,  # Qaqet
        'bzh': crawl_bzh.crawl,  # Mapos Buang
        'bzi': crawl_bzi.crawl,  # Bisu
        'bzj': crawl_bzj.crawl,  # Belize Kriol English
        'ca-valencia': crawl_ca_valencia.crawl,  # Valencian Catalan
        'caa': crawl_caa.crawl,  # Chortí
        'cab': crawl_cab.crawl,  # Garifuna
        'cac': crawl_cac.crawl,  # Chuj
        'cak': crawl_cak.crawl,  # Kaqchikel
        'cap': crawl_cap.crawl,  # Chipaya
        'car': crawl_car.crawl,  # Galibi Carib
        'cax': crawl_cax.crawl,  # Chiquitano
        'cbc': crawl_cbc.crawl,  # Carapana
        'cbi': crawl_cbi.crawl,  # Chachi
        'cbl': crawl_cbl.crawl,  # Bualkhaw Chin
        'cbr': crawl_cbr.crawl,  # Cashibo-Cacataibo
        'cbs': crawl_cbs.crawl,  # Cashinahua
        'cbt': crawl_cbt.crawl,  # Chayahuita
        'cbv': crawl_cbv.crawl,  # Cacua
        'cce': crawl_cce.crawl,  # Chopi
        'ccp': crawl_ccp.crawl,  # Chakma
        'cdf': crawl_cdf.crawl,  # Chiru
        'ce': crawl_ce.crawl,    # Chechen
        'ceb': crawl_ceb.crawl,  # Cebuano
        'ceg': crawl_ceg.crawl,  # Chamacoco
        'cfm': crawl_cfm.crawl,  # Falam Chin
        'cgc': crawl_cgc.crawl,  # Kagayanen
        'chj': crawl_chj.crawl,  # Ojitlán Chinantec
        'chm': crawl_chm.crawl,  # Mari
        'chr': crawl_chr.crawl,  # Cherokee
        'chz': crawl_chz.crawl,  # Ozumacín Chinantec
        'cjo': crawl_cjo.crawl,  # Ashéninka Pajonal
        'cjp': crawl_cjp.crawl,  # Cabécar
        'cjv': crawl_cjv.crawl,  # Chuave
        'cko': crawl_cko.crawl,  # Anufo
        'cle': crawl_cle.crawl,  # Lealao Chinantec
        'cme': crawl_cme.crawl,  # Cerma
        'cmr': crawl_cmr.crawl,  # Mro-Khimi Chin
        'cnh': crawl_cnh.crawl,  # Hakha Chin
        'cni': crawl_cni.crawl,  # Asháninka
        'cnk': crawl_cnk.crawl,  # Khumi Chin
        'cnl': crawl_cnl.crawl,  # Lalana Chinantec
        'cnt': crawl_cnt.crawl,  # Tepetotutla Chinantec
        'coe': crawl_coe.crawl,  # Koreguaje
        'cof': crawl_cof.crawl,  # Colorado
        'cok': crawl_cok.crawl,  # Santa Teresa Cora
        'con': crawl_con.crawl,  # Cofán
        'cot': crawl_cot.crawl,  # Caquinte
        'crh': crawl_crh.crawl,  # Crimean Tatar
        'cs': crawl_cs.crawl,    # Czech
        'csk': crawl_csk.crawl,  # Jola-Kasa
        'cso': crawl_cso.crawl,  # Sochiapam Chinantec
        'ctd-Latn': crawl_ctd_Latn.crawl,  # Tedim Chin (Latin)
        'ctu': crawl_ctu.crawl,  # Chol
        'cub': crawl_cub.crawl,  # Cubeo
        'cuc': crawl_cuc.crawl,  # Usila Chinantec
        'cui': crawl_cui.crawl,  # Cuiba
        'cuk': crawl_cuk.crawl,  # San Blas Kuna
        'cul': crawl_cul.crawl,  # Culina
        'cv': crawl_cv.crawl,    # Chuvash
        'cwe': crawl_cwe.crawl,  # Kwere
        'cwt': crawl_cwt.crawl,  # Kuwaataay
        'cy': crawl_cy.crawl,    # Welsh
        'cya': crawl_cya.crawl,  # Nopala Chatino
        'czt': crawl_czt.crawl,  # Zotung Chin
        'da': crawl_da.crawl,    # Danish
        'daa': crawl_daa.crawl,  # Dangaléat
        'dad': crawl_dad.crawl,  # Marik
        'dah': crawl_dah.crawl,  # Gwahatike
        'ddn': crawl_ddn.crawl,  # Dendi
        'de': crawl_de.crawl,    # German
        'ded': crawl_ded.crawl,  # Dedua
        'des': crawl_des.crawl,  # Desano
        'dga': crawl_dga.crawl,  # Southern Dagaare
        'dgi': crawl_dgi.crawl,  # Northern Dagara
        'dgz': crawl_dgz.crawl,  # Daga
        'din': crawl_din.crawl,  # Southwestern Dinka
        'dip': crawl_dip.crawl,  # Northeastern Dinka
        'djk': crawl_djk.crawl,  # Eastern Maroon Creole
        'dln': crawl_dln.crawl,  # Darlong
        'dnw': crawl_dnw.crawl,  # Western Dani
        'dob': crawl_dob.crawl,  # Dobu
        'dop': crawl_dop.crawl,  # Lukpa
        'dsh': crawl_dsh.crawl,  # Daasanach
        'dtb': crawl_dtb.crawl,  # Labuk-Kinabatangan Kadazan
        'dtp': crawl_dtp.crawl,  # Kadazan Dusun
        'dts': crawl_dts.crawl,  # Toro So Dogon
        'due': crawl_due.crawl,  # Umiray Dumaget Agta
        'dug': crawl_dug.crawl,  # Duruma
        'duo': crawl_duo.crawl,  # Dupaninan Agta
        'dwr': crawl_dwr.crawl,  # Dawro
        'dww': crawl_dww.crawl,  # Dawawa
        'dyi': crawl_dyi.crawl,  # Djimini Senoufo
        'dyo': crawl_dyo.crawl,  # Jola-Fonyi
        'dyu': crawl_dyu.crawl,  # Dyula
        'dz': crawl_dz.crawl,    # Dzongkha
        'ee': crawl_ee.crawl,    # Ewe
        'eka': crawl_eka.crawl,  # Ekajuk
        'el': crawl_el.crawl,    # Greek
        'emi': crawl_emi.crawl,  # Mussau-Emira
        'emp': crawl_emp.crawl,  # Northern Emberá
        'enb': crawl_enb.crawl,  # Markweeta
        'enq': crawl_enq.crawl,  # Enga
        'enx': crawl_enx.crawl,  # Enxet
        'eri': crawl_eri.crawl,  # Ogea
        'es': crawl_es.crawl,    # Spanish
        'ese': crawl_ese.crawl,  # Ese Ejja
        'et': crawl_et.crawl,    # Estonian
        'eu': crawl_eu.crawl,    # Basque
        'ewo': crawl_ewo.crawl,  # Ewondo
        'eza': crawl_eza.crawl,  # Ezaa
        'fa': crawl_fa.crawl,    # Persian
        'fa-AF': crawl_fa_AF.crawl,  # Dari
        'faa': crawl_faa.crawl,  # Fasu
        'fai': crawl_fai.crawl,  # Faiwol
        'fal': crawl_fal.crawl,  # South Fali
        'far': crawl_far.crawl,  # Fataleka
        'fi': crawl_fi.crawl,    # Finnish
        'fil': crawl_fil.crawl,  # Tagalog
        'fip': crawl_fip.crawl,  # Fipa
        'fit': crawl_fit.crawl,  # Tornedalen Finnish
        'fj': crawl_fj.crawl,    # Fijian
        'fo': crawl_fo.crawl,    # Faroese
        'fon': crawl_fon.crawl,  # Fon
        'for': crawl_for.crawl,  # Fore
        'fr': crawl_fr.crawl,    # French
        'fue': crawl_fue.crawl,  # Borgu Fulfulde
        'fuf': crawl_fuf.crawl,  # Pular
        'fuq': crawl_fuq.crawl,  # Central-Eastern Niger Fulfulde
        'fuv': crawl_fuv.crawl,  # Nigerian Fulfulde
        'ga': crawl_ga.crawl,    # Irish
        'gag': crawl_gag.crawl,  # Gagauz
        'gah': crawl_gah.crawl,  # Alekano
        'gam': crawl_gam.crawl,  # Kandawo
        'gaw': crawl_gaw.crawl,  # Nobonob
        'gbi': crawl_gbi.crawl,  # Galela
        'gd': crawl_gd.crawl,    # Scots Gaelic
        'gde': crawl_gde.crawl,  # Gude
        'gdn': crawl_gdn.crawl,  # Umanakaina
        'gdr': crawl_gdr.crawl,  # Wipi
        'gej': crawl_gej.crawl,  # Gen
        'gfk': crawl_gfk.crawl,  # Patpatar
        'ghs': crawl_ghs.crawl,  # Guhu-Samane
        'gil': crawl_gil.crawl,  # Gilbertese
        'gkn': crawl_gkn.crawl,  # Gokana
        'gmv-Latn': crawl_gmv_Latn.crawl,  # Gamo (Latin)
        'gn': crawl_gn.crawl,    # Guarani
        'gnd': crawl_gnd.crawl,  # Zulgo-Gemzek
        'gng': crawl_gng.crawl,  # Ngangam
        'gnw': crawl_gnw.crawl,  # Western Bolivian Guaraní
        'gof': crawl_gof.crawl,  # Gofa
        'gog': crawl_gog.crawl,  # Gogo
        'gor': crawl_gor.crawl,  # Gorontalo
        'gqr': crawl_gqr.crawl,  # Gor
        'grb': crawl_grb.crawl,  # Northern Grebo
        'grt': crawl_grt.crawl,  # Garo
        'gso': crawl_gso.crawl,  # Southwest Gbaya
        'gsw': crawl_gsw.crawl,  # Swiss German
        'gu': crawl_gu.crawl,    # Gujarati
        'gub': crawl_gub.crawl,  # Guajajára
        'guc': crawl_guc.crawl,  # Wayuu
        'gud': crawl_gud.crawl,  # Yocoboué Dida
        'guh': crawl_guh.crawl,  # Guahibo
        'gui': crawl_gui.crawl,  # Eastern Bolivian Guaraní
        'gum': crawl_gum.crawl,  # Guambiano
        'gun': crawl_gun.crawl,  # Mbyá Guaraní
        'guo': crawl_guo.crawl,  # Guayabero
        'guq': crawl_guq.crawl,  # Aché
        'gur': crawl_gur.crawl,  # Farefare
        'gux': crawl_gux.crawl,  # Gourmanchéma
        'gv': crawl_gv.crawl,    # Manx Gaelic
        'gvc': crawl_gvc.crawl,  # Guanano
        'gvf': crawl_gvf.crawl,  # Golin
        'gvl': crawl_gvl.crawl,  # Gulay
        'gwr': crawl_gwr.crawl,  # Gwere
        'gym': crawl_gym.crawl,  # Ngäbere
        'gyr': crawl_gyr.crawl,  # Guarayu
        'ha': crawl_ha.crawl,    # Hausa
        'hae': crawl_hae.crawl,  # Eastern Oromo
        'hag': crawl_hag.crawl,  # Hanga
        'haw': crawl_haw.crawl,  # Hawaiian
        'hay': crawl_hay.crawl,  # Haya
        'heh': crawl_heh.crawl,  # Hehe
        'hi': crawl_hi.crawl,    # Hindi
        'hif': crawl_hif.crawl,  # Fiji Hindi
        'hig': crawl_hig.crawl,  # Kamwe
        'hil': crawl_hil.crawl,  # Hiligaynon
        'hla': crawl_hla.crawl,  # Halia
        'hne': crawl_hne.crawl,  # Chhattisgarhi
        'hnn': crawl_hnn.crawl,  # Hanunoo
        'hns': crawl_hns.crawl,  # Caribbean Hindustani
        'ho': crawl_ho.crawl,    # Hiri Motu
        'hot': crawl_hot.crawl,  # Hote
        'hr': crawl_hr.crawl,    # Croatian
        'ht': crawl_ht.crawl,    # Haitian
        'hto': crawl_hto.crawl,  # Minica Huitoto
        'hu': crawl_hu.crawl,    # Hungarian
        'hub': crawl_hub.crawl,  # Huambisa
        'hui': crawl_hui.crawl,  # Huli
        'hus': crawl_hus.crawl,  # Huastec
        'huu': crawl_huu.crawl,  # Murui Huitoto
        'huv': crawl_huv.crawl,  # San Mateo Del Mar Huave
        'hvn': crawl_hvn.crawl,  # Sabu
        'hy': crawl_hy.crawl,    # Armenian
        'ian': crawl_ian.crawl,  # Iatmul
        'iba': crawl_iba.crawl,  # Iban
        'icr': crawl_icr.crawl,  # Islander Creole English
        'id': crawl_id.crawl,    # Indonesian
        'ifa': crawl_ifa.crawl,  # Amganad Ifugao
        'ifb': crawl_ifb.crawl,  # Batad Ifugao
        'ife': crawl_ife.crawl,  # Ifè
        'ifk': crawl_ifk.crawl,  # Tuwali Ifugao
        'ifu': crawl_ifu.crawl,  # Mayoyao Ifugao
        'ify': crawl_ify.crawl,  # Keley-I Kallahan
        'ig': crawl_ig.crawl,    # Igbo
        'ign': crawl_ign.crawl,  # Ignaciano
        'ik': crawl_ik.crawl,    # Inupiaq
        'ilo': crawl_ilo.crawl,  # Iloko
        'imo': crawl_imo.crawl,  # Imbongu
        'inb': crawl_inb.crawl,  # Inga
        'ino': crawl_ino.crawl,  # Inoke-Yate
        'iou': crawl_iou.crawl,  # Tuma-Irumu
        'ipi': crawl_ipi.crawl,  # Ipili
        'iri': crawl_iri.crawl,  # Irigwe
        'irk': crawl_irk.crawl,  # Iraqw
        'iry': crawl_iry.crawl,  # Iraya
        'it': crawl_it.crawl,    # Italian
        'itv': crawl_itv.crawl,  # Itawit
        'iu': crawl_iu.crawl,    # Inuktitut
        'iws': crawl_iws.crawl,  # Sepik Iwam
        'izr': crawl_izr.crawl,  # Izere
        'izz': crawl_izz.crawl,  # Izii
        'ja': crawl_ja.crawl,    # Japanese
        'jac': crawl_jac.crawl,  # Popti'
        'jae': crawl_jae.crawl,  # Yabem
        'jam': crawl_jam.crawl,  # Jamaican Creole English
        'jbu': crawl_jbu.crawl,  # Jukun Takum
        'jic': crawl_jic.crawl,  # Tol
        'jiv': crawl_jiv.crawl,  # Shuar
        'jmc': crawl_jmc.crawl,  # Machame
        'jun': crawl_jun.crawl,  # Juang
        'jv': crawl_jv.crawl,    # Javanese
        'jvn': crawl_jvn.crawl,  # Caribbean Javanese
        'ka': crawl_ka.crawl,    # Georgian
        'kaa': crawl_kaa.crawl,  # Kara-Kalpak
        'kab': crawl_kab.crawl,  # Kabyle
        'kab-Arab': crawl_kab_Arab.crawl,  # Kabyle (Arabic)
        'kab-Tfng': crawl_kab_Tfng.crawl,  # Kabyle (Tifinagh)
        'kac': crawl_kac.crawl,  # Kachin
        'kao': crawl_kao.crawl,  # Xaasongaxango
        'kaq': crawl_kaq.crawl,  # Capanahua
        'kar': crawl_kar.crawl,  # Karen (language family)
        'kbh': crawl_kbh.crawl,  # Camsá
        'kbm': crawl_kbm.crawl,  # Iwal
        'kbp': crawl_kbp.crawl,  # Kabiyè
        'kbq': crawl_kbq.crawl,  # Kamano
        'kbr': crawl_kbr.crawl,  # Kafa
        'kcg': crawl_kcg.crawl,  # Tyap
        'kdc': crawl_kdc.crawl,  # Kutu
        'kdi': crawl_kdi.crawl,  # Kumam
        'kdj': crawl_kdj.crawl,  # Karamojong
        'kdn': crawl_kdn.crawl,  # Kunda
        'kek': crawl_kek.crawl,  # Kekchí
        'ken': crawl_ken.crawl,  # Kenyang
        'keo': crawl_keo.crawl,  # Kakwa
        'ker': crawl_ker.crawl,  # Kera
        'kew': crawl_kew.crawl,  # West Kewa
        'kez': crawl_kez.crawl,  # Kukele
        'kgf': crawl_kgf.crawl,  # Kube
        'kgr': crawl_kgr.crawl,  # Abun
        'khz': crawl_khz.crawl,  # Keapara
        'kia': crawl_kia.crawl,  # Kim
        'kij': crawl_kij.crawl,  # Kilivila
        'kj': crawl_kj.crawl,    # Kuanyama
        'kjb': crawl_kjb.crawl,  # Q'anjob'al
        'kje': crawl_kje.crawl,  # Kisar
        'kjh': crawl_kjh.crawl,  # Khakas
        'kjs': crawl_kjs.crawl,  # East Kewa
        'kk': crawl_kk.crawl,    # Kazakh
        'kki': crawl_kki.crawl,  # Kagulu
        'kkj': crawl_kkj.crawl,  # Kako
        'kln': crawl_kln.crawl,  # Kalenjin
        'km': crawl_km.crawl,    # Khmer
        'kma': crawl_kma.crawl,  # Konni
        'kmg': crawl_kmg.crawl,  # Kâte
        'kmo': crawl_kmo.crawl,  # Kwoma
        'kms': crawl_kms.crawl,  # Kamasau
        'kmu': crawl_kmu.crawl,  # Kanite
        'kn': crawl_kn.crawl,    # Kannada
        'kne': crawl_kne.crawl,  # Kankanaey
        'knf': crawl_knf.crawl,  # Mankanya
        'knj': crawl_knj.crawl,  # Western Kanjobal
        'knk': crawl_knk.crawl,  # Kuranko
        'kno': crawl_kno.crawl,  # Kono
        'knv': crawl_knv.crawl,  # Tabo
        'kog': crawl_kog.crawl,  # Cogui
        'kpf': crawl_kpf.crawl,  # Komba
        'kpg': crawl_kpg.crawl,  # Kapingamarangi
        'kpr': crawl_kpr.crawl,  # Korafe-Yegha
        'kpw': crawl_kpw.crawl,  # Kobon
        'kpx': crawl_kpx.crawl,  # Mountain Koiali
        'kpz': crawl_kpz.crawl,  # Kupsabiny
        'kqc': crawl_kqc.crawl,  # Doromu-Koki
        'kqe': crawl_kqe.crawl,  # Kalagan
        'kqp': crawl_kqp.crawl,  # Kimré
        'kqw': crawl_kqw.crawl,  # Kandas
        'kqy': crawl_kqy.crawl,  # Koorete
        'krc': crawl_krc.crawl,  # Karachay-Balkar
        'kri': crawl_kri.crawl,  # Krio
        'krj': crawl_krj.crawl,  # Kinaray-A
        'kru': crawl_kru.crawl,  # Kurukh
        'ksd': crawl_ksd.crawl,  # Kuanua
        'ksr': crawl_ksr.crawl,  # Borong
        'ktb': crawl_ktb.crawl,  # Kambaata
        'ktj': crawl_ktj.crawl,  # Plapo Krumen
        'kto': crawl_kto.crawl,  # Kuot
        'ku': crawl_ku.crawl,    # Kurdish
        'kub': crawl_kub.crawl,  # Kutep
        'kud': crawl_kud.crawl,  # ‘Auhelawa
        'kue': crawl_kue.crawl,  # Kuman
        'kum': crawl_kum.crawl,  # Kumyk
        'kup': crawl_kup.crawl,  # Kunimaipa
        'kus': crawl_kus.crawl,  # Kusaal
        'kv': crawl_kv.crawl,    # Komi
        'kvn': crawl_kvn.crawl,  # Border Kuna
        'kwf': crawl_kwf.crawl,  # Kwara'ae
        'kwi': crawl_kwi.crawl,  # Awa-Cuaiquer
        'kwj': crawl_kwj.crawl,  # Kwanga
        'kxc': crawl_kxc.crawl,  # Konso
        'kxm': crawl_kxm.crawl,  # Northern Khmer
        'ky': crawl_ky.crawl,    # Kyrgyz
        'kyc': crawl_kyc.crawl,  # Kyaka
        'kyf': crawl_kyf.crawl,  # Kouya
        'kyg': crawl_kyg.crawl,  # Keyagana
        'kyq': crawl_kyq.crawl,  # Kenga
        'kyu': crawl_kyu.crawl,  # Western Kayah
        'kyz': crawl_kyz.crawl,  # Kayabí
        'kze': crawl_kze.crawl,  # Kosena
        'kzf': crawl_kzf.crawl,  # Da'a Kaili
        'kzj': crawl_kzj.crawl,  # Coastal Kadazan
        'la': crawl_la.crawl,    # Latin
        'laj': crawl_laj.crawl,  # Lango
        'las': crawl_las.crawl,  # Lama
        'law': crawl_law.crawl,  # Lauje
        'lb': crawl_lb.crawl,    # Luxembourgish
        'lcm': crawl_lcm.crawl,  # Tungag
        'lee': crawl_lee.crawl,  # Lyélé
        'lef': crawl_lef.crawl,  # Lelemi
        'lem': crawl_lem.crawl,  # Nomaande
        'leu': crawl_leu.crawl,  # Kara
        'lew': crawl_lew.crawl,  # Ledo Kaili
        'lex': crawl_lex.crawl,  # Luang
        'lgg': crawl_lgg.crawl,  # Lugbara
        'lhu': crawl_lhu.crawl,  # Lahu
        'lia': crawl_lia.crawl,  # West-Central Limba
        'lid': crawl_lid.crawl,  # Nyindrou
        'lif': crawl_lif.crawl,  # Limbu
        'lip': crawl_lip.crawl,  # Sekpele
        'lis': crawl_lis.crawl,  # Lisu
        'ljp': crawl_ljp.crawl,  # Lampung Api
        'lln': crawl_lln.crawl,  # Lele
        'lme': crawl_lme.crawl,  # Pévé
        'lmk': crawl_lmk.crawl,  # Lamkang
        'lnd': crawl_lnd.crawl,  # Lundayeh
        'lo': crawl_lo.crawl,    # Lao
        'lob': crawl_lob.crawl,  # Lobi
        'loe': crawl_loe.crawl,  # Saluan
        'lok': crawl_lok.crawl,  # Loko
        'lon': crawl_lon.crawl,  # Malawi Lomwe
        'lsi': crawl_lsi.crawl,  # Lashi
        'lsm': crawl_lsm.crawl,  # Saamia
        'lt': crawl_lt.crawl,    # Lithuanian
        'luc': crawl_luc.crawl,  # Aringa
        'lus': crawl_lus.crawl,  # Lushai
        'lv': crawl_lv.crawl,    # Latvian
        'lwo': crawl_lwo.crawl,  # Luwo
        'maa': crawl_maa.crawl,  # San Jerónimo Tecóatl Mazatec
        'mad': crawl_mad.crawl,  # Madurese
        'mag': crawl_mag.crawl,  # Magahi
        'mai': crawl_mai.crawl,  # Maithili
        'maj': crawl_maj.crawl,  # Jalapa De Díaz Mazatec
        'mak': crawl_mak.crawl,  # Makasar
        'mam': crawl_mam.crawl,  # Mam
        'maw': crawl_maw.crawl,  # Mampruli
        'maz': crawl_maz.crawl,  # Central Mazahua
        'mbb': crawl_mbb.crawl,  # Western Bukidnon Manobo
        'mbc': crawl_mbc.crawl,  # Macushi
        'mbh': crawl_mbh.crawl,  # Mangseng
        'mbt': crawl_mbt.crawl,  # Matigsalug Manobo
        'mca': crawl_mca.crawl,  # Maca
        'mcb': crawl_mcb.crawl,  # Machiguenga
        'mcd': crawl_mcd.crawl,  # Sharanahua
        'mco': crawl_mco.crawl,  # Coatlán Mixe
        'mcp': crawl_mcp.crawl,  # Makaa
        'mcq': crawl_mcq.crawl,  # Ese
        'mcu': crawl_mcu.crawl,  # Cameroon Mambila
        'mda': crawl_mda.crawl,  # Mada
        'mdy': crawl_mdy.crawl,  # Male
        'med': crawl_med.crawl,  # Melpa
        'mee': crawl_mee.crawl,  # Mengen
        'mej': crawl_mej.crawl,  # Meyah
        'mek': crawl_mek.crawl,  # Mekeo
        'men': crawl_men.crawl,  # Mende
        'meq': crawl_meq.crawl,  # Merey
        'meu': crawl_meu.crawl,  # Motu
        'mfe': crawl_mfe.crawl,  # Morisyen
        'mfh': crawl_mfh.crawl,  # Matal
        'mfi': crawl_mfi.crawl,  # Wandala
        'mfk': crawl_mfk.crawl,  # North Mofu
        'mfq': crawl_mfq.crawl,  # Moba
        'mfy': crawl_mfy.crawl,  # Mayo
        'mfz': crawl_mfz.crawl,  # Mabaan
        'mg': crawl_mg.crawl,    # Malagasy
        'mgd': crawl_mgd.crawl,  # Moru
        'mgh': crawl_mgh.crawl,  # Makhuwa-Meetto
        'mgo': crawl_mgo.crawl,  # Meta'
        'mh': crawl_mh.crawl,    # Marshallese
        'mhi': crawl_mhi.crawl,  # Ma'di
        'mhl': crawl_mhl.crawl,  # Mauwake
        'mhx': crawl_mhx.crawl,  # Maru
        'mhy': crawl_mhy.crawl,  # Ma'anyan
        'mi': crawl_mi.crawl,    # Maori
        'mib': crawl_mib.crawl,  # Atatláhuca Mixtec
        'mif': crawl_mif.crawl,  # Mofu-Gudur
        'mil': crawl_mil.crawl,  # Peñoles Mixtec
        'min': crawl_min.crawl,  # Minangkabau
        'mio': crawl_mio.crawl,  # Pinotepa Nacional Mixtec
        'miq': crawl_miq.crawl,  # Mískito
        'mir': crawl_mir.crawl,  # Isthmus Mixé
        'mit': crawl_mit.crawl,  # Southern Puebla Mixtec
        'mk': crawl_mk.crawl,    # Macedonian
        'mkl': crawl_mkl.crawl,  # Mokole
        'ml': crawl_ml.crawl,    # Malayalam
        'mlh': crawl_mlh.crawl,  # Mape
        'mlp': crawl_mlp.crawl,  # Bargam
        'mmo': crawl_mmo.crawl,  # Mangga Buang
        'mmx': crawl_mmx.crawl,  # Madak
        'mn-Mong': crawl_mn_Mong.crawl,  # Mongolian (Mongolian script)
        'mna': crawl_mna.crawl,  # Mbula
        'mnb': crawl_mnb.crawl,  # Muna
        'mnf': crawl_mnf.crawl,  # Mundani
        'mnw': crawl_mnw.crawl,  # Mon
        'moa': crawl_moa.crawl,  # Mwan
        'mog': crawl_mog.crawl,  # Mongondow
        'mop': crawl_mop.crawl,  # Mopán Maya
        'mor': crawl_mor.crawl,  # Moro
        'mox': crawl_mox.crawl,  # Molima
        'mpg': crawl_mpg.crawl,  # Marba
        'mpm': crawl_mpm.crawl,  # Yosondúa Mixtec
        'mps': crawl_mps.crawl,  # Dadibi
        'mpt': crawl_mpt.crawl,  # Mian
        'mpx': crawl_mpx.crawl,  # Misima-Panaeati
        'mqb': crawl_mqb.crawl,  # Mbuko
        'mqj': crawl_mqj.crawl,  # Mamasa
        'mqn': crawl_mqn.crawl,  # Moronene
        'mr': crawl_mr.crawl,    # Marathi
        'mrw': crawl_mrw.crawl,  # Maranao
        'ms': crawl_ms.crawl,    # Malay
        'msm': crawl_msm.crawl,  # Agusan Manobo
        'msy': crawl_msy.crawl,  # Aruamu
        'mt': crawl_mt.crawl,    # Maltese
        'mta': crawl_mta.crawl,  # Cotabato Manobo
        'mti': crawl_mti.crawl,  # Maiwa
        'mtj': crawl_mtj.crawl,  # Moskona
        'mto': crawl_mto.crawl,  # Totontepec Mixe
        'mtp': crawl_mtp.crawl,  # Wichí Lhamtés Nocten
        'muh': crawl_muh.crawl,  # Mündü
        'mur': crawl_mur.crawl,  # Murle
        'mux': crawl_mux.crawl,  # Bo-Ung
        'muy': crawl_muy.crawl,  # Muyang
        'mva': crawl_mva.crawl,  # Manam
        'mvp': crawl_mvp.crawl,  # Duri
        'mwv': crawl_mwv.crawl,  # Mentawai
        'mxb': crawl_mxb.crawl,  # Tezoatlán Mixtec
        'mxt': crawl_mxt.crawl,  # Jamiltepec Mixtec
        'my': crawl_my.crawl,    # Burmese
        'my-t-d0-zawgyi': crawl_my_t_d0_zawgyi.crawl,  # Burmese (Zawgyi)
        'myb': crawl_myb.crawl,  # Mbay
        'myk': crawl_myk.crawl,  # Mamara Senoufo
        'myv': crawl_myv.crawl,  # Erzya
        'myw': crawl_myw.crawl,  # Muyuw
        'myx': crawl_myx.crawl,  # Masaaba
        'myy': crawl_myy.crawl,  # Macuna
        'mza': crawl_mza.crawl,  # Santa María Zacatepec Mixtec
        'mzi': crawl_mzi.crawl,  # Ixcatlán Mazatec
        'mzk': crawl_mzk.crawl,  # Nigeria Mambila
        'mzm': crawl_mzm.crawl,  # Mumuye
        'naf': crawl_naf.crawl,  # Nabak
        'nak': crawl_nak.crawl,  # Nakanai
        'nan': crawl_nan.crawl,  # Min Nan Chinese
        'nan-Latn': crawl_nan_Latn.crawl,  # Min Nan Chinese (Latin)
        'nas': crawl_nas.crawl,  # Naasioi
        'nca': crawl_nca.crawl,  # Iyo
        'nch': crawl_nch.crawl,  # Central Huasteca Nahuatl
        'ncj': crawl_ncj.crawl,  # Northern Puebla Nahuatl
        'ncu': crawl_ncu.crawl,  # Chumburung
        'ndj': crawl_ndj.crawl,  # Ndamba
        'ndy': crawl_ndy.crawl,  # Lutos
        'ndz': crawl_ndz.crawl,  # Ndogo
        'neb': crawl_neb.crawl,  # Toura
        'new': crawl_new.crawl,  # Newari
        'nfr': crawl_nfr.crawl,  # Nafaanra
        'ngp': crawl_ngp.crawl,  # Ngulu
        'nho': crawl_nho.crawl,  # Takuu
        'nhu': crawl_nhu.crawl,  # Noone
        'nhw': crawl_nhw.crawl,  # Western Huasteca Nahuatl
        'nhy': crawl_nhy.crawl,  # Northern Oaxaca Nahuatl
        'nia': crawl_nia.crawl,  # Nias
        'nii': crawl_nii.crawl,  # Nii
        'nij': crawl_nij.crawl,  # Ngaju
        'nim': crawl_nim.crawl,  # Nilamba
        'nin': crawl_nin.crawl,  # Ninzo
        'nkf': crawl_nkf.crawl,  # Inpui Naga
        'nko': crawl_nko.crawl,  # Nkonya
        'nl': crawl_nl.crawl,    # Dutch
        'nlc': crawl_nlc.crawl,  # Nalca
        'nmz': crawl_nmz.crawl,  # Nawdm
        'nnb': crawl_nnb.crawl,  # Nande
        'nnq': crawl_nnq.crawl,  # Ngindo
        'nnw': crawl_nnw.crawl,  # Southern Nuni
        'noa': crawl_noa.crawl,  # Woun Meu
        'nog': crawl_nog.crawl,  # Nogai
        'nop': crawl_nop.crawl,  # Numanggang
        'not': crawl_not.crawl,  # Nomatsiguenga
        'nou': crawl_nou.crawl,  # Ewage-Notu
        'npl': crawl_npl.crawl,  # Southeastern Puebla Nahuatl
        'npy': crawl_npy.crawl,  # Napu
        'nsn': crawl_nsn.crawl,  # Nehan
        'nsu': crawl_nsu.crawl,  # Sierra Negra Nahuatl
        'ntm': crawl_ntm.crawl,  # Nateni
        'ntp': crawl_ntp.crawl,  # Northern Tepehuan
        'ntr': crawl_ntr.crawl,  # Delo
        'nuj': crawl_nuj.crawl,  # Nyole
        'nus': crawl_nus.crawl,  # Nuer
        'nvm': crawl_nvm.crawl,  # Namiae
        'nwb': crawl_nwb.crawl,  # Nyabwa
        'nwi': crawl_nwi.crawl,  # Southwest Tanna
        'ny': crawl_ny.crawl,    # Nyanja
        'nyf': crawl_nyf.crawl,  # Giryama
        'nyn': crawl_nyn.crawl,  # Nyankole
        'nyo': crawl_nyo.crawl,  # Nyoro
        'nyy': crawl_nyy.crawl,  # Nyakyusa-Ngonde
        'nzi': crawl_nzi.crawl,  # Nzima
        'obo': crawl_obo.crawl,  # Obo Manobo
        'oc': crawl_oc.crawl,    # Occitan
        'oku': crawl_oku.crawl,  # Oku
        'okv': crawl_okv.crawl,  # Orokaiva
        'old': crawl_old.crawl,  # Mochi
        'ong': crawl_ong.crawl,  # Olo
        'opm': crawl_opm.crawl,  # Oksapmin
        'or': crawl_or.crawl,    # Oriya
        'os': crawl_os.crawl,    # Ossetic
        'osa': crawl_osa.crawl,  # Osage
        'otd': crawl_otd.crawl,  # Ot Danum
        'ote': crawl_ote.crawl,  # Mezquital Otomi
        'ozm': crawl_ozm.crawl,  # Koonzime
        'pa': crawl_pa.crawl,    # Punjabi
        'pab': crawl_pab.crawl,  # Parecís
        'pad': crawl_pad.crawl,  # Paumarí
        'pag': crawl_pag.crawl,  # Pangasinan
        'pah': crawl_pah.crawl,  # Tenharim
        'pam': crawl_pam.crawl,  # Pampanga
        'pau': crawl_pau.crawl,  # Palauan
        'pbc': crawl_pbc.crawl,  # Patamona
        'pbi': crawl_pbi.crawl,  # Parkwa
        'pck': crawl_pck.crawl,  # Paite Chin
        'pcm': crawl_pcm.crawl,  # Nigerian Pidgin
        'pez': crawl_pez.crawl,  # Eastern Penan
        'pi-Mymr': crawl_pi_Mymr.crawl, # Pali in Myanmar script
        'pib': crawl_pib.crawl,  # Yine
        'pir': crawl_pir.crawl,  # Piratapuyo
        'pis': crawl_pis.crawl,  # Pijin
        'pjt': crawl_pjt.crawl,  # Pitjantjatjara
        'pkb': crawl_pkb.crawl,  # Pokomo
        'pl': crawl_pl.crawl,    # Polish
        'plw': crawl_plw.crawl,  # Brooke's Point Palawano
        'pmf': crawl_pmf.crawl,  # Pamona
        'pny': crawl_pny.crawl,  # Pinyin
        'poh': crawl_poh.crawl,  # Poqomchi'
        'poi': crawl_poi.crawl,  # Highland Popoluca
        'poy': crawl_poy.crawl,  # Pogolo
        'ppk': crawl_ppk.crawl,  # Uma
        'ppo': crawl_ppo.crawl,  # Folopa
        'prf': crawl_prf.crawl,  # Paranan
        'prk': crawl_prk.crawl,  # Parauk
        'ps': crawl_ps.crawl,    # Pashto
        'pss': crawl_pss.crawl,  # Kaulong
        'pt': crawl_pt.crawl,    # Portuguese
        'pt-PT': crawl_pt_PT.crawl,      # Portuguese (Portugal)
        'ptp': crawl_ptp.crawl,  # Patep
        'ptu': crawl_ptu.crawl,  # Bambam
        'pwg': crawl_pwg.crawl,  # Gapapaiwa
        'pww': crawl_pww.crawl,  # Pwo Northern Karen
        'pxm': crawl_pxm.crawl,  # Quetzaltepec Mixé
        'qu': crawl_qu.crawl,    # Quechua
        'qub': crawl_qub.crawl,  # Huallaga Huánuco Quechua
        'quc': crawl_quc.crawl,  # K'iche'
        'quf': crawl_quf.crawl,  # Lambayeque Quechua
        'quh': crawl_quh.crawl,  # South Bolivian Quechua
        'qul': crawl_qul.crawl,  # North Bolivian Quechua
        'qup': crawl_qup.crawl,  # Southern Pastaza Quechua
        'quw': crawl_quw.crawl,  # Tena Lowland Quichua
        'quy': crawl_quy.crawl,  # Ayacucho Quechua
        'qvc': crawl_qvc.crawl,  # Cajamarca Quechua
        'qve': crawl_qve.crawl,  # Eastern Apurímac Quechua
        'qvi': crawl_qvi.crawl,  # Imbabura Highland Quichua
        'qvm': crawl_qvm.crawl,  # Margos-Yarowilca-Lauricocha Quechua
        'qvn': crawl_qvn.crawl,  # North Junín Quechua
        'qvo': crawl_qvo.crawl,  # Napo Lowland Quechua
        'qvs': crawl_qvs.crawl,  # San Martín Quechua
        'qvw': crawl_qvw.crawl,  # Huaylla Wanca Quechua
        'qvz': crawl_qvz.crawl,  # Northern Pastaza Quichua
        'qwh': crawl_qwh.crawl,  # Huaylas Ancash Quechua
        'qxh': crawl_qxh.crawl,  # Panao Huánuco Quechua
        'qxl': crawl_qxl.crawl,  # Salasaca Highland Quichua
        'qxn': crawl_qxn.crawl,  # Northern Conchucos Ancash Quechua
        'qxo': crawl_qxo.crawl,  # Southern Conchucos Ancash Quechua
        'qxr': crawl_qxr.crawl,  # Cañar Highland Quichua
        'rai': crawl_rai.crawl,  # Ramoaaina
        'raj': crawl_raj.crawl,  # Malvi
        'rav': crawl_rav.crawl,  # Sampang
        'rej': crawl_rej.crawl,  # Rejang
        'rim': crawl_rim.crawl,  # Nyaturu
        'rm': crawl_rm.crawl,    # Romansh
        'rmc': crawl_rmc.crawl,  # Carpathian Romani
        'rmo': crawl_rmo.crawl,  # Sinte Romani
        'rn': crawl_rn.crawl,    # Rundi
        'rnl': crawl_rnl.crawl,  # Ranglong
        'ro': crawl_ro.crawl,    # Romanian
        'ro-MD': crawl_ro_MD.crawl,  # Moldovan
        'rom': crawl_rom.crawl,  # Vlax Romani
        'roo': crawl_roo.crawl,  # Rotokas
        'rro': crawl_rro.crawl,  # Waima
        'ru': crawl_ru.crawl,    # Russian
        'ruf': crawl_ruf.crawl,  # Luguru
        'rug': crawl_rug.crawl,  # Roviana
        'rw': crawl_rw.crawl,    # Kinyarwanda
        'rwo': crawl_rwo.crawl,  # Rawa
        'sab': crawl_sab.crawl,  # Buglere
        'sah': crawl_sah.crawl,  # Sakha
        'sas': crawl_sas.crawl,  # Sasak
        'sat': crawl_sat.crawl,  # Santali
        'sba': crawl_sba.crawl,  # Ngambay
        'sbl': crawl_sbl.crawl,  # Botolan Sambal
        'sck': crawl_sck.crawl,  # Sadri
        'sda': crawl_sda.crawl,  # Toraja-Sa'dan
        'seh': crawl_seh.crawl,  # Sena
        'sey': crawl_sey.crawl,  # Secoya
        'sg': crawl_sg.crawl,    # Sango
        'sgb': crawl_sgb.crawl,  # Mag-antsi Ayta
        'sgw': crawl_sgw.crawl,  # Sebat Bet Gurage
        'sgz': crawl_sgz.crawl,  # Sursurunga
        'shk': crawl_shk.crawl,  # Shilluk
        'shn': crawl_shn.crawl,  # Shan
        'shp': crawl_shp.crawl,  # Shipibo-Conibo
        'si': crawl_si.crawl,    # Sinhala
        'sig': crawl_sig.crawl,  # Paasaal
        'sil': crawl_sil.crawl,  # Tumulung Sisaala
        'sim': crawl_sim.crawl,  # Mende
        'sja': crawl_sja.crawl,  # Epena
        'sk': crawl_sk.crawl,    # Slovak
        'sl': crawl_sl.crawl,    # Slovenian
        'sld': crawl_sld.crawl,  # Sissala
        'sll': crawl_sll.crawl,  # Salt-Yui
        'sm': crawl_sm.crawl,    # Samoan
        'smt': crawl_smt.crawl,  # Simte
        'sn': crawl_sn.crawl,    # Shona
        'snc': crawl_snc.crawl,  # Sinaugoro
        'snn': crawl_snn.crawl,  # Siona
        'snp': crawl_snp.crawl,  # Siane
        'snw': crawl_snw.crawl,  # Selee
        'sny': crawl_sny.crawl,  # Saniyo-Hiyewe
        'so': crawl_so.crawl,    # Somali
        'soq': crawl_soq.crawl,  # Kanasi
        'soy': crawl_soy.crawl,  # Miyobe
        'spl': crawl_spl.crawl,  # Selepet
        'spp': crawl_spp.crawl,  # Supyire Senoufo
        'sps': crawl_sps.crawl,  # Saposa
        'sq': crawl_sq.crawl,    # Albanian
        'sr': crawl_sr.crawl,    # Serbian
        'sr-Latn': crawl_sr_Latn.crawl,  # Serbian (Latin)
        'sri': crawl_sri.crawl,  # Siriano
        'srm': crawl_srm.crawl,  # Saramaccan
        'srn': crawl_srn.crawl,  # Sranan Tongo
        'ssd': crawl_ssd.crawl,  # Siroi
        'ssg': crawl_ssg.crawl,  # Seimat
        'ssx': crawl_ssx.crawl,  # Samberigi
        'stn': crawl_stn.crawl,  # Owa
        'su': crawl_su.crawl,    # Sundanese
        'sua': crawl_sua.crawl,  # Sulka
        'sue': crawl_sue.crawl,  # Suena
        'sur': crawl_sur.crawl,  # Mwaghavul
        'sus': crawl_sus.crawl,  # Susu
        'suz': crawl_suz.crawl,  # Sunwar
        'sv': crawl_sv.crawl,    # Swedish
        'sw': crawl_sw.crawl,    # Swahili
        'swp': crawl_swp.crawl,  # Suau
        'sxn': crawl_sxn.crawl,  # Sangir
        'ta': crawl_ta.crawl,    # Tamil
        'tab': crawl_tab.crawl,  # Tabassaran
        'taj': crawl_taj.crawl,  # Eastern Tamang
        'tap': crawl_tap.crawl,  # Taabwa
        'taq': crawl_taq.crawl,  # Tamasheq
        'tav': crawl_tav.crawl,  # Tatuyo
        'taw': crawl_taw.crawl,  # Tai
        'tbc': crawl_tbc.crawl,  # Takia
        'tbg': crawl_tbg.crawl,  # North Tairora
        'tbo': crawl_tbo.crawl,  # Tawala
        'tby': crawl_tby.crawl,  # Tabaru
        'tbz': crawl_tbz.crawl,  # Ditammari
        'tca': crawl_tca.crawl,  # Ticuna
        'tcc': crawl_tcc.crawl,  # Datooga
        'te': crawl_te.crawl,    # Telugu
        'ted': crawl_ted.crawl,  # Tepo Krumen
        'tem': crawl_tem.crawl,  # Timne
        'teo': crawl_teo.crawl,  # Teso
        'ter': crawl_ter.crawl,  # Tereno
        'tfr': crawl_tfr.crawl,  # Teribe
        'tgo': crawl_tgo.crawl,  # Sudest
        'tgp': crawl_tgp.crawl,  # Tangoa
        'th': crawl_th.crawl,    # Thai
        'thk': crawl_thk.crawl,  # Tharaka
        'ti': crawl_ti.crawl,    # Tigrinya
        'tif': crawl_tif.crawl,  # Tifal
        'tih': crawl_tih.crawl,  # Timugon Murut
        'tik': crawl_tik.crawl,  # Tikar
        'tim': crawl_tim.crawl,  # Timbe
        'tk': crawl_tk.crawl,    # Turkmen
        'tlb': crawl_tlb.crawl,  # Tobelo
        'tlf': crawl_tlf.crawl,  # Telefol
        'tlj': crawl_tlj.crawl,  # Talinga-Bwisi
        'tmc': crawl_tmc.crawl,  # Tumak
        'tna': crawl_tna.crawl,  # Tacana
        'tnr': crawl_tnr.crawl,  # Ménik
        'to': crawl_to.crawl,    # Tonga
        'tob': crawl_tob.crawl,  # Toba
        'toc': crawl_toc.crawl,  # Coyutla Totonac
        'toh': crawl_toh.crawl,  # Gitonga
        'top': crawl_top.crawl,  # Papantla Totonac
        'tos': crawl_tos.crawl,  # Highland Totonac
        'tpi': crawl_tpi.crawl,  # Tok Pisin
        'tpm': crawl_tpm.crawl,  # Tampulma
        'tpp': crawl_tpp.crawl,  # Pisaflores Tepehua
        'tpt': crawl_tpt.crawl,  # Tlachichilco Tepehua
        'tpz': crawl_tpz.crawl,  # Tinputz
        'tqo': crawl_tqo.crawl,  # Toaripi
        'tr': crawl_tr.crawl,    # Turkish
        'trs': crawl_trs.crawl,  # Chicahuaxtla Triqui
        'tsz': crawl_tsz.crawl,  # Purepecha
        'tt': crawl_tt.crawl,    # Tatar
        'ttc': crawl_ttc.crawl,  # Tektiteko
        'tte': crawl_tte.crawl,  # Bwanabwana
        'tue': crawl_tue.crawl,  # Tuyuca
        'tuf': crawl_tuf.crawl,  # Central Tunebo
        'twb': crawl_twb.crawl,  # Western Tawbuid
        'twu': crawl_twu.crawl,  # Termanu
        'txa': crawl_txa.crawl,  # Tombonuo
        'txu': crawl_txu.crawl,  # Kayapó
        'tyv': crawl_tyv.crawl,  # Tuvinian
        'tyz': crawl_tyz.crawl,  # Tày
        'tzh': crawl_tzh.crawl,  # Tzeltal
        'tzj': crawl_tzj.crawl,  # Tz'utujil
        'ubr': crawl_ubr.crawl,  # Ubir
        'ubu': crawl_ubu.crawl,  # Umbu-Ungu
        'udm': crawl_udm.crawl,  # Udmurt
        'udu': crawl_udu.crawl,  # Uduk
        'ug': crawl_ug.crawl,    # Uyghur
        'uk': crawl_uk.crawl,    # Ukrainian
        'ur': crawl_ur.crawl,    # Urdu
        'ura': crawl_ura.crawl,  # Urarina
        'urb': crawl_urb.crawl,  # Urubú-Kaapor
        'urk': crawl_urk.crawl,  # Urak Lawoi'
        'ury': crawl_ury.crawl,  # Orya
        'usa': crawl_usa.crawl,  # Usarufa
        'usp': crawl_usp.crawl,  # Uspanteco
        'uvl': crawl_uvl.crawl,  # Lote
        'uz': crawl_uz.crawl,    # Uzbek
        'vag': crawl_vag.crawl,  # Vagla
        'vec': crawl_vec.crawl,  # Venetian
        'vi': crawl_vi.crawl,    # Vietnamese
        'vid': crawl_vid.crawl,  # Vidunda
        'viv': crawl_viv.crawl,  # Iduna
        'vmw': crawl_vmw.crawl,  # Makhuwa
        'vun': crawl_vun.crawl,  # Vunjo
        'vut': crawl_vut.crawl,  # Vute
        'waj': crawl_waj.crawl,  # Waffa
        'wap': crawl_wap.crawl,  # Wapishana
        'war': crawl_war.crawl,  # Waray
        'way': crawl_way.crawl,  # Wayana
        'wer': crawl_wer.crawl,  # Weri
        'wiu': crawl_wiu.crawl,  # Wiru
        'wlx': crawl_wlx.crawl,  # Wali
        'wmw': crawl_wmw.crawl,  # Mwani
        'wnc': crawl_wnc.crawl,  # Wantoat
        'wnu': crawl_wnu.crawl,  # Usan
        'wob': crawl_wob.crawl,  # Wè Northern
        'wos': crawl_wos.crawl,  # Hanga Hundi
        'wrs': crawl_wrs.crawl,  # Waris
        'wsk': crawl_wsk.crawl,  # Waskia
        'wuv': crawl_wuv.crawl,  # Wuvulu-Aua
        'wwa': crawl_wwa.crawl,  # Waama
        'xal': crawl_xal.crawl,  # Kalmyk
        'xav': crawl_xav.crawl,  # Xavánte
        'xed': crawl_xed.crawl,  # Hdi
        'xla': crawl_xla.crawl,  # Kamula
        'xog': crawl_xog.crawl,  # Soga
        'xrb': crawl_xrb.crawl,  # Eastern Karaboro
        'xsb': crawl_xsb.crawl,  # Sambal
        'xsi': crawl_xsi.crawl,  # Sio
        'xsm': crawl_xsm.crawl,  # Kasem
        'xsr': crawl_xsr.crawl,  # Sherpa
        'xsu': crawl_xsu.crawl,  # Sanumá
        'xtd': crawl_xtd.crawl,  # Diuxi-Tilantongo Mixtec
        'xtm': crawl_xtm.crawl,  # Magdalena Peñasco Mixtec
        'xuo': crawl_xuo.crawl,  # Kuo
        'yaa': crawl_yaa.crawl,  # Yaminahua
        'yad': crawl_yad.crawl,  # Yagua
        'yal': crawl_yal.crawl,  # Yalunka
        'yam': crawl_yam.crawl,  # Yamba
        'yaz': crawl_yaz.crawl,  # Lokaa
        'yby': crawl_yby.crawl,  # Yaweyuha
        'ycn': crawl_ycn.crawl,  # Yucuna
        'yle': crawl_yle.crawl,  # Yele
        'yli': crawl_yli.crawl,  # Angguruk Yali
        'yml': crawl_yml.crawl,  # Iamalele
        'yo': crawl_yo.crawl,    # Yoruba
        'yon': crawl_yon.crawl,  # Yongkom
        'yrb': crawl_yrb.crawl,  # Yareba
        'yre': crawl_yre.crawl,  # Yaouré
        'yss': crawl_yss.crawl,  # Yessan-Mayo
        'yua': crawl_yua.crawl,  # Yucateco
        'yue': crawl_yue.crawl,  # Cantonese
        'yuj': crawl_yuj.crawl,  # Karkar-Yuri
        'yut': crawl_yut.crawl,  # Yopno
        'yuw': crawl_yuw.crawl,  # Yau
        'yva': crawl_yva.crawl,  # Yawa
        'zaa': crawl_zaa.crawl,  # Sierra de Juárez Zapotec
        'zab': crawl_zab.crawl,  # San Juan Guelavía Zapotec
        'zac': crawl_zac.crawl,  # Ocotlán Zapotec
        'zad': crawl_zad.crawl,  # Cajonos Zapotec
        'zae': crawl_zae.crawl,  # Yareni Zapotec
        'zap': crawl_zap.crawl,  # Zapotec
        'zar': crawl_zar.crawl,  # Rincón Zapotec
        'zas': crawl_zas.crawl,  # Santo Domingo Albarradas Zapotec
        'zaw': crawl_zaw.crawl,  # Mitla Zapotec
        'zca': crawl_zca.crawl,  # Coatecas Altas Zapotec
        'zia': crawl_zia.crawl,  # Zia
        'ziw': crawl_ziw.crawl,  # Zigula
        'zlm': crawl_zlm.crawl,  # Malay
        'zne': crawl_zne.crawl,  # Zande
        'zpc': crawl_zpc.crawl,  # Choapan Zapotec
        'zpi': crawl_zpi.crawl,  # Santa María Quiegolani Zapotec
        'zpq': crawl_zpq.crawl,  # Zoogocho Zapotec
        'zpt': crawl_zpt.crawl,  # San Vicente Coatlán Zapotec
        'zpz': crawl_zpz.crawl,  # Texmelucan Zapotec
        'zyp': crawl_zyp.crawl,  # Zyphe Chin
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
    parser.add_argument(
        '--crawldelay', default='15',
        help='number of seconds between fetches')
    args = parser.parse_args()

    crawler = Crawler(language=args.language, output_dir=args.output,
                      cache_dir=args.cache, crawldelay=float(args.crawldelay))
    crawls[args.language](crawler)
    crawler.close()
