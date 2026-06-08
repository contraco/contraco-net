import re

base = r"C:/Users/FrankMeltke/OneDrive - CONTRACO USA/Documents/GitHub/contraco"

for fname in ["insights.html", "press.html"]:
    with open(f"{base}/{fname}", "r", encoding="utf-8") as f:
        content = f.read()
    # Find the malformed block with surrounding context
    idx = content.find('{ "@id": "https://meltke.com/#person" }')
    if idx != -1:
        # Show 250 chars before and 100 after
        print(f"=== {fname} ===")
        print(repr(content[max(0,idx-250):idx+100]))
        print()
