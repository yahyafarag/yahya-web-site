import os
import re

def create_article(base_file, new_file, title, category, date, content_html, lang='en'):
    with open(base_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = re.sub(r'<title>.*?</title>', f'<title>{title} - Yahya Tarek Farag</title>', html)
    html = re.sub(r'<meta name="description".*?>', f'<meta name="description" content="{title}">', html)
    html = re.sub(r'article-cmms\.html', new_file, html)
    html = re.sub(r'article-cmms-ar\.html', new_file.replace('.html', '-ar.html') if lang=='en' else new_file.replace('-ar.html', '.html'), html)
    
    html = re.sub(r'<span class="article-category">.*?</span>', f'<span class="article-category">{category}</span>', html)
    html = re.sub(r'<h1 class="article-title">.*?</h1>', f'<h1 class="article-title">{title}</h1>', html)
    html = re.sub(r'June 12, 2026', date, html)
    
    start_tag = '<div class="article-content">'
    end_tag = '<div class="share-section">'
    
    start_idx = html.find(start_tag) + len(start_tag)
    end_idx = html.find(end_tag)
    
    new_html = html[:start_idx] + '\n' + content_html + '\n        </div>\n        ' + html[end_idx:]
    
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(new_html)

# 1. 7 Lessons
content_en1 = '''
<p>After 13+ years across engineering, maintenance, projects, utilities, and manufacturing support, I have learned that operational performance is rarely the result of one department working harder. It is usually the result of functions working together around a clear operating rhythm.</p>
<h2>Seven lessons continue to guide my work:</h2>
<ul>
    <li><strong>1. Production reliability is a cross-functional responsibility:</strong> It cannot be solved by maintenance alone.</li>
    <li><strong>2. Maintenance improves when priorities, standards, and ownership are visible.</strong></li>
    <li><strong>3. Cost reduction must protect safety, quality, and continuity.</strong> Cutting blindly costs more in the long run.</li>
    <li><strong>4. KPIs are valuable only when they change decisions.</strong> Data without action is just noise.</li>
    <li><strong>5. Greenfield projects succeed through coordination, not only technical design.</strong></li>
    <li><strong>6. A CMMS is a management system, not just software.</strong> It requires governance and human buy-in.</li>
    <li><strong>7. Strong teams are built through clarity, trust, and follow-through.</strong></li>
</ul>
<p>Manufacturing leadership is the discipline of connecting people, assets, data, and investment decisions to business results.</p>
'''

content_ar1 = '''
<p>بعد أكثر من 13 عامًا في الهندسة والصيانة والمشروعات والمرافق ودعم التصنيع، تعلمت أن الأداء التشغيلي لا ينتج عادةً من عمل قسم واحد بجهد أكبر، بل من عمل الوظائف المختلفة معًا وفق نظام واضح.</p>
<h2>أهم الدروس التي توجه عملي:</h2>
<ul>
    <li><strong>1. الاعتمادية مسؤولية مشتركة:</strong> لا يمكن للصيانة وحدها أن تتحمل مسؤولية استمرارية الإنتاج.</li>
    <li><strong>2. الصيانة تتحسن عندما تكون الأولويات والمعايير واضحة.</strong></li>
    <li><strong>3. خفض التكلفة يجب ألا يضر بالسلامة أو الجودة:</strong> التخفيض العشوائي يكلف أكثر.</li>
    <li><strong>4. مؤشرات الأداء لا قيمة لها ما لم تغيّر القرارات.</strong></li>
    <li><strong>5. المشروعات الجديدة (Greenfield) تنجح بالتنسيق بين الأقسام، وليس التصميم الفني فقط.</strong></li>
    <li><strong>6. نظام CMMS هو نظام إدارة وليس مجرد برنامج.</strong></li>
    <li><strong>7. الفرق القوية تُبنى بالوضوح والثقة والمتابعة.</strong></li>
</ul>
'''

create_article('article-cmms.html', 'article-lessons.html', '7 Lessons I Learned After 13 Years in Manufacturing Operations', 'Leadership', 'July 20, 2026', content_en1, 'en')
create_article('article-cmms-ar.html', 'article-lessons-ar.html', '7 دروس تعلمتها بعد 13 عاماً في إدارة التصنيع', 'القيادة', '20 يوليو 2026', content_ar1, 'ar')

# 2. Case Study: EGP 60M Cost Reduction
content_en2 = '''
<p>Cost reduction in manufacturing is not the same as cutting spend everywhere. The better approach is identifying where the cost is created and what capability must be protected.</p>
<h2>Challenge</h2>
<p>The organization faced escalating engineering and maintenance costs that were eroding margins across 3 manufacturing plants and 200+ operational facilities. Reactive maintenance was high, and preventive measures were not properly governed.</p>
<h2>Approach & Implementation</h2>
<ul>
    <li><strong>Visibility:</strong> Implemented an enterprise-wide CMMS to track work orders and inventory accurately.</li>
    <li><strong>Standardization:</strong> Built preventive and predictive maintenance routines.</li>
    <li><strong>Optimization:</strong> Separated recurring costs from one-time costs and challenged purchasing assumptions.</li>
    <li><strong>Governance:</strong> Established KPI dashboards holding teams accountable for both financial performance and operational reliability.</li>
</ul>
<h2>Results</h2>
<p>Within a strategic time-frame, we successfully <strong>reduced annual engineering operating costs by 33%</strong>. This delivered more than <strong>EGP 60M in annual savings</strong> without sacrificing production continuity or food safety.</p>
'''

content_ar2 = '''
<p>خفض التكلفة في التصنيع لا يعني خفض الإنفاق العشوائي في كل مكان. المنهج الأفضل هو تحديد أين تتكون التكلفة، وما هي القدرات التشغيلية التي يجب حمايتها.</p>
<h2>التحدي</h2>
<p>واجهت المنظمة تصاعداً في تكاليف الهندسة والصيانة مما أثر على هوامش الربح عبر 3 مصانع وأكثر من 200 منشأة تشغيلية. كانت الصيانة التفاعلية (Reactive) مرتفعة، ولم تكن التدابير الوقائية محكومة بشكل جيد.</p>
<h2>منهجية العمل (Approach)</h2>
<ul>
    <li><strong>الشفافية:</strong> تم تطبيق نظام CMMS لتتبع أوامر العمل والمخزون بدقة.</li>
    <li><strong>المعايير القياسية:</strong> بناء روتين صيانة وقائية وتنبؤية صارم.</li>
    <li><strong>تحسين النفقات:</strong> فصل التكلفة المتكررة عن المؤقتة ومراجعة سياسات المشتريات.</li>
    <li><strong>الحوكمة:</strong> إنشاء لوحات تحكم (Dashboards) لمؤشرات الأداء.</li>
</ul>
<h2>النتائج</h2>
<p>نجحنا في تحقيق <strong>تخفيض بنسبة 33% في تكاليف التشغيل الهندسية السنوية</strong>، مما أسفر عن تحقيق <strong>وفورات تجاوزت 60 مليون جنيه مصري سنوياً</strong>، دون المساومة على استمرارية الإنتاج أو جودة وسلامة الغذاء.</p>
'''

create_article('article-cmms.html', 'case-study-cost.html', 'Case Study: Achieving EGP 60M Annual Savings Through Engineering Optimization', 'Case Study', 'August 01, 2026', content_en2, 'en')
create_article('article-cmms-ar.html', 'case-study-cost-ar.html', 'دراسة حالة: تحقيق وفورات بقيمة 60 مليون جنيه سنوياً من خلال التحسين الهندسي', 'دراسة حالة', '01 أغسطس 2026', content_ar2, 'ar')

print("Articles and Case Studies generated.")
