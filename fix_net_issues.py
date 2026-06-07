import os, re

base = r"C:/Users/FrankMeltke/OneDrive - CONTRACO USA/Documents/GitHub/contraco"

for fname in sorted(os.listdir(base)):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(base, fname)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    # Find protocol-relative links (not GoatCounter, already fixed)
    matches = re.findall(r'(?:src|href)=["\']//(?!gc\.zgo\.at)[^"\']+["\']', content)
    if matches:
        print(f"{fname}:")
        for m in matches:
            print(f"  {m}")
