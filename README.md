# Corpus Crawler

_Corpus Crawler_ is a tool for [Corpus
Linguistics](https://en.wikipedia.org/wiki/Corpus_linguistics).

Modern linguistic research works by analyzing corpora, which are large
samples of “real world” text. This crawler helps to build corpora: it
follows links to web pages that are known to be written in a certain
language; it removes boilerplate and HTML markup; finally, it writes
its output into plaintext files.  The crawler adheres to the [Robots
Exclusion
Standard](https://en.wikipedia.org/wiki/Robots_exclusion_standard) and
is intentionally slow, so it does not cause much load on the crawled
web sites.

This is not an official Google product. But if you’re a linguist or
plan to write software for spell checking or other language processing,
you might find _Corpus Crawler_ useful.


## Supported Languages

| IETF BCP47 Code     | Language                     |   Tokens |
| :------------------ | :--------------------------- | -------: |
| `am`                | Amharic                      |   1,148¹ |
| `be`                | Belarusian                   |    162K¹ |
| `bg`                | Bulgarian                    |  1,805K¹ |
| `bm`                | Bambara                      |     30K  |
| `bn`                | Bangla                       |  1,144K¹ |
| `bs`                | Bosnian                      |  1,033K¹ |
| `ccp`               | Chakma                       |    120K  |
| `el`                | Greek                        |  1,048K¹ |
| `fa`                | Persian                      |  2,958K¹ |
| `fa-AF`             | Dari                         |      0K¹ |
| `fo`                | Faroese                      |    870K  |
| `fuv`               | Nigerian Fulfulde            |     13K  |
| `gsw-u-sd-chag`     | Swiss German (Aargau)        |    102K  |
| `gsw-u-sd-chbe`     | Swiss German (Bern)          |     73K  |
| `gsw-u-sd-chfr`     | Swiss German (Fribourg)      |     42K  |
| `gv`                | Manx Gaelic                  |    149K  |
| `ha`                | Hausa                        |  1,780K  |
| `hi`                | Hindi                        |  1,197K¹ |
| `hr`                | Croatian                     |    930K¹ |
| `id`                | Indonesian                   |  1,264K¹ |
| `ig`                | Igbo                         |     12K  |
| `kj`                | Kuanyama                     |  1,506K  |
| `ky`                | Kyrgyz                       |  1,151K¹ |
| `mnw`               | Mon                          |    475K  |
| `mk`                | Macedonian                   |  1,355K¹ |
| `mt`                | Maltese                      |  1,045K¹ |
| `my`                | Burmese                      |    486K  |
| `my-t-d0-zawgyi`    | Burmese (Zawgyi encoding)    |    153K  |
| `pl`                | Polish                       |    644K¹ |
| `ps`                | Pashto                       |  1,549K¹ |
| `rm-puter`          | Romansh (Puter)              |  1,230K  |
| `rm-rumgr`          | Romansh (Grischun)           |  5,605K  |
| `rm-surmiran`       | Romansh (Surmiran)           |  3,287K  |
| `rm-sursilv`        | Romansh (Sursilvan)          | 13,552K  |
| `rm-sutsilv`        | Romansh (Sutsilvan)          |  1,230K  |
| `rm-vallader`       | Romansh (Vallader)           |  6,347K  |
| `ro`                | Romanian                     |  1,766K¹ |
| `ru`                | Russian                      |  1,148K¹ |
| `rw`                | Kinyarwanda                  |    616K  |
| `shn`               | Shan                         |    440K  |
| `so`                | Somali                       |    878K  |
| `sq`                | Albanian                     |  1,763K¹ |
| `sw`                | Swahili                      |  2,029K¹ |
| `ta`                | Tamil                        |  1,568K  |
| `taq`               | Tamasheq                     |     63K  |
| `tr`                | Turkish                      |    744K¹ |
| `uk`                | Ukrainian                    |    639K¹ |
| `ur`                | Urdu                         |  4,163K  |
| `yo`                | Yoruba                       |     79K  |

¹ Crawl still in progress; final number will be larger.


You’re very welcome to join the project, for example to add another language.
Please read the [contribution guidelines](./CONTRIBUTING.md) and send [pull
requests](https://help.github.com/categories/collaborating-with-issues-and-pull-requests/).


## Running the Crawler

```sh
./corpuscrawler --language=rm --output=./corpus
```
