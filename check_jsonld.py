import re

base = r"C:/Users/FrankMeltke/OneDrive - CONTRACO USA/Documents/GitHub/contraco"

for fname in ["insights.html", "press.html"]:
    fpath = f"{base}/{fname}"
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    print(f"=== {fname} — {len(blocks)} JSON-LD block(s) ===")
    for i, b in enumerate(blocks):
        stripped = b.strip()
        is_malformed = '"@context"' not in stripped
        flag = "  <-- MALFORMED (no @context)" if is_malformed else ""
        print(f"  Block {i+1} ({len(stripped)} chars){flag}: {stripped[:80]}")
    print()
