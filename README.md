# ACME.ai — Security & GRC Portfolio (ISO 42001 flavored)

This repo showcases an AI governance program for a fictional AI company.  
It includes policies, controls, an AI risk register, and a CI workflow that produces an **ISO/IEC 42001 gap snapshot** on every push.

## What’s inside
- **Policies/Standards/Procedures** (audit-ready)
- **Controls catalog** mapped to ISO 42001, ISO 27001, NIST AI RMF
- **AI risk examples** (YAML + CSV)
- **CI workflow** that builds a gap report artifact (`out/42001-gap.md`)

## How the CI works
On every push, GitHub Actions runs a script that scans the `docs/` folder using the checklist in `ai/checklists/42001_checklist.yaml` and publishes the artifact under **Actions → latest run → Artifacts**.

## Folder structure
