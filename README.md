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
| `am`                | Amharic                      |  2,206K  |
| `az`                | Azeri                        |    511K² |
| `be`                | Belarusian                   |  1,494K  |
| `bg`                | Bulgarian                    | 10,718K  |
| `bm`                | Bambara                      |     31K  |
| `bn`                | Bangla                       |  4,846K² |
| `bo`                | Tibetan                      |  3,269K² |
| `bs`                | Bosnian                      |  9,093K  |
| `ccp`               | Chakma                       |     79K  |
| `cs`                | Czech                        |  2,430K² |
| `dz`                | Dzongkha                     |     62K  |
| `el`                | Greek                        |  1,005K² |
| `fa`                | Persian                      |  9,238K  |
| `fa-AF`             | Dari                         |  4,898K² |
| `fo`                | Faroese                      |    867K  |
| `fuv`               | Nigerian Fulfulde            |     13K  |
| `gsw-u-sd-chag`     | Swiss German (Aargau)        |    102K  |
| `gsw-u-sd-chbe`     | Swiss German (Bern)          |     73K  |
| `gsw-u-sd-chfr`     | Swiss German (Fribourg)      |     42K  |
| `gv`                | Manx Gaelic                  |    153K  |
| `ha`                | Hausa                        |  1,800K  |
| `hi`                | Hindi                        |  2,334K² |
| `hr`                | Croatian                     |  8,292K  |
| `id`                | Indonesian                   |    723K² |
| `ig`                | Igbo                         |     13K  |
| `kj`                | Kuanyama                     |  1,492K  |
| `kk`                | Kazakh                       |    670K  |
| `km`                | Khmer                        |  8,542K² |
| `ku`                | Kurdish                      |  1,620K² |
| `ky`                | Kyrgyz                       |  4,492K² |
| `lo`                | Lao                          |  4,456K  |
| `mk`                | Macedonian                   |  1,469K² |
| `mnw`               | Mon                          |  1,856K  |
| `mt`                | Maltese                      |  3,393K  |
| `my`                | Burmese                      |  1,015K  |
| `my-t-d0-zawgyi`    | Burmese (Zawgyi encoding)    |    599K  |
| `pl`                | Polish                       |    673K² |
| `ps`                | Pashto                       |  7,400K  |
| `rm-puter`          | Romansh (Puter)              |  1,080K  |
| `rm-rumgr`          | Romansh (Grischun)           |  4,870K  |
| `rm-surmiran`       | Romansh (Surmiran)           |  2,580K  |
| `rm-sursilv`        | Romansh (Sursilvan)          | 11,814K  |
| `rm-sutsilv`        | Romansh (Sutsilvan)          |  1,023K  |
| `rm-vallader`       | Romansh (Vallader)           |  5,609K  |
| `ro`                | Romanian                     | 14,092K  |
| `ru`                | Russian                      |  6,322K² |
| `rw`                | Kinyarwanda                  |    618K  |
| `shn`               | Shan                         |  1,481K  |
| `so`                | Somali                       |    883K  |
| `sq`                | Albanian                     | 10,194K  |
| `sr-Latn`           | Serbian (Latin)              |     373K |
| `sw`                | Swahili                      |  8,949K  |
| `ta`                | Tamil                        |  1,435K  |
| `taq`               | Tamasheq                     |     66K  |
| `tr`                | Turkish                      |  7,131K² |
| `ug`                | Uyghur                       |  4,504K² |
| `uk`                | Ukrainian                    |  5,017K² |
| `ur`                | Urdu                         |  3,652K  |
| `yo`                | Yoruba                       |     80K  |

¹ To count tokens, we use an [ICU word break iterator](http://userguide.icu-project.org/boundaryanalysis#TOC-Count-the-words-in-a-document-C-only-:) and count all tokens whose break status is not `UBRK_WORD_NONE`.

² Crawl is still in progress; the final number will be larger.


## Running the Crawler

```sh
./corpuscrawler --language=rm --output=./corpus
```
