# Corpus Crawler

_Corpus Crawler_ is a tool for [Corpus
Linguistics](https://en.wikipedia.org/wiki/Corpus_linguistics),
focusing on languages that are not very well supported by modern
language processing software.

Modern linguistic research works by analyzing corpora, which are large
samples of “real world” text. The crawler helps to build such corpora:
it follows links to web pages that are known to be written in a
certain language; it removes boilerplate and mark-up to extract clean
text; finally, it writes the output as plaintext files, separated by
language. The crawler adheres to the [Robots Exclusion
Standard](https://en.wikipedia.org/wiki/Robots_exclusion_standard) and
is intentionally slow, so it does not cause much load on the crawled
web sites.

This is not an official Google product. But if you’re a linguistic researcher,
or a developer of spell checking or other language-processing software,
you might find _Corpus Crawler_ useful.


## Supported Languages

| IETF BCP47          | Language                 |  Tokens |
| :------------------ | :----------------------- | ------: |
| `ccp`               | Chakma                   |    120K |
| `gsw-u-sd-chbe.txt` | Swiss german (Berne)     |     73K |
| `gsw-u-sd-chfr.txt` | Swiss german (Fribourg)  |     42K |
| `gv`                | Manx Gaelic              |    149K |
| `my`                | Burmese                  |    500K |
| `rm-puter`          | Romansh (Puter)          |  1,230K |
| `rm-rumgr`          | Romansh (Grischun)       |  5,605K |
| `rm-surmiran`       | Romansh (Surmiran)       |  3,287K |
| `rm-sursilv`        | Romansh (Sursilvan)      | 13,552K |
| `rm-sutsilv`        | Romansh (Sutsilvan)      |  1,230K |
| `rm-vallader`       | Romansh (Vallader)       |  6,347K |


If you’d like to add another language, or change anything else in the tool,
please read the [contribution guidelines](./CONTRIBUTING.md) and send
[pull requests](https://help.github.com/categories/collaborating-with-issues-and-pull-requests/).


## Running the Crawler

```sh
./corpuscrawler --language=my --output=./corpus
```
