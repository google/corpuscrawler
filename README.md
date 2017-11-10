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

| IETF BCP47 Code     | Language                     |  Tokens¹                                                                           |
| :------------------ | :--------------------------- | ---------------------------------------------------------------------------------: |
| `ae`                | Avestan                      |    129K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ae.txt)                |
| `ae-Latn`           | Avestan (Latin)              |    141K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ae-Latn.txt)           |
| `am`                | Amharic                      |  2,170K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/am.txt)                |
| `az`                | Azerbaijani                  |  3,413K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/az.txt)                |
| `be`                | Belarusian                   |  1,441K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/be.txt)                |
| `bg`                | Bulgarian                    | 10,597K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bg.txt)                |
| `bm`                | Bambara                      |     30K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bm.txt)                |
| `bn`                | Bangla                       |  7,258K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bn.txt)                |
| `bo`                | Tibetan                      |  5,642K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bo.txt)                |
| `bs`                | Bosnian                      |  8,993K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/bs.txt)                |
| `ccp`               | Chakma                       |     79K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ccp.txt)               |
| `cs`                | Czech                        |  3,141K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/cs.txt)                |
| `de`                | German                       |  7,894K² [💾](http://www.gstatic.com/i18n/corpora/wordcounts/de.txt)                |
| `dz`                | Dzongkha                     |     61K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/dz.txt)                |
| `el`                | Greek                        |  5,470K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/el.txt)                |
| `es`                | Spanish                      | 32,670K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/es.txt)                |
| `fa`                | Persian                      |  9,114K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fa.txt)                |
| `fa-AF`             | Dari                         |  7,363K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fa-AF.txt)             |
| `fi`                | Finnish                      |  4,837K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fi.txt)                |
| `fit`               | Tornedalen Finnish           |    292K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fit.txt)               |
| `fo`                | Faroese                      |    851K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fo.txt)                |
| `fuv`               | Nigerian Fulfulde            |     13K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/fuv.txt)               |
| `ga`                | Irish                        |    298K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ga.txt)                |
| `gd`                | Scottish Gaelic              | 17,105K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gd.txt)                |
| `gsw-u-sd-chag`     | Swiss German (Aargau)        |     99K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gsw-u-sd-chag.txt)     |
| `gsw-u-sd-chbe`     | Swiss German (Bern)          |     73K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gsw-u-sd-chbe.txt)     |
| `gsw-u-sd-chfr`     | Swiss German (Fribourg)      |     42K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gsw-u-sd-chfr.txt)     |
| `gv`                | Manx Gaelic                  |    152K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/gv.txt)                |
| `ha`                | Hausa                        |  1,775K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ha.txt)                |
| `haw`               | Hawaiian                     |  2,221K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/haw.txt)               |
| `hi`                | Hindi                        | 10,004K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hi.txt)                |
| `hr`                | Croatian                     |  8,188K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/hr.txt)                |
| `id`                | Indonesian                   |  6,634K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/id.txt)                |
| `ig`                | Igbo                         |     13K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ig.txt)                |
| `ja`                | Japanese                     |  2,116K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ja.txt)                |
| `kj`                | Kuanyama                     |  1,474K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kj.txt)                |
| `kk`                | Kazakh                       |    642K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/kk.txt)                |
| `km`                | Khmer                        | 20,908K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/km.txt)                |
| `ku`                | Kurdish                      |  2,479K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ku.txt)                |
| `ky`                | Kyrgyz                       |  4,380K² [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ky.txt)                |
| `la`                | Latin                        |     48K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/la.txt)                |
| `lo`                | Lao                          |  4,384K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/lo.txt)                |
| `mi`                | Maori                        |  1,504K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mi.txt)                |
| `mk`                | Macedonian                   | 10,422K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mk.txt)                |
| `mnw`               | Mon                          |  1,836K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mnw.txt)               |
| `mt`                | Maltese                      |  3,331K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/mt.txt)                |
| `my`                | Burmese                      |  1,007K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/my.txt)                |
| `my-t-d0-zawgyi`    | Burmese (Zawgyi encoding)    |    593K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/my-t-d0-zawgyi.txt)    |
| `pl`                | Polish                       |  7,148K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/pl.txt)                |
| `ps`                | Pashto                       |  7,343K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ps.txt)                |
| `rm-puter`          | Romansh (Puter)              |  1,068K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-puter.txt)          |
| `rm-rumgr`          | Romansh (Grischun)           |  4,794K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-rumgr.txt)          |
| `rm-surmiran`       | Romansh (Surmiran)           |  2,540K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-surmiran.txt)       |
| `rm-sursilv`        | Romansh (Sursilvan)          | 11,678K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-sursilv.txt)        |
| `rm-sutsilv`        | Romansh (Sutsilvan)          |  1,007K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-sutsilv.txt)        |
| `rm-vallader`       | Romansh (Vallader)           |  5,560K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rm-vallader.txt)       |
| `ro`                | Romanian                     | 13,962K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ro.txt)                |
| `ru`                | Russian                      |  6,216K² [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ru.txt)                |
| `rw`                | Kinyarwanda                  |    605K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/rw.txt)                |
| `shn`               | Shan                         |  1,435K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/shn.txt)               |
| `si`                | Sinhala                      |  1,046K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/si.txt)                |
| `sn`                | Shona                        |  2,542K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sn.txt)                |
| `so`                | Somali                       |    874K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/so.txt)                |
| `sq`                | Albanian                     | 10,104K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sq.txt)                |
| `sr-Latn`           | Serbian (Latin)              | 10,143K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sr-Latn.txt)           |
| `sv`                | Swedish                      | 33,633K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sv.txt)                |
| `sw`                | Swahili                      |  8,817K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/sw.txt)                |
| `ta`                | Tamil                        |  1,413K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ta.txt)                |
| `taq`               | Tamasheq                     |     66K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/taq.txt)               |
| `ti`                | Tigrinya                     |    803K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ti.txt)                |
| `tr`                | Turkish                      | 13,846K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/tr.txt)                |
| `ug`                | Uyghur                       |  9,493K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ug.txt)                |
| `uk`                | Ukrainian                    | 12,921K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/uk.txt)                |
| `ur`                | Urdu                         |  3,622K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/ur.txt)                |
| `vec`               | Venetian                     |    815K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/vec.txt)               |
| `yo`                | Yoruba                       |     80K  [💾](http://www.gstatic.com/i18n/corpora/wordcounts/yo.txt)                |

¹ To count tokens, we use an [ICU word break iterator](http://userguide.icu-project.org/boundaryanalysis#TOC-Word-Boundary) and count all tokens whose break status is one of `UBRK_WORD_LETTER`, `UBRK_WORD_KANA`, or `UBRK_WORD_IDEO`. Downloadable files include counts for each token. To get the raw text, run the crawler yourself.

² Crawl is still in progress; the final number will be larger.


## Running the Crawler

```sh
./corpuscrawler --language=rm --output=./corpus
```
