import os

base = r'C:/Users/FrankMeltke/OneDrive - CONTRACO USA/Documents/GitHub/contraco'

# Fix 1: www. links in framework-agentic-commerce.html
fpath = os.path.join(base, 'framework-agentic-commerce.html')
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

count = content.count('https://www.contraco.net/')
content = content.replace('https://www.contraco.net/', 'https://contraco.net/')
with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"framework-agentic-commerce.html: fixed {count} www. links")

# Fix 2: GoatCounter protocol-relative across all HTML files
fixed_files = 0
total_fixes = 0
for fname in sorted(os.listdir(base)):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(base, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    count = content.count('async src="//gc.zgo.at/count.js"')
    if count > 0:
        content = content.replace(
            'async src="//gc.zgo.at/count.js"',
            'async src="https://gc.zgo.at/count.js"'
        )
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed_files += 1
        total_fixes += count
        print(f"  GoatCounter fixed: {fname}")

print(f"\nGoatCounter: {total_fixes} fixes across {fixed_files} files")
print("Done")
