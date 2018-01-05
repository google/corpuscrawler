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



## Supported Languages

| IETF BCP47 Code     | Language                     |  Tokens¹                                                                            |
| :------------------ | :--------------------------- | ----------------------------------------------------------------------------------: |
| `aai`               | Arifama-Miniafia             |    181K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aai.txt)               |
| `aak`               | Ankave                       |    194K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aak.txt)               |
| `aby`               | Aneme Wake                   |    233K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aby.txt)               |
| `ace`               | Aceh/Acehnese                |    817K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ace.txt)               |
| `ae`                | Avestan                      |    129K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ae.txt)                |
| `ae-Latn`           | Avestan (Latin)              |    141K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ae-Latn.txt)           |
| `aey`               | Amele                        |    218K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aey.txt)               |
| `agd`               | Agarabi                      |    256K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/agd.txt)               |
| `agg`               | Angor                        |    214K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/agg.txt)               |
| `agm`               | Angaataha                    |    238K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/agm.txt)               |
| `akh`               | Akha                         |    408K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/akh.txt)               |
| `amm`               | Ama (Papua New Guinea)       |    246K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/amm.txt)               |
| `amp`               | Alamblak                     |    241K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/amp.txt)               |
| `am`                | Amharic                      |  2,170K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/am.txt)                |
| `aom`               | Ömie                         |    231K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aom.txt)               |
| `aon`               | Bumbita Arapesh              |    294K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aon.txt)               |
| `ape`               | Bukiyip                      |    294K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ape.txt)               |
| `apr`               | Arop-Lokep                   |    373K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/apr.txt)               |
| `apz`               | Safeyoka                     |    235K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/apz.txt)               |
| `ar`                | Arabic                       | 19,593K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ar.txt)                |
| `aso`               | Dano                         |    290K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/aso.txt)               |
| `ata`               | Pele-Ata                     |    248K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ata.txt)               |
| `auy`               | Awiyaana                     |    164K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/auy.txt)               |
| `avt`               | Au                           |    263K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/avt.txt)               |
| `awb`               | Awa (Papua New Guinea)       |    179K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/awb.txt)               |
| `az`                | Azerbaijani                  |  3,413K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/az.txt)                |
| `ba`                | Bashkir                      |    666K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ba.txt)                |
| `bbb`               | Barai                        |    289K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bbb.txt)               |
| `bbr`               | Girawa                       |    245K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bbr.txt)               |
| `bch`               | Bariai                       |    248K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bch.txt)               |
| `bdd`               | Bunama                       |    171K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bdd.txt)               |
| `bef`               | Benabena                     |    239K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bef.txt)               |
| `be`                | Belarusian                   |  1,441K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/be.txt)                |
| `bg`                | Bulgarian                    | 10,597K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bg.txt)                |
| `bhl`               | Bimin                        |    324K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bhl.txt)               |
| `big`               | Biangai                      |    229K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/big.txt)               |
| `bjr`               | Binumarien                   |    226K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bjr.txt)               |
| `bmh`               | Kein                         |    253K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bmh.txt)               |
| `bmu`               | Somba-Siawari                |    234K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bmu.txt)               |
| `bm`                | Bambara                      |     30K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bm.txt)                |
| `bnp`               | Bola                         |    263K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bnp.txt)               |
| `bn`                | Bangla                       |  7,258K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bn.txt)                |
| `boj`               | Anjam                        |    255K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/boj.txt)               |
| `bon`               | Bine                         |    244K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bon.txt)               |
| `bo`                | Tibetan                      |  5,642K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bo.txt)                |
| `bs`                | Bosnian                      |  8,993K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bs.txt)                |
| `buk`               | Bugawac                      |    264K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/buk.txt)               |
| `byx`               | Qaqet                        |    387K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/byx.txt)               |
| `bzh`               | Mapos Buang                  |    251K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bzh.txt)               |
| `ccp`               | Chakma                       |     79K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ccp.txt)               |
| `cjv`               | Chuave                       |    286K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cjv.txt)               |
| `cs`                | Czech                        |  3,141K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cs.txt)                |
| `cy`                | Welsh                        | 11,519K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cy.txt)                |
| `dad`               | Marik                        |    197K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dad.txt)               |
| `dah`               | Gwahatike                    |    274K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dah.txt)               |
| `ded`               | Dedua                        |    146K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ded.txt)               |
| `de`                | German                       | 46,431K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/de.txt)                |
| `dgz`               | Daga                         |    219K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dgz.txt)               |
| `dob`               | Dobu                         |    179K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dob.txt)               |
| `dww`               | Dawawa                       |    208K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dww.txt)               |
| `dz`                | Dzongkha                     |     61K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dz.txt)                |
| `el`                | Greek                        |  5,470K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/el.txt)                |
| `emi`               | Mussau-Emira                 |    176K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/emi.txt)               |
| `enq`               | Enga                         |    217K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/enq.txt)               |
| `eri`               | Ogea                         |    269K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/eri.txt)               |
| `es`                | Spanish                      | 32,670K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/es.txt)                |
| `fa`                | Persian                      |  9,114K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fa.txt)                |
| `fa-AF`             | Dari                         |  7,363K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fa-AF.txt)             |
| `faa`               | Fasu                         |    238K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/faa.txt)               |
| `fai`               | Faiwol                       |    256K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fai.txt)               |
| `fi`                | Finnish                      |  4,837K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fi.txt)                |
| `fit`               | Tornedalen Finnish           |    292K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fit.txt)               |
| `for`               | Fore                         |    169K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/for.txt)               |
| `fo`                | Faroese                      |    851K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fo.txt)                |
| `fuv`               | Nigerian Fulfulde            |     13K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fuv.txt)               |
| `gah`               | Alekano                      |    210K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gah.txt)               |
| `gam`               | Kandawo                      |    250K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gam.txt)               |
| `gaw`               | Nobonob                      |    246K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gaw.txt)               |
| `ga`                | Irish                        |  7,587K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ga.txt)                |
| `gdn`               | Umanakaina                   |    306K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gdn.txt)               |
| `gdr`               | Wipi                         |    271K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gdr.txt)               |
| `gd`                | Scottish Gaelic              | 17,105K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gd.txt)                |
| `gfk`               | Patpatar                     |    294K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gfk.txt)               |
| `ghs`               | Guhu-Samane                  |    186K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ghs.txt)               |
| `gsw-u-sd-chag`     | Swiss German (Aargau)        |     99K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gsw-u-sd-chag.txt)     |
| `gsw-u-sd-chbe`     | Swiss German (Bern)          |     73K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gsw-u-sd-chbe.txt)     |
| `gsw-u-sd-chfr`     | Swiss German (Fribourg)      |     42K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gsw-u-sd-chfr.txt)     |
| `gvf`               | Golin                        |    276K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gvf.txt)               |
| `gv`                | Manx Gaelic                  |    152K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gv.txt)                |
| `ha`                | Hausa                        |  1,775K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ha.txt)                |
| `haw`               | Hawaiian                     |  2,221K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/haw.txt)               |
| `hi`                | Hindi                        | 10,004K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hi.txt)                |
| `hla`               | Halia                        |    273K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hla.txt)               |
| `hot`               | Hote                         |    222K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hot.txt)               |
| `ho`                | Hiri Motu                    |    240K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ho.txt)                |
| `hr`                | Croatian                     |  8,188K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hr.txt)                |
| `hui`               | Huli                         |    232K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hui.txt)               |
| `hy`                | Armenian                     | 25,972K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hy.txt)                |
| `ian`               | Iatmul                       |    224K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ian.txt)               |
| `id`                | Indonesian                   |  6,634K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/id.txt)                |
| `ig`                | Igbo                         |     13K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ig.txt)                |
| `imo`               | Imbongu                      |    280K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/imo.txt)               |
| `ino`               | Inoke-Yate                   |    236K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ino.txt)               |
| `iou`               | Tuma-Irumu                   |    225K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/iou.txt)               |
| `ipi`               | Ipili                        |    312K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ipi.txt)               |
| `iu`                | Inuktitut                    |     98K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/iu.txt)                |
| `iws`               | Sepik Iwam                   |    307K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/iws.txt)               |
| `jae`               | Yabem                        |    186K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/jae.txt)               |
| `ja`                | Japanese                     |  2,116K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ja.txt)                |
| `kab`               | Kabyle                       |     66K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kab.txt)               |
| `kbm`               | Iwal                         |    298K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kbm.txt)               |
| `kbq`               | Kamano                       |    156K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kbq.txt)               |
| `kew`               | West Kewa                    |    247K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kew.txt)               |
| `kgf`               | Kube                         |    175K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kgf.txt)               |
| `khz`               | Keapara                      |    196K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/khz.txt)               |
| `kjs`               | East Kewa                    |    251K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kjs.txt)               |
| `kj`                | Kuanyama                     |  1,474K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kj.txt)                |
| `kk`                | Kazakh                       |    642K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kk.txt)                |
| `kmg`               | Kâte                         |    127K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kmg.txt)               |
| `kmo`               | Kwoma                        |    213K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kmo.txt)               |
| `kms`               | Kamasau                      |    293K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kms.txt)               |
| `kmu`               | Kanite                       |    214K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kmu.txt)               |
| `km`                | Khmer                        | 29,110K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/km.txt)                |
| `kpf`               | Komba                        |    174K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kpf.txt)               |
| `kpr`               | Korafe-Yegha                 |    262K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kpr.txt)               |
| `kpw`               | Kobon                        |    288K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kpw.txt)               |
| `kpx`               | Mountain Koiali              |    190K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kpx.txt)               |
| `kqc`               | Doromu-Koki                  |    209K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kqc.txt)               |
| `kqw`               | Kandas                       |    201K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kqw.txt)               |
| `ksd`               | Kuanua                       |    228K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ksd.txt)               |
| `ksr`               | Borong                       |    233K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ksr.txt)               |
| `kto`               | Kuot                         |    286K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kto.txt)               |
| `kud`               | ‘Auhelawa                    |    167K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kud.txt)               |
| `kue`               | Kuman (Papua New Guinea)     |    230K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kue.txt)               |
| `kup`               | Kunimaipa                    |    279K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kup.txt)               |
| `ku`                | Kurdish                      |  2,479K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ku.txt)                |
| `kwj`               | Kwanga                       |    290K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kwj.txt)               |
| `kyc`               | Kyaka                        |    220K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kyc.txt)               |
| `kyg`               | Keyagana                     |    190K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kyg.txt)               |
| `ky`                | Kyrgyz                       | 18,597K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ky.txt)                |
| `kze`               | Kosena                       |    164K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kze.txt)               |
| `la`                | Latin                        |     48K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/la.txt)                |
| `lb`                | Luxembourgish                |  5,173K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lb.txt)                |
| `lcm`               | Tungag                       |    239K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lcm.txt)               |
| `leu`               | Kara (Papua New Guinea)      |    255K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/leu.txt)               |
| `lid`               | Nyindrou                     |    308K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lid.txt)               |
| `lo`                | Lao                          |  4,384K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lo.txt)                |
| `mbh`               | Mangseng                     |    321K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mbh.txt)               |
| `mcq`               | Ese                          |    158K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mcq.txt)               |
| `med`               | Melpa                        |    283K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/med.txt)               |
| `mee`               | Mengen                       |    301K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mee.txt)               |
| `mek`               | Mekeo                        |    234K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mek.txt)               |
| `meu`               | Motu                         |    175K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/meu.txt)               |
| `mhl`               | Mauwake                      |    235K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mhl.txt)               |
| `mi`                | Maori                        |  1,504K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mi.txt)                |
| `mk`                | Macedonian                   | 10,422K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mk.txt)                |
| `mlh`               | Mape                         |    235K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mlh.txt)               |
| `mlp`               | Bargam                       |    297K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mlp.txt)               |
| `mmo`               | Mangga Buang                 |    269K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mmo.txt)               |
| `mmx`               | Madak                        |    271K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mmx.txt)               |
| `mna`               | Mbula                        |    257K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mna.txt)               |
| `mnw`               | Mon                          |  1,836K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mnw.txt)               |
| `mox`               | Molima                       |    222K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mox.txt)               |
| `mpt`               | Mian                         |    256K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mpt.txt)               |
| `mpx`               | Misima-Panaeati              |    227K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mpx.txt)               |
| `mr`                | Marathi                      | 16,594K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mr.txt)                |
| `msy`               | Aruamu                       |    229K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/msy.txt)               |
| `mti`               | Maiwa (Papua New Guinea)     |    166K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mti.txt)               |
| `mt`                | Maltese                      |  3,331K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mt.txt)                |
| `mux`               | Bo-Ung                       |    363K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mux.txt)               |
| `mva`               | Manam                        |    231K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mva.txt)               |
| `my`                | Burmese                      |  1,007K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/my.txt)                |
| `my-t-d0-zawgyi`    | Burmese (Zawgyi encoding)    |    593K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/my-t-d0-zawgyi.txt)    |
| `myw`               | Muyuw                        |    150K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/myw.txt)               |
| `naf`               | Nabak                        |    220K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/naf.txt)               |
| `nak`               | Nakanai                      |    333K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nak.txt)               |
| `nas`               | Naasioi                      |    168K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nas.txt)               |
| `nca`               | Iyo                          |    203K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nca.txt)               |
| `nho`               | Takuu                        |    309K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nho.txt)               |
| `nl`                | Dutch                        | 58,357K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nl.txt)                |
| `nop`               | Numanggang                   |    183K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nop.txt)               |
| `nou`               | Ewage-Notu                   |    266K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nou.txt)               |
| `nsn`               | Nehan                        |    248K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nsn.txt)               |
| `nvm`               | Namiae                       |    290K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/nvm.txt)               |
| `ny`                | Nyanja                       |    356K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ny.txt)                |
| `okv`               | Orokaiva                     |    212K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/okv.txt)               |
| `ong`               | Olo                          |    284K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ong.txt)               |
| `opm`               | Oksapmin                     |    332K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/opm.txt)               |
| `osa`               | Osage                        |      3K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/osa.txt)               |
| `pa`                | Punjabi                      | 59,990K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pa.txt)                |
| `pcm`               | Nigerian Pidgin              |    315K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pcm.txt)               |
| `pl`                | Polish                       |  7,148K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pl.txt)                |
| `ppo`               | Folopa                       |    258K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ppo.txt)               |
| `ps`                | Pashto                       |  7,343K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ps.txt)                |
| `ptp`               | Patep                        |    294K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ptp.txt)               |
| `pwg`               | Gapapaiwa                    |    208K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pwg.txt)               |
| `rai`               | Ramoaaina                    |    273K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rai.txt)               |
| `rm-puter`          | Romansh (Puter)              |  1,068K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-puter.txt)          |
| `rm-rumgr`          | Romansh (Grischun)           |  4,794K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-rumgr.txt)          |
| `rm-surmiran`       | Romansh (Surmiran)           |  2,540K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-surmiran.txt)       |
| `rm-sursilv`        | Romansh (Sursilvan)          | 11,678K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-sursilv.txt)        |
| `rm-sutsilv`        | Romansh (Sutsilvan)          |  1,007K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-sutsilv.txt)        |
| `rm-vallader`       | Romansh (Vallader)           |  5,560K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-vallader.txt)       |
| `roo`               | Rotokas                      |    292K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/roo.txt)               |
| `ro`                | Romanian                     | 13,962K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ro.txt)                |
| `rro`               | Waima                        |    177K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rro.txt)               |
| `ru`                | Russian                      | 40,987K² [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ru.txt)                |
| `rw`                | Kinyarwanda                  |    605K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rw.txt)                |
| `sah`               | Sakha                        |  2,457K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sah.txt)               |
| `sgz`               | Sursurunga                   |    327K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sgz.txt)               |
| `shn`               | Shan                         |  1,435K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/shn.txt)               |
| `sim`               | Mende (Papua New Guinea)     |    273K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sim.txt)               |
| `si`                | Sinhala                      |  1,046K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/si.txt)                |
| `sll`               | Salt-Yui                     |    264K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sll.txt)               |
| `sl`                | Slovenian                    | 10,975K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sl.txt)                |
| `snc`               | Sinaugoro                    |    216K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/snc.txt)               |
| `sny`               | Saniyo-Hiyewe                |    348K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sny.txt)               |
| `sn`                | Shona                        |  2,542K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sn.txt)                |
| `soq`               | Kanasi                       |    213K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/soq.txt)               |
| `so`                | Somali                       |    874K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/so.txt)                |
| `spl`               | Selepet                      |    244K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/spl.txt)               |
| `sps`               | Saposa                       |    324K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sps.txt)               |
| `sq`                | Albanian                     | 10,104K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sq.txt)                |
| `sr-Latn`           | Serbian (Latin)              | 10,143K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sr-Latn.txt)           |
| `ssd`               | Siroi                        |    210K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ssd.txt)               |
| `ssg`               | Seimat                       |    221K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ssg.txt)               |
| `ssx`               | Samberigi                    |    233K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ssx.txt)               |
| `sua`               | Sulka                        |    458K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sua.txt)               |
| `sue`               | Suena                        |    227K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sue.txt)               |
| `sv`                | Swedish                      | 33,633K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sv.txt)                |
| `swp`               | Suau                         |    175K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/swp.txt)               |
| `sw`                | Swahili                      |  8,817K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sw.txt)                |
| `taw`               | Tai                          |    268K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/taw.txt)               |
| `ta`                | Tamil                        |  1,413K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ta.txt)                |
| `tbc`               | Takia                        |    278K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tbc.txt)               |
| `tbo`               | Tawala                       |    198K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tbo.txt)               |
| `tgo`               | Sudest                       |    216K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tgo.txt)               |
| `tif`               | Tifal                        |    413K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tif.txt)               |
| `tim`               | Timbe                        |    206K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tim.txt)               |
| `ti`                | Tigrinya                     |    803K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ti.txt)                |
| `tlf`               | Telefol                      |    422K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tlf.txt)               |
| `tpi`               | Tok Pisin                    |  8,049K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tpi.txt)               |
| `tpz`               | Tinputz                      |    370K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tpz.txt)               |
| `tr`                | Turkish                      | 13,846K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tr.txt)                |
| `tte`               | Bwanabwana                   |    198K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tte.txt)               |
| `tt`                | Tatar                        |  1,356K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tt.txt)                |
| `ubr`               | Ubir                         |    222K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ubr.txt)               |
| `ug`                | Uyghur                       |  9,493K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ug.txt)                |
| `uk`                | Ukrainian                    | 12,921K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/uk.txt)                |
| `ur`                | Urdu                         |  3,622K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ur.txt)                |
| `usa`               | Usarufa                      |    171K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/usa.txt)               |
| `uvl`               | Lote                         |    277K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/uvl.txt)               |
| `vec`               | Venetian                     |      2K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/vec.txt)               |
| `vec-u-sd-itpd`     | Venetian (Padua)             |    813K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/vec-u-sd-itpd.txt)     |
| `vec-u-sd-itts`     | Venetian (Trieste)           |     12K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/vec-u-sd-itts.txt)     |
| `vec-u-sd-itvr`     | Venetian (Verona)            |     16K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/vec-u-sd-itvr.txt)     |
| `viv`               | Iduna                        |    220K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/viv.txt)               |
| `waj`               | Waffa                        |    236K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/waj.txt)               |
| `wer`               | Weri                         |    209K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wer.txt)               |
| `wiu`               | Wiru                         |    232K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wiu.txt)               |
| `wnc`               | Wantoat                      |    238K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wnc.txt)               |
| `wnu`               | Usan                         |    234K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wnu.txt)               |
| `wos`               | Hanga Hundi                  |    264K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wos.txt)               |
| `wrs`               | Waris                        |    213K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wrs.txt)               |
| `wsk`               | Waskia                       |    239K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wsk.txt)               |
| `wuv`               | Wuvulu-Aua                   |    187K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/wuv.txt)               |
| `xla`               | Kamula                       |    230K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xla.txt)               |
| `xsi`               | Sio                          |    319K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/xsi.txt)               |
| `yby`               | Yaweyuha                     |    219K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yby.txt)               |
| `yle`               | Yele                         |    298K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yle.txt)               |
| `yml`               | Iamalele                     |    245K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yml.txt)               |
| `yo`                | Yoruba                       |    270K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yo.txt)                |
| `yuj`               | Karkar-Yuri                  |    258K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yuj.txt)               |
| `yut`               | Yopno                        |    227K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yut.txt)               |
| `yuw`               | Yau (Morobe Province)        |    243K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yuw.txt)               |
| `zia`               | Zia                          |    242K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/zia.txt)               |


¹ To count tokens, we use an [ICU word break iterator](http://userguide.icu-project.org/boundaryanalysis#TOC-Word-Boundary) and count all tokens whose break status is one of `UBRK_WORD_LETTER`, `UBRK_WORD_KANA`, or `UBRK_WORD_IDEO`. Downloadable files include counts for each token. To get the raw text, run the crawler yourself.

² Crawl is still in progress; the final number will be larger.


## Running the Crawler

```sh
./corpuscrawler --language=yo --output=./corpus
```
