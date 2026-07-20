# TrustGuard Crawler

Cybersecurity RAG corpus collection and preprocessing toolkit. Crawls,
cleans, and chunks security knowledge from multiple authoritative sources
into retrieval-ready text for LLM-powered security applications.

## Data Sources

| Source | Description | Format |
|---|---|---|
| NVD (National Vulnerability Database) | Recent CVEs with CVSS scores | API → Markdown |
| MITRE CWE Top 25 2024 | Common Weakness Enumeration | API → Markdown |
| MITRE CAPEC | Attack pattern classification | Local → Markdown |
| MITRE ATT&CK | Adversarial tactics & techniques | STIX → Markdown |
| CISA KEV | Known exploited vulnerabilities | Feed → Markdown |
| OWASP Top 10 | Web application security risks | Markdown |
| OWASP ASVS / WSTG | Verification & testing standards | Local → Markdown |
| NIST CSF 2.0 / SP 800-53 | Security frameworks | Local → Markdown |
| ISO/IEC 27001:2022 | ISMS standard | Local → Markdown |
| China GB Standards | National security standards | Local → Markdown |
| cvelistV5 | Full CVE archive (1999–2026) | JSON → Markdown |
| Internet search | Keyword-based security news/articles | DuckDuckGo API |

## Project Structure

```
trustguard-crawler/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── crawlers/                       # Data collection scripts
│   ├── cwe_crawler.py              #   CWE Top 25 / CAPEC / OWASP
│   ├── nist_crawler.py             #   NIST CSF / SP 800-53 / ISO 27001
│   ├── china_standards_crawler.py  #   China GB standards & regulations
│   ├── live_crawler.py             #   NVD recent CVEs / CISA KEV
│   ├── internet_crawler.py         #   DuckDuckGo keyword search
│   └── consolidate.py              #   Merge all outputs into RAG corpus
│
├── scripts/                        # Preprocessing pipeline
│   ├── clean_owasp.py              #   Clean OWASP Markdown
│   ├── clean_attck.py              #   Convert ATT&CK STIX → Markdown
│   ├── clean_cve.py                #   Convert CVE JSON → Markdown
│   └── splitter.py                 #   Chunk cleaned docs for RAG
│
├── doc/                            # Raw documents (organized by source)
│   ├── crawled/                    #   Crawler output (project-generated)
│   ├── owasp/                      #   OWASP Top 10 (2017/2021/2025)
│   ├── cve/                        #   cvelistV5 archive
│   └── attck/                      #   MITRE ATT&CK STIX data
│
├── data-sample/                    # CVE verification dataset samples
│
├── clean/                          # Cleaned Markdown output (gitignored)
└── chunks/                         # Chunked text output (gitignored)
```

## Quick Start

### Prerequisites

- Python 3.9+
- Docker (for data-sample CVE verification)

### Installation

```bash
pip install -r requirements.txt
```

### Crawl Security Data

```bash
# CWE Top 25, CAPEC, OWASP materials
python crawlers/cwe_crawler.py

# NIST frameworks, NVD recent CVEs
python crawlers/nist_crawler.py

# China standards and regulations
python crawlers/china_standards_crawler.py

# Live CVE data from NVD + CISA KEV
python crawlers/live_crawler.py

# Internet keyword search
python crawlers/internet_crawler.py

# Consolidate all crawler output
python crawlers/consolidate.py
```

### Preprocess for RAG

```bash
# Clean OWASP Markdown (strip front matter, HTML, etc.)
python scripts/clean_owasp.py \
    --input doc/owasp/Top10-master/2017/en \
    --output clean/owasp/2017/en

# Convert ATT&CK STIX to Markdown
python scripts/clean_attck.py

# Convert CVE JSON to Markdown
python scripts/clean_cve.py \
    --input doc/cve/cvelistV5-main/cves/2026 \
    --output clean/cve/2026

# Split cleaned docs into retrieval chunks
python scripts/splitter.py \
    --input clean/owasp/2017/en \
    --output chunks/owasp/2017/en
```

All scripts support `--help` for full usage details.

### Data Sample (CVE Verification)

The `data-sample/` directory contains Docker-based CVE verification environments
for 3 projects across 8 CVEs:

| Project | Language | CVEs |
|---|---|---|
| caddy | Go | CVE-2026-27587, CVE-2026-27588, CVE-2026-30851 |
| cms (Kirby/Craft) | PHP | CVE-2025-30207, CVE-2025-31493, CVE-2025-35939 |
| saleor | Python | CVE-2026-22849, CVE-2026-24136 |

See `data-sample/README.md` for detailed usage.

## RAG Corpus Stats

| Metric | Value |
|---|---|
| Total entries | 114 |
| Total characters | ~303K |
| Data sources | 7 |
| Categories | 8 |

## Incremental Updates

- **Daily**: `live_crawler.py` and `internet_crawler.py` for latest CVEs and news
- **Weekly**: `cwe_crawler.py` for CWE Top 25 updates
- **On-demand**: `china_standards_crawler.py` and `nist_crawler.py` for frameworks
- **After each crawl**: `consolidate.py` to rebuild the unified corpus

## Upstream Source Repositories

The `doc/` directory includes data from these public repositories:

- [OWASP Top 10](https://github.com/OWASP/Top10)
- [cvelistV5](https://github.com/CVEProject/cvelistV5)
- [ATT&CK STIX Data](https://github.com/mitre-attack/attack-stix-data)

If you need the full upstream datasets, clone them directly from source.

## License

MIT License — see [LICENSE](LICENSE) for details.
