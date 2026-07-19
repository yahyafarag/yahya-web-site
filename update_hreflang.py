import re

tags = '''
    <link rel="canonical" href="https://yahyafarag.github.io/yahya-web-site/{file}">
    <link rel="alternate" hreflang="en" href="https://yahyafarag.github.io/yahya-web-site/index.html">
    <link rel="alternate" hreflang="ar" href="https://yahyafarag.github.io/yahya-web-site/index-ar.html">
    <link rel="alternate" hreflang="x-default" href="https://yahyafarag.github.io/yahya-web-site/index.html">
'''

for file in ['index.html', 'index-ar.html']:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if 'hreflang' not in html:
        insert_idx = html.find('</title>') + 8
        new_html = html[:insert_idx] + tags.format(file=file) + html[insert_idx:]
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f'Added tags to {file}')
