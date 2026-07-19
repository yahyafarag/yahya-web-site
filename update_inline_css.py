import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace inline cyan
    content = content.replace('rgba(0, 242, 254, 0.1)', 'rgba(242, 140, 40, 0.1)')
    content = content.replace('rgba(0, 242, 254, 0.2)', 'rgba(242, 140, 40, 0.2)')
    
    # Replace inline pink with orange
    content = content.replace('rgba(236, 72, 153, 0.1)', 'rgba(242, 140, 40, 0.1)')
    content = content.replace('#ec4899', 'var(--accent)')
    
    # Replace inline green (#10b981) in index with something else if needed, but it's okay to keep green for "success" metrics. Let's leave green for now.

    # Fix the "INJAZ Engineering Performance" hero if it broke anything
    # We already fixed it in update_hero.py
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("All HTML files updated with new inline brand colors.")
