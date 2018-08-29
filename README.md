# Corpus Crawler

_Corpus Crawler_ is a tool for
[Corpus Linguistics](https://en.wikipedia.org/wiki/Corpus_linguistics).

Modern linguistic research works on language corpora, which are large samples of
“real world” text.  This crawler helps to build such corpora: it follows links
to publicly accessible web pages known to be written in a certain language; it
removes boilerplate and HTML markup; finally, it writes its output into
plaintext files.  The crawler implements the
[Robots Exclusion Standard](https://en.wikipedia.org/wiki/Robots_exclusion_standard),
and it is intentionally slow so it does not cause much load on the crawled
web sites.

This is not an official Google product.  But if you’re a linguistic researcher,
or if you’re writing a spell checker (or similar language-processing software)
for an “exotic” language, you might find _Corpus Crawler_ useful.

To build corpora for not-yet-supported languages, please read the
[contribution guidelines](./CONTRIBUTING.md) and send us
[GitHub pull requests](https://help.github.com/categories/collaborating-with-issues-and-pull-requests/).

The crawled corpora have been used to compute word frequencies in
Unicode’s [Unilex project](https://github.com/unicode-org/unilex).


## Supported Languages

| IETF BCP47 Code     | Language                     |  Tokens¹                                                                            |
| :------------------ | :--------------------------- | ----------------------------------------------------------------------------------: |
| `aai`               | Arifama-Miniafia             |    181K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aai.txt)               |
| `aak`               | Ankave                       |    194K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aak.txt)               |
| `aau`               | Abau                         |    313K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aau.txt)               |
| `aaz`               | Amarasi                      |    308K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aaz.txt)               |
| `abt`               | Ambulas                      |    297K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/abt.txt)               |
| `aby`               | Aneme Wake                   |    233K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aby.txt)               |
| `acd`               | Gikyode                      |    323K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/acd.txt)               |
| `ace`               | Aceh/Acehnese                |    817K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ace.txt)               |
| `acf`               | Saint Lucian Creole French   |    236K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/acf.txt)               |
| `ach`               | Acoli                        |    178K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ach.txt)               |
| `acn`               | Achang                       |    232K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/acn.txt)               |
| `acr`               | Achi                         |    239K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/acr.txt)               |
| `acu`               | Achuar-Shiwiar               |    174K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/acu.txt)               |
| `ade`               | Adele                        |    267K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ade.txt)               |
| `adh`               | Adhola                       |    166K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/adh.txt)               |
| `adj`               | Adioukrou                    |    233K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/adj.txt)               |
| `ae`                | Avestan                      |    129K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ae.txt)                |
| `ae-Latn`           | Avestan (Latin)              |    141K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ae-Latn.txt)           |
| `aey`               | Amele                        |    218K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aey.txt)               |
| `agd`               | Agarabi                      |    256K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/agd.txt)               |
| `agg`               | Angor                        |    214K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/agg.txt)               |
| `agm`               | Angaataha                    |    238K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/agm.txt)               |
| `agn`               | Agutaynen                    |    234K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/agn.txt)               |
| `agr`               | Aguaruna                     |    149K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/agr.txt)               |
| `ahk`               | Akha                         |    367K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ahk.txt)               |
| `aia`               | Arosi                        |    223K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aia.txt)               |
| `akb`               | Batak Angkola                |    220K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/akb.txt)               |
| `ake`               | Akawaio                      |    190K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ake.txt)               |
| `akh`               | Akha                         |    408K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/akh.txt)               |
| `akp`               | Siwu                         |    191K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/akp.txt)               |
| `alj`               | Alangan                      |    185K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/alj.txt)               |
| `alp`               | Alune                        |    225K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/alp.txt)               |
| `alt`               | Southern Altai               |    121K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/alt.txt)               |
| `alz`               | Alur                         |    160K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/alz.txt)               |
| `am`                | Amharic                      |  2,170K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/am.txt)                |
| `ame`               | Yanesha'                     |    221K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ame.txt)               |
| `amf`               | Hamer-Banna                  |    152K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/amf.txt)               |
| `amk`               | Ambai                        |    229K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/amk.txt)               |
| `amm`               | Ama (Papua New Guinea)       |    246K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/amm.txt)               |
| `amn`               | Amanab                       |    207K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/amn.txt)               |
| `amp`               | Alamblak                     |    241K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/amp.txt)               |
| `amr`               | Amarakaeri                   |    151K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/amr.txt)               |
| `amu`               | Guerrero Amuzgo              |    202K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/amu.txt)               |
| `ann`               | Obolo                        |    236K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ann.txt)               |
| `anv`               | Denya                        |    214K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/anv.txt)               |
| `aoj`               | Mufian                       |    217K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aoj.txt)               |
| `aom`               | Ömie                         |    231K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aom.txt)               |
| `aon`               | Bumbita Arapesh              |    294K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aon.txt)               |
| `aoz`               | Uab Meto                     |    197K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aoz.txt)               |
| `ape`               | Bukiyip                      |    294K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ape.txt)               |
| `apr`               | Arop-Lokep                   |    373K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/apr.txt)               |
| `apz`               | Safeyoka                     |    235K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/apz.txt)               |
| `ar`                | Arabic                       | 19,593K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ar.txt)                |
| `arl`               | Arabela                      |    206K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/arl.txt)               |
| `asg`               | Cishingini                   |    270K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/asg.txt)               |
| `aso`               | Dano                         |    290K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aso.txt)               |
| `ata`               | Pele-Ata                     |    248K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ata.txt)               |
| `atb`               | Zaiwa                        |    291K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/atb.txt)               |
| `atg`               | Ivbie North-Okpela-Arhe      |    229K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/atg.txt)               |
| `atq`               | Aralle-Tabulahan             |    202K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/atq.txt)               |
| `auy`               | Awiyaana                     |    164K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/auy.txt)               |
| `av`                | Avaric                       |    111K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/av.txt)                |
| `avn`               | Avatime                      |    229K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/avn.txt)               |
| `avt`               | Au                           |    263K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/avt.txt)               |
| `avu`               | Avokaya                      |    391K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/avu.txt)               |
| `awa`               | Awadhi                       |    211K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/awa.txt)               |
| `awb`               | Awa (Papua New Guinea)       |    179K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/awb.txt)               |
| `ay`                | Aymara                       |    482K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ay.txt)                |
| `ayo`               | Ayoreo                       |    264K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ayo.txt)               |
| `az`                | Azerbaijani                  |  3,413K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/az.txt)                |
| `azg`               | San Pedro Amuzgos Amuzgo     |    271K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/azg.txt)               |
| `azz`               | Highland Puebla Nahuatl      |    265K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/azz.txt)               |
| `ba`                | Bashkir                      |    666K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ba.txt)                |
| `ban`               | Balinese                     |    211K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ban.txt)               |
| `bao`               | Waimaha                      |    232K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bao.txt)               |
| `bav`               | Vengo                        |    250K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bav.txt)               |
| `bba`               | Baatonum                     |    792K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bba.txt)               |
| `bbb`               | Barai                        |    289K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bbb.txt)               |
| `bbo`               | Northern Bobo Madaré         |    211K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bbo.txt)               |
| `bbr`               | Girawa                       |    245K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bbr.txt)               |
| `bch`               | Bariai                       |    248K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bch.txt)               |
| `bcw`               | Bana                         |    304K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bcw.txt)               |
| `bdd`               | Bunama                       |    171K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bdd.txt)               |
| `be`                | Belarusian                   |  1,441K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/be.txt)                |
| `be-tarask`         | Belarusian (Taraškievica)    | 108,431K [💾](http://www.gstatic.com/i18n/corpora/wordcounts/be-tarask.txt)         |
| `bef`               | Benabena                     |    239K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bef.txt)               |
| `bep`               | Besoa                        |    204K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bep.txt)               |
| `bex`               | Jur Modo                     |    254K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bex.txt)               |
| `bfd`               | Bafut                        |    276K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bfd.txt)               |
| `bfo`               | Malba Birifor                |    260K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bfo.txt)               |
| `bg`                | Bulgarian                    | 10,597K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bg.txt)                |
| `bgr`               | Bawm Chin                    |    213K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bgr.txt)               |
| `bgz`               | Banggai                      |    186K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bgz.txt)               |
| `bhl`               | Bimin                        |    324K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bhl.txt)               |
| `bhw`               | Biak                         |    164K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bhw.txt)               |
| `bi`                | Bislama                      |    315K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bi.txt)                |
| `bib`               | Bissa                        |    243K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bib.txt)               |
| `big`               | Biangai                      |    229K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/big.txt)               |
| `bik`               | Central Bikol                |    183K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bik.txt)               |
| `bim`               | Bimoba                       |    215K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bim.txt)               |
| `biv`               | Southern Birifor             |    221K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/biv.txt)               |
| `bjr`               | Binumarien                   |    226K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bjr.txt)               |
| `bjv`               | Bedjond                      |    268K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bjv.txt)               |
| `bkl`               | Berik                        |    306K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bkl.txt)               |
| `bku`               | Buhid                        |    204K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bku.txt)               |
| `bkv`               | Bekwarra                     |    244K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bkv.txt)               |
| `blh`               | Kuwaa                        |    259K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/blh.txt)               |
| `blt-Latn`          | Tai Dam (Latin)              |    262K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/blt-Latn.txt)          |
| `blz`               | Balantak                     |    199K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/blz.txt)               |
| `bm`                | Bambara                      |     30K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bm.txt)                |
| `bmh`               | Kein                         |    253K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bmh.txt)               |
| `bmq`               | Bomu                         |    207K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bmq.txt)               |
| `bmr`               | Muinane                      |    122K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bmr.txt)               |
| `bmu`               | Somba-Siawari                |    234K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bmu.txt)               |
| `bmv`               | Bum                          |    258K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bmv.txt)               |
| `bn`                | Bangla                       |  7,258K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bn.txt)                |
| `bnj`               | Eastern Tawbuid              |    239K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bnj.txt)               |
| `bnp`               | Bola                         |    263K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bnp.txt)               |
| `bo`                | Tibetan                      |  5,642K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bo.txt)                |
| `boa`               | Bora                         |    133K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/boa.txt)               |
| `boj`               | Anjam                        |    255K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/boj.txt)               |
| `bon`               | Bine                         |    244K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bon.txt)               |
| `bov`               | Tuwuli                       |    203K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bov.txt)               |
| `box`               | Buamu                        |    274K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/box.txt)               |
| `bpr`               | Koronadal Blaan              |    204K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bpr.txt)               |
| `bps`               | Sarangani Blaan              |    214K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bps.txt)               |
| `bqc`               | Boko                         |    567K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bqc.txt)               |
| `bqj`               | Bandial                      |    175K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bqj.txt)               |
| `bqp`               | Busa                         |    162K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bqp.txt)               |
| `bru`               | Eastern Bru                  |    261K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bru.txt)               |
| `bs`                | Bosnian                      |  8,993K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bs.txt)                |
| `bsn`               | Barasana-Eduria              |    225K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bsn.txt)               |
| `bss`               | Akoose                       |    199K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bss.txt)               |
| `btd`               | Batak Dairi                  |    192K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/btd.txt)               |
| `bts`               | Batak Simalungun             |    175K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bts.txt)               |
| `btt`               | Bete-Bendi                   |    266K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/btt.txt)               |
| `btx`               | Batak Karo                   |    189K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/btx.txt)               |
| `bua`               | Buriat                       |    143K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bua.txt)               |
| `bud`               | Ntcham                       |    207K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bud.txt)               |
| `buk`               | Bugawac                      |    264K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/buk.txt)               |
| `bus`               | Bokobaru                     |    159K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bus.txt)               |
| `bvc`               | Baelelea                     |    308K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bvc.txt)               |
| `bvz`               | Bauzi                        |    509K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bvz.txt)               |
| `bwq`               | Southern Bobo Madaré         |    214K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bwq.txt)               |
| `bwu`               | Buli                         |    285K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bwu.txt)               |
| `byr`               | Baruya                       |    182K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/byr.txt)               |
| `byx`               | Qaqet                        |    387K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/byx.txt)               |
| `bzh`               | Mapos Buang                  |    251K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bzh.txt)               |
| `bzi`               | Bisu                         |    381K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bzi.txt)               |
| `bzj`               | Belize Kriol English         |    240K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bzj.txt)               |
| `ca-valencia`       | Valencian                    | 24,295K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ca-valencia.txt)       |
| `caa`               | Chortí                       |    307K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/caa.txt)               |
| `cab`               | Garifuna                     |    154K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cab.txt)               |
| `cac`               | Chuj                         |    244K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cac.txt)               |
| `cak`               | Kaqchikel                    |    259K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cak.txt)               |
| `cap`               | Chipaya                      |    154K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cap.txt)               |
| `car`               | Galibi Carib                 |    160K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/car.txt)               |
| `cax`               | Chiquitano                   |    149K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cax.txt)               |
| `cbc`               | Carapana                     |    256K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cbc.txt)               |
| `cbi`               | Chachi                       |    187K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cbi.txt)               |
| `cbl`               | Bualkhaw Chin                |    210K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cbl.txt)               |
| `cbr`               | Cashibo-Cacataibo            |    236K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cbr.txt)               |
| `cbs`               | Cashinahua                   |    198K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cbs.txt)               |
| `cbt`               | Chayahuita                   |    150K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cbt.txt)               |
| `cbv`               | Cacua                        |    265K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cbv.txt)               |
| `cce`               | Chopi                        |    204K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cce.txt)               |
| `ccp`               | Chakma                       |     79K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ccp.txt)               |
| `cdf`               | Chiru                        |    193K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cdf.txt)               |
| `ce`                | Chechen                      |    669K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ce.txt)                |
| `ceb`               | Cebuano                      |  1,067K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ceb.txt)               |
| `ceg`               | Chamacoco                    |    232K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ceg.txt)               |
| `cfm`               | Falam Chin                   |    438K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cfm.txt)               |
| `cgc`               | Kagayanen                    |    299K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cgc.txt)               |
| `chj`               | Ojitlán Chinantec            |    305K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/chj.txt)               |
| `chm`               | Mari                         |    132K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/chm.txt)               |
| `chr`               | Cherokee                     |    119K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/chr.txt)               |
| `chz`               | Ozumacín Chinantec           |    205K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/chz.txt)               |
| `cjo`               | Ashéninka Pajonal            |    141K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cjo.txt)               |
| `cjp`               | Cabécar                      |    199K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cjp.txt)               |
| `cjv`               | Chuave                       |    286K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cjv.txt)               |
| `cko`               | Anufo                        |    272K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cko.txt)               |
| `cle`               | Lealao Chinantec             |    313K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cle.txt)               |
| `cme`               | Cerma                        |    230K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cme.txt)               |
| `cmr`               | Mro-Khimi Chin               |    275K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cmr.txt)               |
| `cnh`               | Hakha Chin                   |    934K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cnh.txt)               |
| `cni`               | Asháninka                    |    122K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cni.txt)               |
| `cnk`               | Khumi Chin                   |    237K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cnk.txt)               |
| `cnl`               | Lalana Chinantec             |    308K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cnl.txt)               |
| `cnt`               | Tepetotutla Chinantec        |    261K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cnt.txt)               |
| `coe`               | Koreguaje                    |    181K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/coe.txt)               |
| `cof`               | Colorado                     |    183K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cof.txt)               |
| `cok`               | Santa Teresa Cora            |    230K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cok.txt)               |
| `con`               | Cofán                        |    151K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/con.txt)               |
| `cot`               | Caquinte                     |    128K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cot.txt)               |
| `crh`               | Crimean Tatar                |    505K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/crh.txt)               |
| `cs`                | Czech                        |  3,141K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cs.txt)                |
| `csk`               | Jola-Kasa                    |    177K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/csk.txt)               |
| `cso`               | Sochiapam Chinantec          |    328K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cso.txt)               |
| `ctd-Latn`          | Tedim Chin (Latin)           |    852K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ctd-Latn.txt)          |
| `ctu`               | Chol                         |    203K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ctu.txt)               |
| `cub`               | Cubeo                        |    220K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cub.txt)               |
| `cuc`               | Usila Chinantec              |    278K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cuc.txt)               |
| `cui`               | Cuiba                        |    292K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cui.txt)               |
| `cuk`               | San Blas Kuna                |    187K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cuk.txt)               |
| `cul`               | Culina                       |    221K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cul.txt)               |
| `cv`                | Chuvash                      |    111K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cv.txt)                |
| `cwe`               | Kwere                        |    144K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cwe.txt)               |
| `cwt`               | Kuwaataay                    |    168K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cwt.txt)               |
| `cy`                | Welsh                        | 11,519K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cy.txt)                |
| `cya`               | Nopala Chatino               |    245K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cya.txt)               |
| `czt`               | Zotung Chin                  |    227K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/czt.txt)               |
| `da`                | Danish                       |    655K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/da.txt)                |
| `daa`               | Dangaléat                    |    208K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/daa.txt)               |
| `dad`               | Marik                        |    197K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dad.txt)               |
| `dah`               | Gwahatike                    |    274K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dah.txt)               |
| `ddn`               | Dendi                        |    210K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ddn.txt)               |
| `de`                | German                       | 46,431K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/de.txt)                |
| `ded`               | Dedua                        |    146K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ded.txt)               |
| `des`               | Desano                       |    210K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/des.txt)               |
| `dga`               | Southern Dagaare             |    458K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dga.txt)               |
| `dgi`               | Northern Dagara              |    257K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dgi.txt)               |
| `dgz`               | Daga                         |    219K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dgz.txt)               |
| `din`               | Southwestern Dinka           |    196K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/din.txt)               |
| `dip`               | Northeastern Dinka           |    193K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dip.txt)               |
| `djk`               | Eastern Maroon Creole        |    307K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/djk.txt)               |
| `dln`               | Darlong                      |    776K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dln.txt)               |
| `dnw`               | Western Dani                 |    254K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dnw.txt)               |
| `dob`               | Dobu                         |    179K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dob.txt)               |
| `dop`               | Lukpa                        |    226K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dop.txt)               |
| `dsh`               | Daasanach                    |    211K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dsh.txt)               |
| `dtb`               | Labuk-Kinabatangan Kadazan   |    248K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dtb.txt)               |
| `dtp`               | Kadazan Dusun                |  1,038K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dtp.txt)               |
| `dts`               | Toro So Dogon                |    202K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dts.txt)               |
| `due`               | Umiray Dumaget Agta          |    247K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/due.txt)               |
| `dug`               | Duruma                       |    172K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dug.txt)               |
| `duo`               | Dupaninan Agta               |    266K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/duo.txt)               |
| `dwr`               | Dawro                        |    254K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dwr.txt)               |
| `dww`               | Dawawa                       |    208K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dww.txt)               |
| `dyi`               | Djimini Senoufo              |    268K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dyi.txt)               |
| `dyo`               | Jola-Fonyi                   |    158K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dyo.txt)               |
| `dyu`               | Dyula                        |  1,156K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dyu.txt)               |
| `dz`                | Dzongkha                     |     61K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dz.txt)                |
| `ee`                | Ewe                          |    421K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ee.txt)                |
| `eka`               | Ekajuk                       |    213K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/eka.txt)               |
| `el`                | Greek                        |  5,470K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/el.txt)                |
| `emi`               | Mussau-Emira                 |    176K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/emi.txt)               |
| `emp`               | Northern Emberá              |    158K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/emp.txt)               |
| `enb`               | Markweeta                    |    147K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/enb.txt)               |
| `enq`               | Enga                         |    217K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/enq.txt)               |
| `enx`               | Enxet                        |    772K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/enx.txt)               |
| `eri`               | Ogea                         |    269K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/eri.txt)               |
| `es`                | Spanish                      | 32,670K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/es.txt)                |
| `ese`               | Ese Ejja                     |    226K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ese.txt)               |
| `et`                | Estonian                     |  3,658K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/et.txt)                |
| `eu`                | Basque                       |    130K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/eu.txt)                |
| `ewo`               | Ewondo                       |    158K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ewo.txt)               |
| `eza`               | Ezaa                         |    963K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/eza.txt)               |
| `fa`                | Persian                      |  9,114K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fa.txt)                |
| `fa-AF`             | Dari                         |  7,363K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fa-AF.txt)             |
| `faa`               | Fasu                         |    238K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/faa.txt)               |
| `fai`               | Faiwol                       |    256K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fai.txt)               |
| `fal`               | South Fali                   |    198K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fal.txt)               |
| `far`               | Fataleka                     |    286K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/far.txt)               |
| `fi`                | Finnish                      |  4,837K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fi.txt)                |
| `fil`               | Tagalog                      |    184K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fil.txt)               |
| `fip`               | Fipa                         |    134K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fip.txt)               |
| `fit`               | Tornedalen Finnish           |    292K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fit.txt)               |
| `fj`                | Fijian                       |    257K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fj.txt)                |
| `fo`                | Faroese                      |    851K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fo.txt)                |
| `fon`               | Fon                          |    266K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fon.txt)               |
| `for`               | Fore                         |    169K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/for.txt)               |
| `fr`                | French                       |  5,488K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fr.txt)               |
| `fue`               | Borgu Fulfulde               |    148K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fue.txt)               |
| `fuf`               | Pular                        |    174K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fuf.txt)               |
| `fuq`               | Central-Eastern Niger Fulfulde |  156K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fuq.txt)               |
| `fuv`               | Nigerian Fulfulde            |     13K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fuv.txt)               |
| `ga`                | Irish                        |  7,587K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ga.txt)                |
| `gag`               | Gagauz                       |    245K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gag.txt)               |
| `gah`               | Alekano                      |    210K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gah.txt)               |
| `gam`               | Kandawo                      |    250K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gam.txt)               |
| `gaw`               | Nobonob                      |    246K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gaw.txt)               |
| `gbi`               | Galela                       |    288K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gbi.txt)               |
| `gd`                | Scottish Gaelic              | 17,105K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gd.txt)                |
| `gde`               | Gude                         |    217K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gde.txt)               |
| `gdn`               | Umanakaina                   |    306K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gdn.txt)               |
| `gdr`               | Wipi                         |    271K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gdr.txt)               |
| `gej`               | Gen                          |    236K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gej.txt)               |
| `gfk`               | Patpatar                     |    294K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gfk.txt)               |
| `ghs`               | Guhu-Samane                  |    186K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ghs.txt)               |
| `gil`               | Gilbertese                   |    228K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gil.txt)               |
| `gkn`               | Gokana                       |    267K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gkn.txt)               |
| `gmv-Latn`          | Gamo (Latin)                 |    127K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gmv-Latn.txt)          |
| `gn`                | Guarani                      |    142K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gn.txt)                |
| `gnd`               | Zulgo-Gemzek                 |    364K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gnd.txt)               |
| `gng`               | Ngangam                      |    219K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gng.txt)               |
| `gnw`               | Western Bolivian Guaraní     |    263K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gnw.txt)               |
| `gof`               | Gofa                         |    124K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gof.txt)               |
| `gog`               | Gogo                         |    173K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gog.txt)               |
| `gor`               | Gorontalo                    |    211K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gor.txt)               |
| `gqr`               | Gor                          |    218K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gqr.txt)               |
| `grb`               | Northern Grebo               |    270K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/grb.txt)               |
| `grt`               | Garo                         |    141K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/grt.txt)               |
| `gso`               | Southwest Gbaya              |    228K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gso.txt)               |
| `gsw-u-sd-chag`     | Swiss German (Aargau)        |     99K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gsw-u-sd-chag.txt)     |
| `gsw-u-sd-chbe`     | Swiss German (Bern)          |     73K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gsw-u-sd-chbe.txt)     |
| `gsw-u-sd-chfr`     | Swiss German (Fribourg)      |     42K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gsw-u-sd-chfr.txt)     |
| `gu`                | Gujarati                     |    702K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gu.txt)                |
| `gub`               | Guajajára                    |    997K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gub.txt)               |
| `guc`               | Wayuu                        |    211K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/guc.txt)               |
| `gud`               | Yocoboué Dida                |    216K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gud.txt)               |
| `guh`               | Guahibo                      |    204K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/guh.txt)               |
| `gui`               | Eastern Bolivian Guaraní     |    197K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gui.txt)               |
| `gum`               | Guambiano                    |    186K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gum.txt)               |
| `gun`               | Mbyá Guaraní                 |    176K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gun.txt)               |
| `guo`               | Guayabero                    |    203K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/guo.txt)               |
| `guq`               | Aché                         |    184K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/guq.txt)               |
| `gur`               | Farefare                     |    240K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gur.txt)               |
| `gux`               | Gourmanchéma                 |    215K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gux.txt)               |
| `gv`                | Manx Gaelic                  |    152K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gv.txt)                |
| `gvc`               | Guanano                      |    241K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gvc.txt)               |
| `gvf`               | Golin                        |    276K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gvf.txt)               |
| `gvl`               | Gulay                        |    270K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gvl.txt)               |
| `gwr`               | Gwere                        |    157K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gwr.txt)               |
| `gym`               | Ngäbere                      |    294K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gym.txt)               |
| `gyr`               | Guarayu                      |    176K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gyr.txt)               |
| `ha`                | Hausa                        |  1,775K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ha.txt)                |
| `hae`               | Eastern Oromo                |    163K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hae.txt)               |
| `hag`               | Hanga                        |    202K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hag.txt)               |
| `haw`               | Hawaiian                     |  2,221K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/haw.txt)               |
| `hay`               | Haya                         |    112K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hay.txt)               |
| `heh`               | Hehe                         |    136K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/heh.txt)               |
| `hi`                | Hindi                        | 10,004K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hi.txt)                |
| `hif`               | Fiji Hindi                   |    204K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hif.txt)               |
| `hig`               | Kamwe                        |    261K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hig.txt)               |
| `hil`               | Hiligaynon                   |    208K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hil.txt)               |
| `hla`               | Halia                        |    273K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hla.txt)               |
| `hne`               | Chhattisgarhi                |    207K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hne.txt)               |
| `hnn`               | Hanunoo                      |    212K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hnn.txt)               |
| `hns`               | Caribbean Hindustani         |    312K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hns.txt)               |
| `ho`                | Hiri Motu                    |    240K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ho.txt)                |
| `hot`               | Hote                         |    222K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hot.txt)               |
| `hr`                | Croatian                     |  8,188K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hr.txt)                |
| `ht`                | Haitian                      |  1,101K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ht.txt)                |
| `hto`               | Minica Huitoto               |    182K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hto.txt)               |
| `hu`                | Hungarian                    |    600K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hu.txt)                |
| `hub`               | Huambisa                     |    160K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hub.txt)               |
| `hui`               | Huli                         |    232K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hui.txt)               |
| `hus`               | Huastec                      |    236K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hus.txt)               |
| `huu`               | Murui Huitoto                |    165K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/huu.txt)               |
| `huv`               | San Mateo Del Mar Huave      |    197K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/huv.txt)               |
| `hvn`               | Sabu                         |    312K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hvn.txt)               |
| `hy`                | Armenian                     | 25,972K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hy.txt)                |
| `ian`               | Iatmul                       |    224K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ian.txt)               |
| `iba`               | Iban                         |    179K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/iba.txt)               |
| `icr`               | Islander Creole English      |    248K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/icr.txt)               |
| `id`                | Indonesian                   |  6,634K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/id.txt)                |
| `ifa`               | Amganad Ifugao               |    810K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ifa.txt)               |
| `ifb`               | Batad Ifugao                 |    835K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ifb.txt)               |
| `ife`               | Ifè                          |    300K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ife.txt)               |
| `ifk`               | Tuwali Ifugao                |    214K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ifk.txt)               |
| `ifu`               | Mayoyao Ifugao               |    258K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ifu.txt)               |
| `ify`               | Keley-I Kallahan             |    863K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ify.txt)               |
| `ig`                | Igbo                         |     13K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ig.txt)                |
| `ign`               | Ignaciano                    |    161K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ign.txt)               |
| `ik`                | Inupiaq                      |     96K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ik.txt)                |
| `ilo`               | Iloko                        |    169K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ilo.txt)               |
| `imo`               | Imbongu                      |    280K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/imo.txt)               |
| `inb`               | Inga                         |    151K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/inb.txt)               |
| `ino`               | Inoke-Yate                   |    236K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ino.txt)               |
| `iou`               | Tuma-Irumu                   |    225K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/iou.txt)               |
| `ipi`               | Ipili                        |    312K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ipi.txt)               |
| `iri`               | Irigwe                       |    243K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/iri.txt)               |
| `irk`               | Iraqw                        |    184K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/irk.txt)               |
| `iry`               | Iraya                        |    205K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/iry.txt)               |
| `it`                | Italian                      | 13,569K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/it.txt)                |
| `itv`               | Itawit                       |    242K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/itv.txt)               |
| `iu`                | Inuktitut                    |     98K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/iu.txt)                |
| `iws`               | Sepik Iwam                   |    307K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/iws.txt)               |
| `izr`               | Izere                        |    216K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/izr.txt)               |
| `izz`               | Izii                         |    908K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/izz.txt)               |
| `ja`                | Japanese                     |  2,116K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ja.txt)                |
| `jac`               | Popti'                       |    221K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/jac.txt)               |
| `jae`               | Yabem                        |    186K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/jae.txt)               |
| `jam`               | Jamaican Creole English      |    254K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/jam.txt)               |
| `jbu`               | Jukun Takum                  |    264K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/jbu.txt)               |
| `jic`               | Tol                          |    285K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/jic.txt)               |
| `jiv`               | Shuar                        |    134K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/jiv.txt)               |
| `jmc`               | Machame                      |    150K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/jmc.txt)               |
| `jun`               | Juang                        |    178K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/jun.txt)               |
| `jv`                | Javanese                     |    177K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/jv.txt)                |
| `jvn`               | Caribbean Javanese           |    211K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/jvn.txt)               |
| `ka`                | Georgian                     |  4,978K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ka.txt)                |
| `kaa`               | Kara-Kalpak                  |    135K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kaa.txt)               |
| `kab-Arab`          | Kabyle (Arabic)              |    715K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kab-Arab.txt)          |
| `kab-Tfng`          | Kabyle (Tifinagh)            |  1,338K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kab-Tfng.txt)          |
| `kab`               | Kabyle                       |     66K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kab.txt)               |
| `kac`               | Kachin                       |  1,057K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kac.txt)               |
| `kao`               | Xaasongaxango                |    205K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kao.txt)               |
| `kaq`               | Capanahua                    |    164K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kaq.txt)               |
| `kbh`               | Camsá                        |    193K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kbh.txt)               |
| `kbm`               | Iwal                         |    298K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kbm.txt)               |
| `kbp`               | Kabiyè                       |    571K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kbp.txt)               |
| `kbq`               | Kamano                       |    156K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kbq.txt)               |
| `kbr`               | Kafa                         |    147K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kbr.txt)               |
| `kcg`               | Tyap                         |    279K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kcg.txt)               |
| `kdc`               | Kutu                         |    140K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kdc.txt)               |
| `kdi`               | Kumam                        |    195K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kdi.txt)               |
| `kdj`               | Karamojong                   |    163K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kdj.txt)               |
| `kdn`               | Kunda                        |    144K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kdn.txt)               |
| `kek`               | Kekchí                       |    406K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kek.txt)               |
| `ken`               | Kenyang                      |    200K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ken.txt)               |
| `keo`               | Kakwa                        |    215K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/keo.txt)               |
| `ker`               | Kera                         |    267K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ker.txt)               |
| `kew`               | West Kewa                    |    247K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kew.txt)               |
| `kez`               | Kukele                       |    173K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kez.txt)               |
| `kgf`               | Kube                         |    175K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kgf.txt)               |
| `kgr`               | Abun                         |    356K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kgr.txt)               |
| `khz`               | Keapara                      |    196K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/khz.txt)               |
| `kia`               | Kim                          |    525K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kia.txt)               |
| `kij`               | Kilivila                     |    155K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kij.txt)               |
| `kj`                | Kuanyama                     |  1,474K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kj.txt)                |
| `kjb`               | Q'anjob'al                   |    263K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kjb.txt)               |
| `kje`               | Kisar                        |    235K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kje.txt)               |
| `kjh`               | Khakas                       |    128K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kjh.txt)               |
| `kjs`               | East Kewa                    |    251K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kjs.txt)               |
| `kk`                | Kazakh                       |    642K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kk.txt)                |
| `kki`               | Kagulu                       |    125K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kki.txt)               |
| `kkj`               | Kako                         |    263K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kkj.txt)               |
| `kln`               | Kalenjin                     |    149K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kln.txt)               |
| `km`                | Khmer                        | 29,110K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/km.txt)                |
| `kma`               | Konni                        |    230K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kma.txt)               |
| `kmg`               | Kâte                         |    127K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kmg.txt)               |
| `kmo`               | Kwoma                        |    213K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kmo.txt)               |
| `kms`               | Kamasau                      |    293K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kms.txt)               |
| `kmu`               | Kanite                       |    214K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kmu.txt)               |
| `kn`                | Kannada                      |    126K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kn.txt)                |
| `kne`               | Kankanaey                    |    230K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kne.txt)               |
| `knf`               | Mankanya                     |    164K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/knf.txt)               |
| `knj`               | Western Kanjobal             |  1,350K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/knj.txt)               |
| `knk`               | Kuranko                      |    228K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/knk.txt)               |
| `kno`               | Kono                         |    360K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kno.txt)               |
| `knv`               | Tabo                         |    243K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/knv.txt)               |
| `kog`               | Cogui                        |    189K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kog.txt)               |
| `kpf`               | Komba                        |    174K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kpf.txt)               |
| `kpg`               | Kapingamarangi               |    967K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kpg.txt)               |
| `kpr`               | Korafe-Yegha                 |    262K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kpr.txt)               |
| `kpw`               | Kobon                        |    288K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kpw.txt)               |
| `kpx`               | Mountain Koiali              |    190K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kpx.txt)               |
| `kpz`               | Kupsabiny                    |    166K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kpz.txt)               |
| `kqc`               | Doromu-Koki                  |    209K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kqc.txt)               |
| `kqe`               | Kalagan                      |    241K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kqe.txt)               |
| `kqp`               | Kimré                        |    254K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kqp.txt)               |
| `kqw`               | Kandas                       |    201K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kqw.txt)               |
| `kqy`               | Koorete                      |    156K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kqy.txt)               |
| `krc`               | Karachay-Balkar              |    132K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/krc.txt)               |
| `kri`               | Krio                         |    256K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kri.txt)               |
| `krj`               | Kinaray-A                    |    228K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/krj.txt)               |
| `kru`               | Kurukh                       |    182K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kru.txt)               |
| `ksd`               | Kuanua                       |    228K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ksd.txt)               |
| `ksr`               | Borong                       |    233K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ksr.txt)               |
| `ktb`               | Kambaata                     |    113K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ktb.txt)               |
| `ktj`               | Plapo Krumen                 |    356K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ktj.txt)               |
| `kto`               | Kuot                         |    286K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kto.txt)               |
| `ku`                | Kurdish                      |  2,479K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ku.txt)                |
| `kub`               | Kutep                        |    281K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kub.txt)               |
| `kud`               | ‘Auhelawa                    |    167K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kud.txt)               |
| `kue`               | Kuman (Papua New Guinea)     |    230K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kue.txt)               |
| `kum`               | Kumyk                        |    142K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kum.txt)               |
| `kup`               | Kunimaipa                    |    279K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kup.txt)               |
| `kus`               | Kusaal                       |    200K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kus.txt)               |
| `kv`                | Komi                         |    122K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kv.txt)                |
| `kvn`               | Border Kuna                  |    212K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kvn.txt)               |
| `kwf`               | Kwara'ae                     |    296K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kwf.txt)               |
| `kwi`               | Awa-Cuaiquer                 |    165K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kwi.txt)               |
| `kwj`               | Kwanga                       |    290K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kwj.txt)               |
| `kxc`               | Konso                        |    148K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kxc.txt)               |
| `kxm`               | Northern Khmer               |    257K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kxm.txt)               |
| `ky`                | Kyrgyz                       | 18,597K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ky.txt)                |
| `kyc`               | Kyaka                        |    220K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kyc.txt)               |
| `kyf`               | Kouya                        |    215K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kyf.txt)               |
| `kyg`               | Keyagana                     |    190K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kyg.txt)               |
| `kyq`               | Kenga                        |    250K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kyq.txt)               |
| `kyu`               | Western Kayah                |    466K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kyu.txt)               |
| `kyz`               | Kayabí                       |    324K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kyz.txt)               |
| `kze`               | Kosena                       |    164K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kze.txt)               |
| `kzf`               | Da'a Kaili                   |    213K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kzf.txt)               |
| `kzj`               | Coastal Kadazan              |    215K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kzj.txt)               |
| `la`                | Latin                        |     48K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/la.txt)                |
| `laj`               | Lango                        |    175K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/laj.txt)               |
| `las`               | Lama                         |    235K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/las.txt)               |
| `law`               | Lauje                        |    262K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/law.txt)               |
| `lb`                | Luxembourgish                |  5,173K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lb.txt)                |
| `lcm`               | Tungag                       |    239K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lcm.txt)               |
| `lee`               | Lyélé                        |    257K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lee.txt)               |
| `lef`               | Lelemi                       |    211K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lef.txt)               |
| `lem`               | Nomaande                     |    249K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lem.txt)               |
| `leu`               | Kara (Papua New Guinea)      |    255K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/leu.txt)               |
| `lew`               | Ledo Kaili                   |    198K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lew.txt)               |
| `lex`               | Luang                        |    271K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lex.txt)               |
| `lgg`               | Lugbara                      |    188K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lgg.txt)               |
| `lhu`               | Lahu                         |    352K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lhu.txt)               |
| `lia`               | West-Central Limba           |    247K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lia.txt)               |
| `lid`               | Nyindrou                     |    308K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lid.txt)               |
| `lif`               | Limbu                        |    138K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lif.txt)               |
| `lip`               | Sekpele                      |    214K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lip.txt)               |
| `lis`               | Lisu                         |    304K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lis.txt)               |
| `ljp`               | Lampung Api                  |    188K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ljp.txt)               |
| `lln`               | Lele                         |    291K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lln.txt)               |
| `lme`               | Pévé                         |    245K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lme.txt)               |
| `lmk`               | Lamkang                      |    217K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lmk.txt)               |
| `lnd`               | Lundayeh                     |    670K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lnd.txt)               |
| `lo`                | Lao                          |  4,384K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lo.txt)                |
| `lob`               | Lobi                         |    192K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lob.txt)               |
| `loe`               | Saluan                       |    220K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/loe.txt)               |
| `lok`               | Loko                         |    264K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lok.txt)               |
| `lon`               | Malawi Lomwe                 |    137K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lon.txt)               |
| `lsi`               | Lashi                        |  1,077K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lsi.txt)               |
| `lsm`               | Saamia                       |    156K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lsm.txt)               |
| `lt`                | Lithuanian                   | 39,575K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lt.txt)                |
| `luc`               | Aringa                       |    242K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/luc.txt)               |
| `lus`               | Lushai                       |    204K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lus.txt)               |
| `lv`                | Latvian                      |  1,020K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lv.txt)                |
| `lwo`               | Luwo                         |    255K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lwo.txt)               |
| `maa`               | San Jerónimo Tecóatl Mazatec |    487K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/maa.txt)               |
| `mad`               | Madurese                     |    706K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mad.txt)               |
| `mag`               | Magahi                       |    193K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mag.txt)               |
| `mai`               | Maithili                     |    211K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mai.txt)               |
| `maj`               | Jalapa De Díaz Mazatec       |    188K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/maj.txt)               |
| `mak`               | Makasar                      |    179K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mak.txt)               |
| `mam`               | Mam                          |    834K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mam.txt)               |
| `maw`               | Mampruli                     |    251K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/maw.txt)               |
| `maz`               | Central Mazahua              |    286K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/maz.txt)               |
| `mbb`               | Western Bukidnon Manobo      |    278K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mbb.txt)               |
| `mbc`               | Macushi                      |    221K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mbc.txt)               |
| `mbh`               | Mangseng                     |    321K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mbh.txt)               |
| `mbt`               | Matigsalug Manobo            |    226K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mbt.txt)               |
| `mca`               | Maca                         |    208K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mca.txt)               |
| `mcb`               | Machiguenga                  |    132K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mcb.txt)               |
| `mcd`               | Sharanahua                   |    200K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mcd.txt)               |
| `mco`               | Coatlán Mixe                 |    217K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mco.txt)               |
| `mcp`               | Makaa                        |    237K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mcp.txt)               |
| `mcq`               | Ese                          |    158K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mcq.txt)               |
| `mcu`               | Cameroon Mambila             |    260K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mcu.txt)               |
| `mda`               | Mada                         |    312K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mda.txt)               |
| `mdy`               | Male                         |    589K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mdy.txt)               |
| `med`               | Melpa                        |    283K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/med.txt)               |
| `mee`               | Mengen                       |    301K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mee.txt)               |
| `mej`               | Meyah                        |    323K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mej.txt)               |
| `mek`               | Mekeo                        |    234K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mek.txt)               |
| `men`               | Mende                        |    210K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/men.txt)               |
| `meq`               | Merey                        |    291K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/meq.txt)               |
| `meu`               | Motu                         |    175K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/meu.txt)               |
| `mfe`               | Morisyen                     |    172K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mfe.txt)               |
| `mfh`               | Matal                        |    238K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mfh.txt)               |
| `mfi`               | Wandala                      |    265K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mfi.txt)               |
| `mfk`               | North Mofu                   |    248K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mfk.txt)               |
| `mfq`               | Moba                         |    232K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mfq.txt)               |
| `mfy`               | Mayo                         |    167K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mfy.txt)               |
| `mfz`               | Mabaan                       |    237K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mfz.txt)               |
| `mg`                | Malagasy                     |  1,623K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mg.txt)                |
| `mgd`               | Moru                         |    192K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mgd.txt)               |
| `mgh`               | Makhuwa-Meetto               |    150K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mgh.txt)               |
| `mgo`               | Meta'                        |    251K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mgo.txt)               |
| `mh`                | Marshallese                  |    750K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mh.txt)                |
| `mhi`               | Ma'di                        |    192K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mhi.txt)               |
| `mhl`               | Mauwake                      |    235K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mhl.txt)               |
| `mhx`               | Maru                         |    291K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mhx.txt)               |
| `mhy`               | Ma'anyan                     |    190K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mhy.txt)               |
| `mi`                | Maori                        |  1,504K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mi.txt)                |
| `mib`               | Atatláhuca Mixtec            |    263K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mib.txt)               |
| `mif`               | Mofu-Gudur                   |    283K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mif.txt)               |
| `mil`               | Peñoles Mixtec               |    365K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mil.txt)               |
| `min`               | Minangkabau                  |    242K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/min.txt)               |
| `mio`               | Pinotepa Nacional Mixtec     |    288K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mio.txt)               |
| `miq`               | Mískito                      |    214K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/miq.txt)               |
| `mit`               | Southern Puebla Mixtec       |    273K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mit.txt)               |
| `mk`                | Macedonian                   | 10,422K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mk.txt)                |
| `mkl`               | Mokole                       |    230K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mkl.txt)               |
| `ml`                | Malayalam                    |    118K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ml.txt)                |
| `mlh`               | Mape                         |    235K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mlh.txt)               |
| `mlp`               | Bargam                       |    297K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mlp.txt)               |
| `mmo`               | Mangga Buang                 |    269K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mmo.txt)               |
| `mmx`               | Madak                        |    271K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mmx.txt)               |
| `mna`               | Mbula                        |    257K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mna.txt)               |
| `mnb`               | Muna                         |    151K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mnb.txt)               |
| `mnf`               | Mundani                      |    241K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mnf.txt)               |
| `mnw`               | Mon                          |  1,836K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mnw.txt)               |
| `moa`               | Mwan                         |    308K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/moa.txt)               |
| `mog`               | Mongondow                    |    220K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mog.txt)               |
| `mop`               | Mopán Maya                   |    296K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mop.txt)               |
| `mor`               | Moro                         |    152K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mor.txt)               |
| `mox`               | Molima                       |    222K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mox.txt)               |
| `mpg`               | Marba                        |    210K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mpg.txt)               |
| `mpm`               | Yosondúa Mixtec              |    336K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mpm.txt)               |
| `mps`               | Dadibi                       |  1,270K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mps.txt)               |
| `mpt`               | Mian                         |    256K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mpt.txt)               |
| `mpx`               | Misima-Panaeati              |    227K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mpx.txt)               |
| `mqb`               | Mbuko                        |    302K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mqb.txt)               |
| `mqj`               | Mamasa                       |    164K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mqj.txt)               |
| `mqn`               | Moronene                     |    164K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mqn.txt)               |
| `mr`                | Marathi                      | 16,594K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mr.txt)                |
| `mrw`               | Maranao                      |    912K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mrw.txt)               |
| `ms`                | Malay                        |    659K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ms.txt)                |
| `msm`               | Agusan Manobo                |    225K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/msm.txt)               |
| `msy`               | Aruamu                       |    229K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/msy.txt)               |
| `mt`                | Maltese                      |  3,331K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mt.txt)                |
| `mta`               | Cotabato Manobo              |    262K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mta.txt)               |
| `mti`               | Maiwa (Papua New Guinea)     |    166K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mti.txt)               |
| `mtj`               | Moskona                      |    321K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mtj.txt)               |
| `mto`               | Totontepec Mixe              |    233K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mto.txt)               |
| `mtp`               | Wichí Lhamtés Nocten         |    183K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mtp.txt)               |
| `muh`               | Mündü                        |    392K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/muh.txt)               |
| `mur`               | Murle                        |    210K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mur.txt)               |
| `mux`               | Bo-Ung                       |    363K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mux.txt)               |
| `muy`               | Muyang                       |    265K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/muy.txt)               |
| `mva`               | Manam                        |    231K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mva.txt)               |
| `mvp`               | Duri                         |    174K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mvp.txt)               |
| `mwv`               | Mentawai                     |    141K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mwv.txt)               |
| `mxb`               | Tezoatlán Mixtec             |    281K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mxb.txt)               |
| `mxt`               | Jamiltepec Mixtec            |    267K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mxt.txt)               |
| `my`                | Burmese                      |  1,007K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/my.txt)                |
| `my-t-d0-zawgyi`    | Burmese (Zawgyi encoding)    |    593K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/my-t-d0-zawgyi.txt)    |
| `myb`               | Mbay                         |    192K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/myb.txt)               |
| `myk`               | Mamara Senoufo               |    272K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/myk.txt)               |
| `myv`               | Erzya                        |    143K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/myv.txt)               |
| `myw`               | Muyuw                        |    150K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/myw.txt)               |
| `myx`               | Masaaba                      |    164K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/myx.txt)               |
| `myy`               | Macuna                       |    245K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/myy.txt)               |
| `mza`               | Santa María Zacatepec Mixtec |    316K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mza.txt)               |
| `mzi`               | Ixcatlán Mazatec             |    190K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mzi.txt)               |
| `mzk`               | Nigeria Mambila              |    283K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mzk.txt)               |
| `mzm`               | Mumuye                       |    265K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mzm.txt)               |
| `naf`               | Nabak                        |    220K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/naf.txt)               |
| `nak`               | Nakanai                      |    333K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nak.txt)               |
| `nan-Latn`          | Min Nan Chinese (Latin)      |    231K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nan-Latn.txt)          |
| `nas`               | Naasioi                      |    168K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nas.txt)               |
| `nca`               | Iyo                          |    203K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nca.txt)               |
| `nch`               | Central Huasteca Nahuatl     |    195K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nch.txt)               |
| `ncj`               | Northern Puebla Nahuatl      |    164K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ncj.txt)               |
| `ncu`               | Chumburung                   |    312K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ncu.txt)               |
| `ndj`               | Ndamba                       |    141K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ndj.txt)               |
| `ndy`               | Lutos                        |    216K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ndy.txt)               |
| `ndz`               | Ndogo                        |    350K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ndz.txt)               |
| `neb`               | Toura                        |    326K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/neb.txt)               |
| `new`               | Newari                       |    150K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/new.txt)               |
| `nfr`               | Nafaanra                     |    233K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nfr.txt)               |
| `ngp`               | Ngulu                        |    149K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ngp.txt)               |
| `nho`               | Takuu                        |    309K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nho.txt)               |
| `nhu`               | Noone                        |    270K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nhu.txt)               |
| `nhw`               | Western Huasteca Nahuatl     |    194K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nhw.txt)               |
| `nhy`               | Northern Oaxaca Nahuatl      |    185K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nhy.txt)               |
| `nia`               | Nias                         |    182K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nia.txt)               |
| `nii`               | Nii                          |    316K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nii.txt)               |
| `nij`               | Ngaju                        |    194K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nij.txt)               |
| `nim`               | Nilamba                      |    117K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nim.txt)               |
| `nin`               | Ninzo                        |    267K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nin.txt)               |
| `nkf`               | Inpui Naga                   |    197K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nkf.txt)               |
| `nko`               | Nkonya                       |    168K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nko.txt)               |
| `nl`                | Dutch                        | 58,357K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nl.txt)                |
| `nlc`               | Nalca                        |    241K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nlc.txt)               |
| `nmz`               | Nawdm                        |    209K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nmz.txt)               |
| `nnb`               | Nande                        |    127K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nnb.txt)               |
| `nnq`               | Ngindo                       |    137K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nnq.txt)               |
| `nnw`               | Southern Nuni                |    291K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nnw.txt)               |
| `noa`               | Woun Meu                     |    275K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/noa.txt)               |
| `nog`               | Nogai                        |    104K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nog.txt)               |
| `nop`               | Numanggang                   |    183K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nop.txt)               |
| `not`               | Nomatsiguenga                |    141K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/not.txt)               |
| `nou`               | Ewage-Notu                   |    266K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nou.txt)               |
| `npl`               | Southeastern Puebla Nahuatl  |    148K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/npl.txt)               |
| `npy`               | Napu                         |    192K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/npy.txt)               |
| `nsn`               | Nehan                        |    248K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nsn.txt)               |
| `nsu`               | Sierra Negra Nahuatl         |    170K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nsu.txt)               |
| `ntm`               | Nateni                       |    229K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ntm.txt)               |
| `ntp`               | Northern Tepehuan            |    173K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ntp.txt)               |
| `ntr`               | Delo                         |    272K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ntr.txt)               |
| `nuj`               | Nyole                        |    151K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nuj.txt)               |
| `nus`               | Nuer                         |    195K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nus.txt)               |
| `nvm`               | Namiae                       |    290K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nvm.txt)               |
| `nwb`               | Nyabwa                       |    316K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nwb.txt)               |
| `nwi`               | Southwest Tanna              |    230K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nwi.txt)               |
| `ny`                | Nyanja                       |    356K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ny.txt)                |
| `nyf`               | Giryama                      |    169K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nyf.txt)               |
| `nyn`               | Nyankole                     |    120K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nyn.txt)               |
| `nyo`               | Nyoro                        |    120K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nyo.txt)               |
| `nyy`               | Nyakyusa-Ngonde              |    138K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nyy.txt)               |
| `nzi`               | Nzima                        |    201K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nzi.txt)               |
| `obo`               | Obo Manobo                   |    266K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/obo.txt)               |
| `oc`                | Occitan                      |  2,706K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/oc.txt)                |
| `oku`               | Oku                          |    239K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/oku.txt)               |
| `okv`               | Orokaiva                     |    212K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/okv.txt)               |
| `old`               | Mochi                        |    151K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/old.txt)               |
| `ong`               | Olo                          |    284K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ong.txt)               |
| `opm`               | Oksapmin                     |    332K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/opm.txt)               |
| `or`                | Oriya                        |    175K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/or.txt)               |
| `os`                | Ossetic                      |    135K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/os.txt)               |
| `osa`               | Osage                        |      3K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/osa.txt)               |
| `otd`               | Ot Danum                     |    187K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/otd.txt)               |
| `ote`               | Mezquital Otomi              |    251K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ote.txt)               |
| `ozm`               | Koonzime                     |    267K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ozm.txt)               |
| `pa`                | Punjabi                      | 59,990K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pa.txt)                |
| `pab`               | Parecís                      |    156K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pab.txt)               |
| `pad`               | Paumarí                      |    242K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pad.txt)               |
| `pag`               | Pangasinan                   |    177K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pag.txt)               |
| `pah`               | Tenharim                     |    268K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pah.txt)               |
| `pam`               | Pampanga                     |    196K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pam.txt)               |
| `pau`               | Palauan                      |    255K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pau.txt)               |
| `pbc`               | Patamona                     |    181K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pbc.txt)               |
| `pbi`               | Parkwa                       |    272K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pbi.txt)               |
| `pck`               | Paite Chin                   |    770K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pck.txt)               |
| `pcm`               | Nigerian Pidgin              |    315K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pcm.txt)               |
| `pez`               | Eastern Penan                |    235K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pez.txt)               |
| `pib`               | Yine                         |    114K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pib.txt)               |
| `pir`               | Piratapuyo                   |    229K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pir.txt)               |
| `pis`               | Pijin                        |    263K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pis.txt)               |
| `pjt`               | Pitjantjatjara               |    237K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pjt.txt)               |
| `pkb`               | Pokomo                       |    166K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pkb.txt)               |
| `pl`                | Polish                       |  7,148K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pl.txt)                |
| `plw`               | Brooke's Point Palawano      |    203K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/plw.txt)               |
| `pmf`               | Pamona                       |    307K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pmf.txt)               |
| `pny`               | Pinyin                       |    247K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pny.txt)               |
| `poh`               | Poqomchi'                    |    266K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/poh.txt)               |
| `poi`               | Highland Popoluca            |    179K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/poi.txt)               |
| `poy`               | Pogolo                       |    147K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/poy.txt)               |
| `ppk`               | Uma                          |    220K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ppk.txt)               |
| `ppo`               | Folopa                       |    258K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ppo.txt)               |
| `prf`               | Paranan                      |    203K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/prf.txt)               |
| `prk`               | Parauk                       |  1,026K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/prk.txt)               |
| `ps`                | Pashto                       |  7,343K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ps.txt)                |
| `pss`               | Kaulong                      |    326K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pss.txt)               |
| `pt`                | Portuguese                   | 20,891K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pt.txt)                |
| `pt-PT`             | Portuguese (Portugal)        |    666K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pt-PT.txt)             |
| `ptp`               | Patep                        |    294K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ptp.txt)               |
| `ptu`               | Bambam                       |    194K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ptu.txt)               |
| `pwg`               | Gapapaiwa                    |    208K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pwg.txt)               |
| `pww`               | Pwo Northern Karen           |    345K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pww.txt)               |
| `pxm`               | Quetzaltepec Mixé            |    720K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pxm.txt)               |
| `qu`                | Quechua                      |    580K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qu.txt)                |
| `qub`               | Huallaga Huánuco Quechua     |    122K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qub.txt)               |
| `quc`               | K'iche'                      |    207K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/quc.txt)               |
| `quf`               | Lambayeque Quechua           |    161K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/quf.txt)               |
| `quh`               | South Bolivian Quechua       |    623K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/quh.txt)               |
| `qul`               | North Bolivian Quechua       |    140K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qul.txt)               |
| `qup`               | Southern Pastaza Quechua     |    177K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qup.txt)               |
| `quw`               | Tena Lowland Quichua         |    116K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/quw.txt)               |
| `quy`               | Ayacucho Quechua             |    106K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/quy.txt)               |
| `qvc`               | Cajamarca Quechua            |    166K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qvc.txt)               |
| `qve`               | Eastern Apurímac Quechua     |    168K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qve.txt)               |
| `qvi`               | Imbabura Highland Quichua    |    146K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qvi.txt)               |
| `qvm`               | Margos-Yarowilca-Lauricocha Quechua |    132K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qvm.txt)        |
| `qvn`               | North Junín Quechua          |    139K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qvn.txt)               |
| `qvo`               | Napo Lowland Quechua         |    117K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qvo.txt)               |
| `qvs`               | San Martín Quechua           |    153K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qvs.txt)               |
| `qvw`               | Huaylla Wanca Quechua        |    111K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qvw.txt)               |
| `qvz`               | Northern Pastaza Quichua     |    157K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qvz.txt)               |
| `qwh`               | Huaylas Ancash Quechua       |    128K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qwh.txt)               |
| `qxh`               | Panao Huánuco Quechua        |    123K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qxh.txt)               |
| `qxl`               | Salasaca Highland Quichua    |    127K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qxl.txt)               |
| `qxn`               | Northern Conchucos Ancash Quechua |    150K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qxn.txt)          |
| `qxo`               | Southern Conchucos Ancash Quechua |    136K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qxo.txt)          |
| `qxr`               | Cañar Highland Quichua       |    509K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/qxr.txt)               |
| `rai`               | Ramoaaina                    |    273K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rai.txt)               |
| `raj`               | Malvi                        |    198K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/raj.txt)               |
| `rav`               | Sampang                      |    138K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rav.txt)               |
| `rej`               | Rejang                       |    178K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rej.txt)               |
| `rim`               | Nyaturu                      |    151K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rim.txt)               |
| `rm-puter`          | Romansh (Puter)              |  1,068K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-puter.txt)          |
| `rm-rumgr`          | Romansh (Grischun)           |  4,794K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-rumgr.txt)          |
| `rm-surmiran`       | Romansh (Surmiran)           |  2,540K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-surmiran.txt)       |
| `rm-sursilv`        | Romansh (Sursilvan)          | 11,678K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-sursilv.txt)        |
| `rm-sutsilv`        | Romansh (Sutsilvan)          |  1,007K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-sutsilv.txt)        |
| `rm-vallader`       | Romansh (Vallader)           |  5,560K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-vallader.txt)       |
| `rmc`               | Carpathian Romani            |    170K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rmc.txt)               |
| `rmo`               | Sinte Romani                 |    228K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rmo.txt)               |
| `rn`                | Rundi                        |    120K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rn.txt)                |
| `rnl`               | Ranglong                     |    221K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rnl.txt)               |
| `ro`                | Romanian                     | 13,962K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ro.txt)                |
| `ro-MD`             | Moldavian                    |  2,694K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ro-MD.txt)             |
| `rom`               | Vlax Romani                  |    186K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rom.txt)               |
| `roo`               | Rotokas                      |    292K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/roo.txt)               |
| `rro`               | Waima                        |    177K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rro.txt)               |
| `ru`                | Russian                      | 40,987K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ru.txt)                |
| `ruf`               | Luguru                       |    135K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ruf.txt)               |
| `rug`               | Roviana                      |    956K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rug.txt)               |
| `rw`                | Kinyarwanda                  |    605K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rw.txt)                |
| `rwo`               | Rawa                         |    261K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rwo.txt)               |
| `sab`               | Buglere                      |    405K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sab.txt)               |
| `sah`               | Sakha                        |  2,457K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sah.txt)               |
| `sas`               | Sasak                        |    196K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sas.txt)               |
| `sat`               | Santali                      |    149K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sat.txt)               |
| `sba`               | Ngambay                      |    246K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sba.txt)               |
| `sbl`               | Botolan Sambal               |    251K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sbl.txt)               |
| `sck`               | Sadri                        |    189K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sck.txt)               |
| `sda`               | Toraja-Sa'dan                |    154K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sda.txt)               |
| `seh`               | Sena                         |    155K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/seh.txt)               |
| `sey`               | Secoya                       |    163K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sey.txt)               |
| `sg`                | Sango                        |    265K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sg.txt)                |
| `sgb`               | Mag-antsi Ayta               |    233K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sgb.txt)               |
| `sgw`               | Sebat Bet Gurage             |    116K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sgw.txt)               |
| `sgz`               | Sursurunga                   |    327K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sgz.txt)               |
| `shk`               | Shilluk                      |    189K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/shk.txt)               |
| `shn`               | Shan                         |  1,435K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/shn.txt)               |
| `shp`               | Shipibo-Conibo               |    169K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/shp.txt)               |
| `si`                | Sinhala                      |  1,046K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/si.txt)                |
| `sig`               | Paasaal                      |    277K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sig.txt)               |
| `sil`               | Tumulung Sisaala             |    256K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sil.txt)               |
| `sim`               | Mende (Papua New Guinea)     |    273K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sim.txt)               |
| `sja`               | Epena                        |    194K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sja.txt)               |
| `sk`                | Slovak                       | 70,933K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sk.txt)                |
| `sl`                | Slovenian                    | 10,975K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sl.txt)                |
| `sld`               | Sissala                      |    206K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sld.txt)               |
| `sll`               | Salt-Yui                     |    264K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sll.txt)               |
| `sm`                | Samoan                       |    248K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sm.txt)                |
| `smt`               | Simte                        |    177K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/smt.txt)               |
| `sn`                | Shona                        |  2,542K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sn.txt)                |
| `snc`               | Sinaugoro                    |    216K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/snc.txt)               |
| `snn`               | Siona                        |    222K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/snn.txt)               |
| `snp`               | Siane                        |    237K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/snp.txt)               |
| `snw`               | Selee                        |    212K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/snw.txt)               |
| `sny`               | Saniyo-Hiyewe                |    348K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sny.txt)               |
| `so`                | Somali                       |    874K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/so.txt)                |
| `soq`               | Kanasi                       |    213K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/soq.txt)               |
| `soy`               | Miyobe                       |    205K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/soy.txt)               |
| `spl`               | Selepet                      |    244K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/spl.txt)               |
| `spp`               | Supyire Senoufo              |    251K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/spp.txt)               |
| `sps`               | Saposa                       |    324K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sps.txt)               |
| `sq`                | Albanian                     | 10,104K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sq.txt)                |
| `sr`                | Serbian                      |  4,785K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sr.txt)                |
| `sr-Latn`           | Serbian (Latin)              | 10,143K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sr-Latn.txt)           |
| `sri`               | Siriano                      |    166K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sri.txt)               |
| `srm`               | Saramaccan                   |    369K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/srm.txt)               |
| `srn`               | Sranan Tongo                 |    232K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/srn.txt)               |
| `ssd`               | Siroi                        |    210K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ssd.txt)               |
| `ssg`               | Seimat                       |    221K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ssg.txt)               |
| `ssx`               | Samberigi                    |    233K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ssx.txt)               |
| `stn`               | Owa                          |    263K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/stn.txt)               |
| `su`                | Sundanese                    |    172K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/su.txt)                |
| `sua`               | Sulka                        |    458K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sua.txt)               |
| `sue`               | Suena                        |    227K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sue.txt)               |
| `sur`               | Mwaghavul                    |    261K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sur.txt)               |
| `sus`               | Susu                         |    205K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sus.txt)               |
| `suz`               | Sunwar                       |    732K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/suz.txt)               |
| `sv`                | Swedish                      | 33,633K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sv.txt)                |
| `sw`                | Swahili                      |  8,817K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sw.txt)                |
| `swp`               | Suau                         |    175K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/swp.txt)               |
| `sxn`               | Sangir                       |    209K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sxn.txt)               |
| `ta`                | Tamil                        |  1,413K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ta.txt)                |
| `tab`               | Tabassaran                   |    132K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tab.txt)               |
| `taj`               | Eastern Tamang               |    169K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/taj.txt)               |
| `tap`               | Taabwa                       |    145K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tap.txt)               |
| `taq`               | Tamasheq                     |    218K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/taq.txt)               |
| `tav`               | Tatuyo                       |    256K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tav.txt)               |
| `taw`               | Tai                          |    268K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/taw.txt)               |
| `tbc`               | Takia                        |    278K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tbc.txt)               |
| `tbg`               | North Tairora                |    235K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tbg.txt)               |
| `tbo`               | Tawala                       |    198K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tbo.txt)               |
| `tby`               | Tabaru                       |    226K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tby.txt)               |
| `tbz`               | Ditammari                    |    692K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tbz.txt)               |
| `tca`               | Ticuna                       |    251K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tca.txt)               |
| `tcc`               | Datooga                      |    135K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tcc.txt)               |
| `te`                | Telugu                       |    574K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/te.txt)                |
| `ted`               | Tepo Krumen                  |    346K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ted.txt)               |
| `tem`               | Timne                        |    190K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tem.txt)               |
| `teo`               | Teso                         |    118K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/teo.txt)               |
| `ter`               | Tereno                       |    187K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ter.txt)               |
| `tfr`               | Teribe                       |    228K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tfr.txt)               |
| `tgo`               | Sudest                       |    216K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tgo.txt)               |
| `tgp`               | Tangoa                       |    228K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tgp.txt)               |
| `thk`               | Tharaka                      |    150K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/thk.txt)               |
| `ti`                | Tigrinya                     |    803K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ti.txt)                |
| `tif`               | Tifal                        |    413K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tif.txt)               |
| `tih`               | Timugon Murut                |    879K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tih.txt)               |
| `tik`               | Tikar                        |    264K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tik.txt)               |
| `tim`               | Timbe                        |    206K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tim.txt)               |
| `tk`                | Turkmen                      |    516K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tk.txt)                |
| `tlb`               | Tobelo                       |    209K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tlb.txt)               |
| `tlf`               | Telefol                      |    422K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tlf.txt)               |
| `tlj`               | Talinga-Bwisi                |    159K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tlj.txt)               |
| `tmc`               | Tumak                        |    245K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tmc.txt)               |
| `tna`               | Tacana                       |    216K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tna.txt)               |
| `tnr`               | Ménik                        |    254K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tnr.txt)               |
| `to`                | Tonga                        |  1,214K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/to.txt)                |
| `tob`               | Toba                         |    229K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tob.txt)               |
| `toc`               | Coyutla Totonac              |    218K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/toc.txt)               |
| `toh`               | Gitonga                      |    194K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/toh.txt)               |
| `top`               | Papantla Totonac             |    168K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/top.txt)               |
| `tos`               | Highland Totonac             |    224K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tos.txt)               |
| `tpi`               | Tok Pisin                    |  8,049K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tpi.txt)               |
| `tpm`               | Tampulma                     |    892K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tpm.txt)               |
| `tpp`               | Pisaflores Tepehua           |    162K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tpp.txt)               |
| `tpt`               | Tlachichilco Tepehua         |    173K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tpt.txt)               |
| `tpz`               | Tinputz                      |    370K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tpz.txt)               |
| `tqo`               | Toaripi                      |    215K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tqo.txt)               |
| `tr`                | Turkish                      | 13,846K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tr.txt)                |
| `trs`               | Chicahuaxtla Triqui          |    287K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/trs.txt)               |
| `tsz`               | Purepecha                    |    129K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tsz.txt)               |
| `tt`                | Tatar                        |  1,356K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tt.txt)                |
| `ttc`               | Tektiteko                    |    231K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ttc.txt)               |
| `tte`               | Bwanabwana                   |    198K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tte.txt)               |
| `tue`               | Tuyuca                       |    141K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tue.txt)               |
| `tuf`               | Central Tunebo               |    237K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tuf.txt)               |
| `twb`               | Western Tawbuid              |    198K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/twb.txt)               |
| `twu`               | Termanu                      |    242K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/twu.txt)               |
| `txa`               | Tombonuo                     |    224K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/txa.txt)               |
| `txu`               | Kayapó                       |    354K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/txu.txt)               |
| `tyv`               | Tuvinian                     |    614K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tyv.txt)               |
| `tyz`               | Tày                          |    260K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tyz.txt)               |
| `tzh`               | Tzeltal                      |    901K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tzh.txt)               |
| `tzj`               | Tz'utujil                    |    245K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tzj.txt)               |
| `ubr`               | Ubir                         |    222K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ubr.txt)               |
| `ubu`               | Umbu-Ungu                    |    308K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ubu.txt)               |
| `udm`               | Udmurt                       |    135K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/udm.txt)               |
| `udu`               | Uduk                         |    287K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/udu.txt)               |
| `ug`                | Uyghur                       |  9,493K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ug.txt)                |
| `uk`                | Ukrainian                    | 12,921K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/uk.txt)                |
| `ur`                | Urdu                         |  3,622K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ur.txt)                |
| `ura`               | Urarina                      |    193K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ura.txt)               |
| `urb`               | Urubú-Kaapor                 |    347K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/urb.txt)               |
| `urk`               | Urak Lawoi'                  |    368K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/urk.txt)               |
| `ury`               | Orya                         |    301K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ury.txt)               |
| `usa`               | Usarufa                      |    171K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/usa.txt)               |
| `usp`               | Uspanteco                    |    228K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/usp.txt)               |
| `uvl`               | Lote                         |    277K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/uvl.txt)               |
| `uz`                | Uzbek                        |    131K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/uz.txt)                |
| `vag`               | Vagla                        |    221K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/vag.txt)               |
| `vec`               | Venetian                     |      2K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/vec.txt)               |
| `vec-u-sd-itpd`     | Venetian (Padua)             |    813K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/vec-u-sd-itpd.txt)     |
| `vec-u-sd-itts`     | Venetian (Trieste)           |     12K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/vec-u-sd-itts.txt)     |
| `vec-u-sd-itvr`     | Venetian (Verona)            |     16K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/vec-u-sd-itvr.txt)     |
| `vid`               | Vidunda                      |    151K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/vid.txt)               |
| `viv`               | Iduna                        |    220K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/viv.txt)               |
| `vmw`               | Makhuwa                      |    130K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/vmw.txt)               |
| `vun`               | Vunjo                        |    141K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/vun.txt)               |
| `vut`               | Vute                         |    206K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/vut.txt)               |
| `waj`               | Waffa                        |    236K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/waj.txt)               |
| `wap`               | Wapishana                    |    193K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wap.txt)               |
| `war`               | Waray                        |    208K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/war.txt)               |
| `way`               | Wayana                       |    143K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/way.txt)               |
| `wer`               | Weri                         |    209K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wer.txt)               |
| `wiu`               | Wiru                         |    232K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wiu.txt)               |
| `wlx`               | Wali                         |    847K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wlx.txt)               |
| `wmw`               | Mwani                        |    139K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wmw.txt)               |
| `wnc`               | Wantoat                      |    238K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wnc.txt)               |
| `wnu`               | Usan                         |    234K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wnu.txt)               |
| `wob`               | Wè Northern                  |    270K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wob.txt)               |
| `wos`               | Hanga Hundi                  |    264K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wos.txt)               |
| `wrs`               | Waris                        |    213K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wrs.txt)               |
| `wsk`               | Waskia                       |    239K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wsk.txt)               |
| `wuv`               | Wuvulu-Aua                   |    187K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wuv.txt)               |
| `wwa`               | Waama                        |    239K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wwa.txt)               |
| `xal`               | Kalmyk                       |    135K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xal.txt)               |
| `xav`               | Xavánte                      |    440K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xav.txt)               |
| `xed`               | Hdi                          |    229K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xed.txt)               |
| `xla`               | Kamula                       |    230K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xla.txt)               |
| `xog`               | Soga                         |    127K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xog.txt)               |
| `xrb`               | Eastern Karaboro             |    286K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xrb.txt)               |
| `xsb`               | Sambal                       |    244K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xsb.txt)               |
| `xsi`               | Sio                          |    319K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xsi.txt)               |
| `xsm`               | Kasem                        |    604K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xsm.txt)               |
| `xsr`               | Sherpa                       |    184K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xsr.txt)               |
| `xsu`               | Sanumá                       |    408K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xsu.txt)               |
| `xtd`               | Diuxi-Tilantongo Mixtec      |    277K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xtd.txt)               |
| `xtm`               | Magdalena Peñasco Mixtec     |    335K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xtm.txt)               |
| `xuo`               | Kuo                          |    306K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xuo.txt)               |
| `yaa`               | Yaminahua                    |    204K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yaa.txt)               |
| `yad`               | Yagua                        |    142K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yad.txt)               |
| `yal`               | Yalunka                      |    203K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yal.txt)               |
| `yam`               | Yamba                        |    277K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yam.txt)               |
| `yaz`               | Lokaa                        |    222K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yaz.txt)               |
| `yby`               | Yaweyuha                     |    219K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yby.txt)               |
| `ycn`               | Yucuna                       |    202K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ycn.txt)               |
| `yle`               | Yele                         |    298K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yle.txt)               |
| `yli`               | Angguruk Yali                |    221K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yli.txt)               |
| `yml`               | Iamalele                     |    245K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yml.txt)               |
| `yo`                | Yoruba                       |    270K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yo.txt)                |
| `yon`               | Yongkom                      |    202K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yon.txt)               |
| `yrb`               | Yareba                       |    184K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yrb.txt)               |
| `yre`               | Yaouré                       |    285K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yre.txt)               |
| `yss`               | Yessan-Mayo                  |    227K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yss.txt)               |
| `yua`               | Yucateco                     |    813K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yua.txt)               |
| `yuj`               | Karkar-Yuri                  |    258K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yuj.txt)               |
| `yut`               | Yopno                        |    227K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yut.txt)               |
| `yuw`               | Yau (Morobe Province)        |    243K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yuw.txt)               |
| `yva`               | Yawa                         |    250K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yva.txt)               |
| `zaa`               | Sierra de Juárez Zapotec     |    265K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zaa.txt)               |
| `zad`               | Cajonos Zapotec              |    180K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zad.txt)               |
| `zae`               | Yareni Zapotec               |    248K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zae.txt)               |
| `zap`               | Zapotec                      |    194K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zap.txt)               |
| `zas`               | Santo Domingo Albarradas Zapotec |184K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zas.txt)               |
| `zaw`               | Mitla Zapotec                |    157K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zaw.txt)               |
| `zca`               | Coatecas Altas Zapotec       |    236K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zca.txt)               |
| `zia`               | Zia                          |    242K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zia.txt)               |
| `ziw`               | Zigula                       |    140K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ziw.txt)               |
| `zlm`               | Malay                        |    664K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zlm.txt)               |
| `zne`               | Zande                        |    253K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zne.txt)               |
| `zpc`               | Choapan Zapotec              |    208K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zpc.txt)               |
| `zpi`               | Santa María Quiegolani Zapotec |  209K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zpi.txt)               |
| `zpq`               | Zoogocho Zapotec             |    208K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zpq.txt)               |
| `zpt`               | San Vicente Coatlán Zapotec  |    229K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zpt.txt)               |
| `zpz`               | Texmelucan Zapotec           |    281K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zpz.txt)               |
| `zyp`               | Zyphe Chin                   |    230K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zyp.txt)               |


¹ Downloadable files include counts for each token; to get raw text, run the crawler yourself. For breaking text into words, we use an [ICU word break iterator](http://userguide.icu-project.org/boundaryanalysis#TOC-Word-Boundary) and count all tokens whose break status is one of `UBRK_WORD_LETTER`, `UBRK_WORD_KANA`, or `UBRK_WORD_IDEO`.


## Running the Crawler

```sh
./corpuscrawler --language=yo --output=./corpus
```
