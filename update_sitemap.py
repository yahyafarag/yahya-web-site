import re

def update_sitemap(sitemap_file):
    with open(sitemap_file, 'r', encoding='utf-8') as f:
        xml = f.read()
    
    new_urls = """
    <url>
        <loc>https://yahyafarag.github.io/yahya-web-site/article-lessons.html</loc>
        <lastmod>2026-07-20</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>https://yahyafarag.github.io/yahya-web-site/article-lessons-ar.html</loc>
        <lastmod>2026-07-20</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>https://yahyafarag.github.io/yahya-web-site/case-study-cost.html</loc>
        <lastmod>2026-08-01</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://yahyafarag.github.io/yahya-web-site/case-study-cost-ar.html</loc>
        <lastmod>2026-08-01</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
</urlset>
"""
    
    xml = xml.replace('</urlset>', new_urls)
    
    with open(sitemap_file, 'w', encoding='utf-8') as f:
        f.write(xml)
    print("Sitemap updated.")

update_sitemap('sitemap.xml')
