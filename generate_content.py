import os

template_en = """<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{TITLE} - Yahya Tarek Farag</title>
    <meta name="description" content="{DESC}">
    <link rel="canonical" href="https://yahyafarag.github.io/yahya-web-site/{FILENAME}">
    <link rel="alternate" hreflang="en" href="https://yahyafarag.github.io/yahya-web-site/{FILENAME}" />
    <link rel="alternate" hreflang="ar" href="https://yahyafarag.github.io/yahya-web-site/{FILENAME_AR}" />
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
    <style>
        .article-content {{
            background: rgba(255,255,255,0.02);
            border: 1px solid var(--glass-border);
            border-radius: 15px;
            padding: 3rem;
            margin-top: 2rem;
            text-align: left;
            line-height: 1.8;
            font-size: 1.1rem;
        }}
        .article-content h2 {{ color: var(--accent); margin-top: 2rem; }}
        .article-content ul {{ padding-left: 1.5rem; margin-top: 1rem; }}
        .article-content li {{ margin-bottom: 0.5rem; }}
    </style>
</head>
<body>
    <div class="header">
        <h1 style="font-size: clamp(1rem, 1.5vw, 1.2rem); margin: 0; color: var(--accent);"><i class="fa-solid fa-file-lines"></i> Knowledge Base</h1>
        <div>
            <a href="{FILENAME_AR}" class="lang-switch">عربي</a>
            <a href="blog.html" class="btn"><i class="fa-solid fa-arrow-left"></i> Back to Blog</a>
        </div>
    </div>
    <div class="container">
        <h2 style="font-size: 2.5rem; margin-bottom: 1rem;">{TITLE}</h2>
        <div class="article-content">
            {CONTENT}
        </div>
    </div>
</body>
</html>"""

template_ar = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{TITLE} - يحيى طارق</title>
    <meta name="description" content="{DESC}">
    <link rel="canonical" href="https://yahyafarag.github.io/yahya-web-site/{FILENAME_AR}">
    <link rel="alternate" hreflang="ar" href="https://yahyafarag.github.io/yahya-web-site/{FILENAME_AR}" />
    <link rel="alternate" hreflang="en" href="https://yahyafarag.github.io/yahya-web-site/{FILENAME}" />
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
    <style>
        .article-content {{
            background: rgba(255,255,255,0.02);
            border: 1px solid var(--glass-border);
            border-radius: 15px;
            padding: 3rem;
            margin-top: 2rem;
            text-align: right;
            line-height: 1.8;
            font-size: 1.1rem;
        }}
        .article-content h2 {{ color: var(--accent); margin-top: 2rem; }}
        .article-content ul {{ padding-right: 1.5rem; margin-top: 1rem; }}
        .article-content li {{ margin-bottom: 0.5rem; }}
    </style>
</head>
<body>
    <div class="header">
        <h1 style="font-size: clamp(1rem, 1.5vw, 1.2rem); margin: 0; color: var(--accent);"><i class="fa-solid fa-file-lines"></i> قاعدة المعرفة</h1>
        <div>
            <a href="{FILENAME}" class="lang-switch">English</a>
            <a href="blog-ar.html" class="btn">العودة للمدونة <i class="fa-solid fa-arrow-right"></i></a>
        </div>
    </div>
    <div class="container">
        <h2 style="font-size: 2.5rem; margin-bottom: 1rem;">{TITLE}</h2>
        <div class="article-content">
            {CONTENT}
        </div>
    </div>
</body>
</html>"""

pages = [
    {
        "FILENAME": "case-study-fastfood.html",
        "FILENAME_AR": "case-study-fastfood-ar.html",
        "TITLE": "Saving 5M EGP in Maintenance for a Fast Food Chain",
        "TITLE_AR": "توفير 5 ملايين جنيه من الصيانة في السنة الأولى لسلسلة مطاعم",
        "DESC": "Case study of a 15-branch fast food chain that saved 5M EGP in maintenance costs with a 3-month ROI.",
        "DESC_AR": "دراسة حالة لسلسلة مطاعم 15 فرعاً وفرت 5 ملايين جنيه من الصيانة في أول سنة باسترداد استثمار 3 أشهر.",
        "CONTENT": """
            <p><strong>The Challenge:</strong> A fast food chain with 15 branches across Greater Cairo was spending over 800,000 EGP monthly on cooking and cooling equipment maintenance. Each branch dealt with different suppliers and distinct protocols, lacking a unified asset registry or lifespan tracking system.</p>
            <h2>The Solution Applied</h2>
            <ul>
                <li>Developed a unified asset registry for 15 branches encompassing 2,400 pieces of equipment.</li>
                <li>Restructured maintenance contracts and consolidated suppliers.</li>
                <li>Implemented preventive maintenance protocols for cooking and cooling equipment.</li>
                <li>Trained local branch maintenance officers on daily documentation.</li>
                <li>Conducted MTBF (Mean Time Between Failures) team training and developed rapid response protocols.</li>
            </ul>
            <h2>The Results</h2>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap; text-align: center; margin: 2rem 0;">
                <div style="background: rgba(0,242,254,0.1); padding: 2rem; border-radius: 10px; min-width: 200px;">
                    <h3 style="color: var(--accent); font-size: 2rem; margin: 0;">5M EGP</h3>
                    <p>Annual Savings</p>
                </div>
                <div style="background: rgba(0,242,254,0.1); padding: 2rem; border-radius: 10px; min-width: 200px;">
                    <h3 style="color: var(--accent); font-size: 2rem; margin: 0;">3 Months</h3>
                    <p>ROI Period</p>
                </div>
            </div>
            <p>Execution Time: 3 Months.</p>
        """,
        "CONTENT_AR": """
            <p><strong>التحدي:</strong> سلسلة من 15 فرعاً في القاهرة الكبرى كانت تُنفق 800,000 جنيه شهرياً على صيانة معدات الطهي والتبريد. كل فرع كان يتعامل مع موردين مختلفين وبروتوكولات مختلفة، دون وجود سجل أصول موحد أو إحصاء لأعمار المعدات.</p>
            <h2>الحل المطبق</h2>
            <ul>
                <li>بناء سجل أصول موحد لـ 15 فرعاً يضم 2,400 قطعة معدات.</li>
                <li>إعادة هيكلة عقود الصيانة وتوحيد الموردين.</li>
                <li>تطبيق بروتوكولات الصيانة الوقائية لمعدات الطهي والتبريد.</li>
                <li>تدريب مسؤولي الصيانة في كل فرع على التوثيق اليومي.</li>
                <li>تدريب الفريق على الـ MTBF (متوسط الوقت بين الأعطال) وإجراءات رد الفعل السريع.</li>
            </ul>
            <h2>النتائج المحققة</h2>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap; text-align: center; margin: 2rem 0;">
                <div style="background: rgba(0,242,254,0.1); padding: 2rem; border-radius: 10px; min-width: 200px;">
                    <h3 style="color: var(--accent); font-size: 2rem; margin: 0;">5 مليون</h3>
                    <p>جنيه توفير سنوي</p>
                </div>
                <div style="background: rgba(0,242,254,0.1); padding: 2rem; border-radius: 10px; min-width: 200px;">
                    <h3 style="color: var(--accent); font-size: 2rem; margin: 0;">3 أشهر</h3>
                    <p>فترة استرداد الاستثمار</p>
                </div>
            </div>
            <p>مدة التنفيذ: 3 أشهر.</p>
        """
    },
    {
        "FILENAME": "case-study-beverage.html",
        "FILENAME_AR": "case-study-beverage-ar.html",
        "TITLE": "Reducing Electricity Bills by 22% for a Beverage Factory",
        "TITLE_AR": "خفض فاتورة الكهرباء 22% من الشهر الأول لمصنع مشروبات",
        "DESC": "Energy audit case study showing how a beverage factory reduced its monthly electricity bill by 22%.",
        "DESC_AR": "دراسة حالة لتدقيق الطاقة توضح كيف تم خفض فاتورة كهرباء مصنع مشروبات بنسبة 22%.",
        "CONTENT": """
            <p><strong>The Challenge:</strong> A beverage factory in 10th of Ramadan City had a monthly electricity bill exceeding 200,000 EGP. Management had accepted this figure as a "necessary industrial cost". However, an engineering energy audit revealed that 22% of this bill was immediately savable.</p>
            <h2>The Solution Applied</h2>
            <ul>
                <li>Repaired 47 compressed air leak points which were wasting 18% of the compressor's energy.</li>
                <li>Installed a capacitor bank to correct the Power Factor from 0.72 to 0.97.</li>
                <li>Replaced 3 outdated motors with IE3 high-efficiency motors, generating annual savings that covered the upgrade cost twice over.</li>
                <li>Rescheduled heavy machinery operation outside of peak tariff hours.</li>
            </ul>
            <h2>The Results</h2>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap; text-align: center; margin: 2rem 0;">
                <div style="background: rgba(0,242,254,0.1); padding: 2rem; border-radius: 10px; min-width: 200px;">
                    <h3 style="color: var(--accent); font-size: 2rem; margin: 0;">22%</h3>
                    <p>Energy Savings</p>
                </div>
                <div style="background: rgba(0,242,254,0.1); padding: 2rem; border-radius: 10px; min-width: 200px;">
                    <h3 style="color: var(--accent); font-size: 2rem; margin: 0;">45K EGP</h3>
                    <p>Saved Monthly</p>
                </div>
            </div>
            <p>Execution Time: 6 Weeks.</p>
        """,
        "CONTENT_AR": """
            <p><strong>التحدي:</strong> مصنع مشروبات في العاشر من رمضان كانت فاتورة كهربائه الشهرية تتجاوز 200,000 جنيه. الإدارة قبلت الرقم كـ "ضرورة صناعية". لكن التدقيق الهندسي كشف أن 22% من هذه الفاتورة قابلة للتوفير الفوري.</p>
            <h2>الحل المطبق</h2>
            <ul>
                <li>إصلاح 47 نقطة تسريب هواء مضغوط كانت تهدر 18% من طاقة الكمبريسور.</li>
                <li>تركيب بنك مكثفات لتصحيح معامل القدرة من 0.72 إلى 0.97 لتجنب الغرامات.</li>
                <li>استبدال 3 محركات قديمة بأخرى عالية الكفاءة (IE3) بتوفير سنوي يتجاوز تكلفتها مرتين.</li>
                <li>جدولة أوقات تشغيل المعدات الثقيلة خارج ساعات الذروة.</li>
            </ul>
            <h2>النتائج المحققة</h2>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap; text-align: center; margin: 2rem 0;">
                <div style="background: rgba(0,242,254,0.1); padding: 2rem; border-radius: 10px; min-width: 200px;">
                    <h3 style="color: var(--accent); font-size: 2rem; margin: 0;">22%</h3>
                    <p>توفير في الطاقة</p>
                </div>
                <div style="background: rgba(0,242,254,0.1); padding: 2rem; border-radius: 10px; min-width: 200px;">
                    <h3 style="color: var(--accent); font-size: 2rem; margin: 0;">45,000 ج.م</h3>
                    <p>وفورات شهرية</p>
                </div>
            </div>
            <p>مدة التنفيذ: 6 أسابيع.</p>
        """
    },
    {
        "FILENAME": "article-oee.html",
        "FILENAME_AR": "article-oee-ar.html",
        "TITLE": "OEE: The Ultimate Metric for Production Efficiency",
        "TITLE_AR": "مؤشر OEE: كيف تكشف الطاقة الإنتاجية الحقيقية لمصنعك",
        "DESC": "Learn how Overall Equipment Effectiveness (OEE) reveals hidden capacity and how we raised a factory's OEE from 62% to 88%.",
        "DESC_AR": "تعرف على مؤشر كفاءة المعدات الشاملة (OEE) وكيف تمكنا من رفع كفاءة مصنع من 62% إلى 88% في 90 يوماً.",
        "CONTENT": """
            <p>Overall Equipment Effectiveness (OEE) is the gold standard for measuring manufacturing productivity. It identifies the percentage of manufacturing time that is truly productive. An OEE score of 100% means you are manufacturing only good parts, as fast as possible, with no stop time.</p>
            <h2>The Three Pillars of OEE</h2>
            <ul>
                <li><strong>Availability:</strong> Takes into account Downtime Loss, which includes any events that stop planned production for an appreciable length of time (e.g., equipment failures, material shortages).</li>
                <li><strong>Performance:</strong> Accounts for Speed Loss, which includes any factors that cause the process to operate at less than the maximum possible speed when running (e.g., machine wear, substandard materials).</li>
                <li><strong>Quality:</strong> Factors in Quality Loss, which encompasses produced pieces that do not meet quality standards, including pieces that require rework.</li>
            </ul>
            <h2>Case in Point: The 90-Day Turnaround</h2>
            <p>In a recent engagement with a bottling plant, their perceived capacity was fully maxed out, and management was considering purchasing a new production line. We measured their baseline OEE and found it hovering at an alarming <strong>62%</strong>.</p>
            <p>By implementing targeted preventive maintenance to boost Availability, and optimizing conveyor speeds to improve Performance, we successfully raised the OEE to <strong>88%</strong> within 90 days. This uncovered "hidden capacity" saved the client millions in CAPEX that would have been spent on a new line.</p>
        """,
        "CONTENT_AR": """
            <p>تعتبر الفعالية الشاملة للمعدات (OEE) المعيار الذهبي لقياس الإنتاجية في التصنيع. فهي تحدد النسبة المئوية لوقت التصنيع الذي يكون منتجاً حقاً. درجة OEE بنسبة 100٪ تعني أنك تصنع أجزاء جيدة فقط، بأسرع ما يمكن، دون أي وقت توقف.</p>
            <h2>الركائز الثلاث لمؤشر OEE</h2>
            <ul>
                <li><strong>الإتاحة (Availability):</strong> تأخذ في الاعتبار خسارة التوقف، والتي تشمل أي أحداث توقف الإنتاج المخطط له لفترة زمنية ملحوظة (مثل أعطال المعدات، نقص المواد).</li>
                <li><strong>الأداء (Performance):</strong> يحسب خسارة السرعة، والتي تشمل أي عوامل تتسبب في تشغيل العملية بسرعة أقل من أقصى سرعة ممكنة (مثل تآكل الماكينات).</li>
                <li><strong>الجودة (Quality):</strong> تشمل خسارة الجودة، والتي تتضمن القطع المنتجة التي لا تفي بمعايير الجودة والمنتجات المعيبة.</li>
            </ul>
            <h2>دراسة من الواقع: التحول في 90 يوماً</h2>
            <p>في مشروع حديث مع مصنع تعبئة، كانت السعة المحددة مستنفدة بالكامل، وكانت الإدارة تدرس شراء خط إنتاج جديد. قمنا بقياس الـ OEE ووجدناه عند <strong>62%</strong> فقط.</p>
            <p>من خلال تنفيذ صيانة وقائية موجهة لرفع الإتاحة، وتحسين سرعات السيور لرفع الأداء، نجحنا في رفع مؤشر OEE إلى <strong>88%</strong> في غضون 90 يوماً فقط. هذه "الطاقة الخفية" وفرت على المصنع ملايين الجنيهات التي كانت ستُنفق على خط جديد.</p>
        """
    },
    {
        "FILENAME": "article-tco.html",
        "FILENAME_AR": "article-tco-ar.html",
        "TITLE": "Repair or Replace? The TCO Equation That Decides",
        "TITLE_AR": "هل تستبدل المعدة أم تصلحها؟ معادلة الـ TCO",
        "DESC": "Total Cost of Ownership (TCO) vs CAPEX. Stop guessing and use data to make asset replacement decisions.",
        "DESC_AR": "تحليل التكلفة الإجمالية للملكية (TCO). توقف عن التخمين واستخدم البيانات لاتخاذ قرارات استبدال الأصول بذكاء.",
        "CONTENT": """
            <p>The "Repair vs. Replace" dilemma is one of the most common and critical CAPEX decisions engineering managers face. Making this decision based on gut feeling or simple repair cost comparisons often leads to massive financial leaks.</p>
            <h2>The TCO Approach</h2>
            <p>The <strong>Total Cost of Ownership (TCO)</strong> model moves beyond the initial purchase price or the immediate repair quote. It factors in:</p>
            <ul>
                <li><strong>Acquisition Costs:</strong> Purchase price, shipping, installation, and commissioning.</li>
                <li><strong>Operating Costs:</strong> Energy consumption, consumables, and operator labor (newer machines often consume significantly less energy).</li>
                <li><strong>Maintenance Costs:</strong> Routine PM, spare parts, and expected failure rates.</li>
                <li><strong>Downtime Costs:</strong> The opportunity cost of lost production. An older machine might be cheap to repair, but if it breaks down frequently, the lost production value eclipses the repair savings.</li>
                <li><strong>Salvage Value:</strong> The residual value of the asset at the end of its life.</li>
            </ul>
            <h2>Making the Call</h2>
            <p>If the projected TCO of the existing machine over the next 3-5 years (including the rising curve of maintenance and downtime costs) exceeds the TCO of a new machine (CAPEX + lower operating/maintenance costs), it's time to replace. Don't let the sunk cost fallacy tie you to a depreciating, inefficient asset.</p>
        """,
        "CONTENT_AR": """
            <p>تعتبر معضلة "الإصلاح أم الاستبدال" واحدة من أكثر قرارات ميزانية الـ CAPEX شيوعاً وأهمية التي يواجهها مديرو الهندسة. اتخاذ هذا القرار بناءً على الحدس أو مقارنات بسيطة لتكلفة الإصلاح غالباً ما يؤدي إلى تسرب مالي ضخم.</p>
            <h2>منهجية التكلفة الإجمالية للملكية (TCO)</h2>
            <p>يتجاوز نموذج <strong>التكلفة الإجمالية للملكية (TCO)</strong> سعر الشراء الأولي أو فاتورة الإصلاح الحالية. فهو يأخذ في الاعتبار:</p>
            <ul>
                <li><strong>تكاليف الاستحواذ:</strong> سعر الشراء، الشحن، التركيب، والتشغيل.</li>
                <li><strong>تكاليف التشغيل:</strong> استهلاك الطاقة، المواد الاستهلاكية، وعمالة التشغيل (الآلات الأحدث تستهلك طاقة أقل بكثير).</li>
                <li><strong>تكاليف الصيانة:</strong> الصيانة الوقائية الروتينية، قطع الغيار، ومعدلات الفشل المتوقعة.</li>
                <li><strong>تكاليف التوقف:</strong> تكلفة الفرصة البديلة للإنتاج المفقود. قد تكون الماكينة القديمة رخيصة في الإصلاح، ولكن إذا كانت تتعطل بشكل متكرر، فإن قيمة الإنتاج المفقود تتجاوز وفورات الإصلاح بأضعاف.</li>
                <li><strong>القيمة التخريدية:</strong> القيمة المتبقية للأصل في نهاية عمره الافتراضي.</li>
            </ul>
            <h2>القرار المبني على الأرقام</h2>
            <p>إذا كانت التكلفة الإجمالية للملكية (TCO) المتوقعة للماكينة الحالية على مدى 3-5 سنوات القادمة (بما في ذلك المنحنى المتصاعد لتكاليف الصيانة والتوقف) تتجاوز الـ TCO لماكينة جديدة (سعر الشراء + تكاليف تشغيل وصيانة أقل)، فقد حان وقت الاستبدال. لا تدع مغالطة التكلفة الغارقة (Sunk Cost Fallacy) تربطك بأصل غير فعال يستهلك أرباحك.</p>
        """
    }
]

for p in pages:
    html_en = template_en.format(**p)
    with open(p['FILENAME'], 'w', encoding='utf-8') as f:
        f.write(html_en)
        
    p['CONTENT'] = p['CONTENT_AR']
    p['TITLE'] = p['TITLE_AR']
    p['DESC'] = p['DESC_AR']
    
    html_ar = template_ar.format(**p)
    with open(p['FILENAME_AR'], 'w', encoding='utf-8') as f:
        f.write(html_ar)

print("Generated all HTML files successfully.")
