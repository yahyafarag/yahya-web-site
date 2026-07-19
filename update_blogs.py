import re

def insert_articles(file_path, new_articles_html):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Find the blog-grid div
    match = re.search(r'(<div class="blog-grid"[^>]*>)', html)
    if match:
        insert_idx = match.end()
        new_html = html[:insert_idx] + '\n' + new_articles_html + html[insert_idx:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Updated {file_path}")
    else:
        print(f"Could not find blog-grid in {file_path}")

en_articles = """
        <!-- Article: Case Study -->
        <article class="blog-card" data-category="case-study">
            <img src="assets/images/blog/cmms.jpg" alt="Cost Reduction Case Study" class="blog-img">
            <div class="blog-content">
                <div class="blog-meta">
                    <span class="blog-category">Case Study</span>
                    <span>August 01, 2026</span>
                </div>
                <h3 class="blog-title">Achieving EGP 60M Annual Savings Through Engineering Optimization</h3>
                <p class="blog-excerpt">How we successfully reduced annual engineering operating costs by 33% across 3 manufacturing plants.</p>
                <a href="case-study-cost.html" class="read-more-btn">Read Article <i class="fa-solid fa-arrow-right"></i></a>
            </div>
        </article>

        <!-- Article: 7 Lessons -->
        <article class="blog-card" data-category="leadership">
            <img src="assets/images/blog/greenfield.jpg" alt="Manufacturing Lessons" class="blog-img">
            <div class="blog-content">
                <div class="blog-meta">
                    <span class="blog-category">Leadership</span>
                    <span>July 20, 2026</span>
                </div>
                <h3 class="blog-title">7 Lessons I Learned After 13 Years in Manufacturing Operations</h3>
                <p class="blog-excerpt">Operational performance is rarely the result of one department working harder. It is the result of functions working together.</p>
                <a href="article-lessons.html" class="read-more-btn">Read Article <i class="fa-solid fa-arrow-right"></i></a>
            </div>
        </article>
"""

ar_articles = """
        <!-- Article: Case Study -->
        <article class="blog-card" data-category="case-study">
            <img src="assets/images/blog/cmms.jpg" alt="دراسة حالة خفض التكلفة" class="blog-img">
            <div class="blog-content">
                <div class="blog-meta">
                    <span class="blog-category">دراسة حالة</span>
                    <span>01 أغسطس 2026</span>
                </div>
                <h3 class="blog-title">تحقيق وفورات بقيمة 60 مليون جنيه سنوياً من خلال التحسين الهندسي</h3>
                <p class="blog-excerpt">كيف نجحنا في تحقيق تخفيض بنسبة 33% في تكاليف التشغيل الهندسية السنوية عبر 3 مصانع.</p>
                <a href="case-study-cost-ar.html" class="read-more-btn">اقرأ المقال <i class="fa-solid fa-arrow-left"></i></a>
            </div>
        </article>

        <!-- Article: 7 Lessons -->
        <article class="blog-card" data-category="leadership">
            <img src="assets/images/blog/greenfield.jpg" alt="دروس إدارة التصنيع" class="blog-img">
            <div class="blog-content">
                <div class="blog-meta">
                    <span class="blog-category">القيادة</span>
                    <span>20 يوليو 2026</span>
                </div>
                <h3 class="blog-title">7 دروس تعلمتها بعد 13 عاماً في إدارة التصنيع</h3>
                <p class="blog-excerpt">الأداء التشغيلي لا ينتج عادةً من عمل قسم واحد بجهد أكبر، بل من عمل الوظائف المختلفة معًا وفق نظام واضح.</p>
                <a href="article-lessons-ar.html" class="read-more-btn">اقرأ المقال <i class="fa-solid fa-arrow-left"></i></a>
            </div>
        </article>
"""

insert_articles('blog.html', en_articles)
insert_articles('blog-ar.html', ar_articles)
