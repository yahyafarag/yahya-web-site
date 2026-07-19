import re

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<title>Yahya Tarek Farag - Engineering Profile</title>', '<title>INJAZ - Engineering Performance Solutions</title>')
html = html.replace('<h1>Yahya Tarek Farag</h1>', '<h1>INJAZ Engineering Performance</h1><h3 style="color: var(--text-muted); text-align:center; margin-bottom: 0.5rem;">Eng. Yahya Tarek</h3>')
html = html.replace('<h2>General Manager of Engineering</h2>', '<h2>Engineering Performance & Industrial Maintenance Expert<br><span style="font-size: 0.85em; color: var(--accent); display:block; margin-top:0.5rem; font-weight:bold;">"Stop the bleed, multiply your profits"</span></h2>')

# Slide 9 updates
html = html.replace('50+</h3>\n                          <p style="color: var(--text-muted); margin: 0.5rem 0 0 0;">New Branches Launched', '50M+</h3>\n                          <p style="color: var(--text-muted); margin: 0.5rem 0 0 0;">EGP Saved for Clients')
html = html.replace('35%</h3>\n                          <p style="color: var(--text-muted); margin: 0.5rem 0 0 0;">Contractor Cost Savings', '80%</h3>\n                          <p style="color: var(--text-muted); margin: 0.5rem 0 0 0;">Downtime Reduction')
html = html.replace('fa-store', 'fa-piggy-bank')
html = html.replace('fa-money-bill-trend-up', 'fa-arrow-trend-down')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update index-ar.html
with open('index-ar.html', 'r', encoding='utf-8') as f:
    html_ar = f.read()

html_ar = html_ar.replace('<title>Yahya Tarek Farag - Engineering Profile</title>', '<title>إنجاز لحلول الأداء الهندسي | م. يحيى طارق</title>')
html_ar = html_ar.replace('<h1>يحيى طارق فرج</h1>', '<h1>إنجاز لحلول الأداء الهندسي</h1><h3 style="color: var(--text-muted); text-align:center; margin-bottom: 0.5rem;">م. يحيى طارق</h3>')
html_ar = html_ar.replace('<h2>مدير عام هندسي</h2>', '<h2>خبير الأداء الهندسي والصيانة الصناعية<br><span style="font-size: 0.85em; color: var(--accent); display:block; margin-top:0.5rem; font-weight:bold;">"أوقف النزيف، وضاعف أرباحك"</span></h2>')

# Slide 9 Arabic updates
html_ar = html_ar.replace('+50</h3>\n                          <p style="color: var(--text-muted); margin: 0.5rem 0 0 0;">فرع جديد تم إطلاقه', '+50M</h3>\n                          <p style="color: var(--text-muted); margin: 0.5rem 0 0 0;">جنيه تم توفيرها لعملائنا')
html_ar = html_ar.replace('35%</h3>\n                          <p style="color: var(--text-muted); margin: 0.5rem 0 0 0;">توفير في تكاليف المقاولين', '80%</h3>\n                          <p style="color: var(--text-muted); margin: 0.5rem 0 0 0;">انخفاض في توقف خطوط الإنتاج')
html_ar = html_ar.replace('fa-store', 'fa-piggy-bank')
html_ar = html_ar.replace('fa-money-bill-trend-up', 'fa-arrow-trend-down')


with open('index-ar.html', 'w', encoding='utf-8') as f:
    f.write(html_ar)

print("Hero sections updated successfully.")
