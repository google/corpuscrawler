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

| IETF BCP47 Code     | Language                     |  Tokens¹ |
| :------------------ | :--------------------------- | -------: |
| `ae`                | Avestan                      |    129K  |
| `ae-Latn`           | Avestan (Latin)              |    141K  |
| `am`                | Amharic                      |  2,170K  |
| `az`                | Azerbaijani                  |  3,413K  |
| `be`                | Belarusian                   |  1,441K  |
| `bg`                | Bulgarian                    | 10,597K  |
| `bm`                | Bambara                      |     30K  |
| `bn`                | Bangla                       |  7,258K  |
| `bo`                | Tibetan                      |  5,642K  |
| `bs`                | Bosnian                      |  8,993K  |
| `ccp`               | Chakma                       |     79K  |
| `cs`                | Czech                        |  3,141K  |
| `dz`                | Dzongkha                     |     61K  |
| `el`                | Greek                        |    995K² |
| `fa`                | Persian                      |  9,114K  |
| `fa-AF`             | Dari                         |  7,363K  |
| `fi`                | Finnish                      |  4,058K² |
| `fit`               | Tornedalen Finnish           |    292K  |
| `fo`                | Faroese                      |    851K  |
| `fuv`               | Nigerian Fulfulde            |     13K  |
| `gsw-u-sd-chag`    | Swiss German (Aargau)        |     99K  |
| `gsw-u-sd-chbe`    | Swiss German (Bern)          |     73K  |
| `gsw-u-sd-chfr`    | Swiss German (Fribourg)      |     42K  |
| `gv`                | Manx Gaelic                  |    152K  |
| `ha`                | Hausa                        |  1,775K  |
| `hi`                | Hindi                        |  2,303K² |
| `hr`                | Croatian                     |  8,188K  |
| `id`                | Indonesian                   |  6,634K  |
| `ig`                | Igbo                         |     13K  |
| `ja`                | Japanese                     |  2,116K  |
| `kj`                | Kuanyama                     |  1,474K  |
| `kk`                | Kazakh                       |    642K  |
| `km`                | Khmer                        | 20,908K  |
| `ku`                | Kurdish                      |  2,479K  |
| `ky`                | Kyrgyz                       |  4,380K² |
| `lo`                | Lao                          |  4,384K  |
| `mk`                | Macedonian                   |  1,449K² |
| `mnw`               | Mon                          |  1,836K  |
| `mt`                | Maltese                      |  3,331K  |
| `my`                | Burmese                      |  1,007K  |
| `my-t-d0-zawgyi`    | Burmese (Zawgyi encoding)    |    593K  |
| `pl`                | Polish                       |    661K² |
| `ps`                | Pashto                       |  7,343K  |
| `rm-puter`          | Romansh (Puter)              |  1,068K  |
| `rm-rumgr`          | Romansh (Grischun)           |  4,794K  |
| `rm-surmiran`       | Romansh (Surmiran)           |  2,540K  |
| `rm-sursilv`        | Romansh (Sursilvan)          | 11,678K  |
| `rm-sutsilv`        | Romansh (Sutsilvan)          |  1,007K  |
| `rm-vallader`       | Romansh (Vallader)           |  5,560K  |
| `ro`                | Romanian                     | 13,962K  |
| `ru`                | Russian                      |  6,216K² |
| `rw`                | Kinyarwanda                  |    605K  |
| `shn`               | Shan                         |  1,435K  |
| `so`                | Somali                       |    874K  |
| `sq`                | Albanian                     | 10,104K  |
| `sr-Latn`           | Serbian (Latin)              |    369K² |
| `sv`                | Swedish                      |    236K² |
| `sw`                | Swahili                      |  8,817K  |
| `ta`                | Tamil                        |  1,413K  |
| `taq`               | Tamasheq                     |     66K  |
| `ti`                | Tigrinya                     |    803K  |
| `tr`                | Turkish                      |  7,005K² |
| `ug`                | Uyghur                       |  9,493K  |
| `uk`                | Ukrainian                    |  4,942K² |
| `ur`                | Urdu                         |  3,622K  |
| `yo`                | Yoruba                       |     80K  |

¹ To count tokens, we use an [ICU word break iterator](http://userguide.icu-project.org/boundaryanalysis#TOC-Word-Boundary) and count all tokens whose break status is one of `UBRK_WORD_LETTER`, `UBRK_WORD_KANA`, or `UBRK_WORD_IDEO`.

² Crawl is still in progress; the final number will be larger.


## Running the Crawler

```sh
./corpuscrawler --language=rm --output=./corpus
```
