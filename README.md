name: AI Governance Gap Snapshot

on:
  push:
    branches: [ "main" ]
  pull_request:

jobs:
  gap-assessment:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install deps
        run: pip install pyyaml tabulate

      - name: Run ISO 42001 gap snapshot
        run: |
          python scripts/run_gap_assessment.py \
            --docs docs \
            --checklist ai/checklists/42001_checklist.yaml \
            --out out/42001-gap.md

      - name: Upload report artifact
        uses: actions/upload-artifact@v4
        with:
          name: iso42001-gap-snapshot
          path: out/42001-gap.md

  secret-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Gitleaks
        uses: zricethezav/gitleaks-action@v2
        with:
          args: "--redact --verbose"

