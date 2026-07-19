import re

new_cards_en = """
        <!-- Article: Case Study Fast Food -->
        <article class="blog-card" data-category="maintenance">
            <img loading="lazy" src="assets/images/projects/mega_expansion.webp" alt="Fast Food Maintenance Case Study" class="blog-img" onerror="this.src='assets/images/blog/cmms.jpg'">
            <div class="blog-content">
                <div class="blog-meta">
                    <span class="blog-category">Case Study</span>
                    <span>March 10, 2026</span>
                </div>
                <h3 class="blog-title">Saving 5M EGP in Maintenance for a Fast Food Chain</h3>
                <p class="blog-excerpt">How standardizing asset registries and consolidating suppliers saved millions in 15 branches.</p>
                <a href="case-study-fastfood.html" class="read-more-btn">Read Case Study <i class="fa-solid fa-arrow-right" style="margin-left: 0.5rem;"></i></a>
            </div>
        </article>

        <!-- Article: Case Study Beverage -->
        <article class="blog-card" data-category="automation">
            <img loading="lazy" src="assets/images/blog/it-ot.jpg" alt="Energy Audit Case Study" class="blog-img">
            <div class="blog-content">
                <div class="blog-meta">
                    <span class="blog-category">Case Study</span>
                    <span>February 15, 2026</span>
                </div>
                <h3 class="blog-title">Reducing Electricity Bills by 22% for a Beverage Factory</h3>
                <p class="blog-excerpt">An energy audit that repaired leaks, corrected power factor, and replaced inefficient motors.</p>
                <a href="case-study-beverage.html" class="read-more-btn">Read Case Study <i class="fa-solid fa-arrow-right" style="margin-left: 0.5rem;"></i></a>
            </div>
        </article>

        <!-- Article: OEE -->
        <article class="blog-card" data-category="maintenance">
            <img loading="lazy" src="assets/images/blog/greenfield.jpg" alt="OEE Metric" class="blog-img">
            <div class="blog-content">
                <div class="blog-meta">
                    <span class="blog-category">Maintenance</span>
                    <span>January 20, 2026</span>
                </div>
                <h3 class="blog-title">OEE: The Ultimate Metric for Production Efficiency</h3>
                <p class="blog-excerpt">Learn how Overall Equipment Effectiveness reveals hidden capacity in your manufacturing plant.</p>
                <a href="article-oee.html" class="read-more-btn">Read Article <i class="fa-solid fa-arrow-right" style="margin-left: 0.5rem;"></i></a>
            </div>
        </article>

        <!-- Article: TCO -->
        <article class="blog-card" data-category="leadership">
            <img loading="lazy" src="assets/images/blog/cmms.jpg" alt="TCO Equation" class="blog-img">
            <div class="blog-content">
                <div class="blog-meta">
                    <span class="blog-category">Leadership</span>
                    <span>December 05, 2025</span>
                </div>
                <h3 class="blog-title">Repair or Replace? The TCO Equation That Decides</h3>
                <p class="blog-excerpt">Stop guessing and use the Total Cost of Ownership model to make asset replacement decisions.</p>
                <a href="article-tco.html" class="read-more-btn">Read Article <i class="fa-solid fa-arrow-right" style="margin-left: 0.5rem;"></i></a>
            </div>
        </article>
"""

with open('blog.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert after <div class="blog-grid" id="blogGrid">
html = html.replace('<div class="blog-grid" id="blogGrid">', '<div class="blog-grid" id="blogGrid">\n' + new_cards_en)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(html)


new_cards_ar = """
        <!-- Article: Case Study Fast Food -->
        <article class="blog-card" data-category="maintenance">
            <img loading="lazy" src="assets/images/projects/mega_expansion.webp" alt="Fast Food Maintenance Case Study" class="blog-img" onerror="this.src='assets/images/blog/cmms.jpg'">
            <div class="blog-content">
                <div class="blog-meta">
                    <span class="blog-category">دراسة حالة</span>
                    <span>10 مارس 2026</span>
                </div>
                <h3 class="blog-title">توفير 5 ملايين جنيه من الصيانة لسلسلة مطاعم</h3>
                <p class="blog-excerpt">كيف أدى توحيد سجلات الأصول والموردين إلى توفير الملايين في 15 فرعاً.</p>
                <a href="case-study-fastfood-ar.html" class="read-more-btn">اقرأ دراسة الحالة <i class="fa-solid fa-arrow-left" style="margin-right: 0.5rem;"></i></a>
            </div>
        </article>

        <!-- Article: Case Study Beverage -->
        <article class="blog-card" data-category="automation">
            <img loading="lazy" src="assets/images/blog/it-ot.jpg" alt="Energy Audit Case Study" class="blog-img">
            <div class="blog-content">
                <div class="blog-meta">
                    <span class="blog-category">دراسة حالة</span>
                    <span>15 فبراير 2026</span>
                </div>
                <h3 class="blog-title">خفض فاتورة الكهرباء 22% لمصنع مشروبات</h3>
                <p class="blog-excerpt">تدقيق للطاقة شمل إصلاح التسريبات، وتصحيح معامل القدرة، واستبدال المحركات.</p>
                <a href="case-study-beverage-ar.html" class="read-more-btn">اقرأ دراسة الحالة <i class="fa-solid fa-arrow-left" style="margin-right: 0.5rem;"></i></a>
            </div>
        </article>

        <!-- Article: OEE -->
        <article class="blog-card" data-category="maintenance">
            <img loading="lazy" src="assets/images/blog/greenfield.jpg" alt="OEE Metric" class="blog-img">
            <div class="blog-content">
                <div class="blog-meta">
                    <span class="blog-category">الصيانة</span>
                    <span>20 يناير 2026</span>
                </div>
                <h3 class="blog-title">مؤشر OEE: كيف تكشف الطاقة الإنتاجية لمصنعك</h3>
                <p class="blog-excerpt">تعرف على كيفية كشف الطاقة الخفية في مصنعك عبر مؤشر فعالية المعدات الشاملة.</p>
                <a href="article-oee-ar.html" class="read-more-btn">اقرأ المقال <i class="fa-solid fa-arrow-left" style="margin-right: 0.5rem;"></i></a>
            </div>
        </article>

        <!-- Article: TCO -->
        <article class="blog-card" data-category="leadership">
            <img loading="lazy" src="assets/images/blog/cmms.jpg" alt="TCO Equation" class="blog-img">
            <div class="blog-content">
                <div class="blog-meta">
                    <span class="blog-category">الإدارة</span>
                    <span>05 ديسمبر 2025</span>
                </div>
                <h3 class="blog-title">هل تستبدل المعدة أم تصلحها؟ معادلة الـ TCO</h3>
                <p class="blog-excerpt">توقف عن التخمين واستخدم التكلفة الإجمالية للملكية لاتخاذ قرارات استبدال الأصول.</p>
                <a href="article-tco-ar.html" class="read-more-btn">اقرأ المقال <i class="fa-solid fa-arrow-left" style="margin-right: 0.5rem;"></i></a>
            </div>
        </article>
"""

with open('blog-ar.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert after <div class="blog-grid" id="blogGrid">
html = html.replace('<div class="blog-grid" id="blogGrid">', '<div class="blog-grid" id="blogGrid">\n' + new_cards_ar)

with open('blog-ar.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated blog grids successfully.")
