import argparse, os, yaml
from tabulate import tabulate

def collect_text(root):
    blobs = []
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.endswith((".md",".txt",".yaml",".yml",".csv")):
                p = os.path.join(dirpath, fn)
                try:
                    with open(p, "r", encoding="utf-8") as f:
                        blobs.append((p, f.read().lower()))
                except Exception:
                    pass
    return blobs

def keyword_hit(text, keywords):
    return any(k.lower() in text for k in keywords)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", required=True)
    ap.add_argument("--checklist", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    with open(args.checklist, "r", encoding="utf-8") as f:
        checklist = yaml.safe_load(f)

    blobs = collect_text(args.docs)

    rows = []
    for item in checklist["items"]:
        hits = [path for (path, text) in blobs if keyword_hit(text, item["evidence_keywords"])]
        status = "Adequate" if hits else "Gap"
        rows.append([item["id"], item["title"], status, "; ".join(hits[:5])])

    md = ["# ISO/IEC 42001 Gap Snapshot\n",
          "| Requirement | Title | Status | Evidence |",
          "|---|---|---|---|"]
    for r in rows:
        md.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |")

    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    print(tabulate(rows, headers=["Requirement","Title","Status","Evidence"], tablefmt="github"))

if __name__ == "__main__":
    main()
