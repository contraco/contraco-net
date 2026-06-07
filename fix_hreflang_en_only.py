import re

base = r"C:/Users/FrankMeltke/OneDrive - CONTRACO USA/Documents/GitHub/contraco"

pages = [
    "consulting-addiction.html",
    "consulting-addiction-1-executive-muscle-atrophy.html",
    "consulting-addiction-2-malicious-compliance.html",
    "consulting-addiction-3-translator-class.html",
    "consulting-addiction-4-deck-as-shield.html",
    "european-entry.html",
    "european-entry-1-germany-problem.html",
    "framework-agentic-commerce.html",
    "ai-cognition-essay.html",
]

for fname in pages:
    fpath = f"{base}/{fname}"
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove hreflang alternates for de, ru, ko only
    before = content.count("hreflang")
    content = re.sub(r'\s*<link[^>]+hreflang="(de|ru|ko)"[^>]*>\n?', '\n', content)
    after = content.count("hreflang")
    removed = before - after

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{fname}: removed {removed} hreflang tag(s)")

print("\nDone")
