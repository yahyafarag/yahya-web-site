import re

for file in ['blog.html', 'blog-ar.html']:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('<img ', '<img loading="lazy" ')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print('Added lazy loading.')
