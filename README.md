# LexiRead: Automated Vocabulary Documentation Pipeline

LexiRead is a vocabulary tracking and diagnostic engine that transforms raw vocabulary data (`words.json`) into audited technical documentation (`VOCAB_REPORT.md`) using a Docs-as-Code methodology.

## 🚀 Architecture & Pipeline

```text
[ words.json ] ──► [ Python Diagnostic Scripts ] ──► [ VOCAB_REPORT.md ] ──► [ GitHub Pages ]
  (Raw Data)           (Analysis & Health)             (Markdown Report)       (Live Docs)
