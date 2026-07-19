import re

new_projects_en = """
            <div class="project-vault-card">
                <img loading="lazy" decoding="async" src="assets/images/blog/cmms.jpg" alt="Intelligent Asset Management" class="project-vault-img" style="height:250px; object-fit:cover;">
                <div class="project-vault-content">
                    <h3 class="project-vault-title"><i class="fa-solid fa-qrcode"></i> Intelligent Asset Management (22 Branches)</h3>
                    <p class="project-vault-desc">Implemented a comprehensive cloud-based asset registry for a major restaurant chain that had lost track of expensive kitchen equipment across its branches.</p>
                    <ul class="project-vault-list">
                        <li>Conducted a full field inventory and tagged assets with heat/water-resistant metal QR codes.</li>
                        <li>Reduced unnecessary equipment procurement by <strong>18%</strong> by redistributing idle assets.</li>
                        <li>Achieved <strong>100% accurate spatial tracking</strong> of all high-value machinery.</li>
                    </ul>
                </div>
            </div>

            <div class="project-vault-card">
                <img loading="lazy" decoding="async" src="assets/images/blog/it-ot.jpg" alt="Energy Solutions for Textile Factory" class="project-vault-img" style="height:250px; object-fit:cover;">
                <div class="project-vault-content">
                    <h3 class="project-vault-title"><i class="fa-solid fa-bolt"></i> Energy Optimization: Giant Textile Factory</h3>
                    <p class="project-vault-desc">Air compressors were running at full capacity 24/7, consuming 30% of the factory's total electricity bill while sections still complained of low pressure.</p>
                    <ul class="project-vault-list">
                        <li>Used ultrasonic scanning to detect and fix <strong>85 compressed air leaks</strong>.</li>
                        <li>Installed Variable Frequency Drives (VFDs) on the main compressors.</li>
                        <li>Reduced compressor energy consumption by <strong>25%</strong> and stabilized air pressure by <strong>15%</strong>.</li>
                    </ul>
                </div>
            </div>

            <div class="project-vault-card">
                <img loading="lazy" decoding="async" src="assets/images/blog/greenfield.jpg" alt="Commercial Mall FM" class="project-vault-img" style="height:250px; object-fit:cover;">
                <div class="project-vault-content">
                    <h3 class="project-vault-title"><i class="fa-solid fa-city"></i> Integrated FM & Automation for a Commercial Mall</h3>
                    <p class="project-vault-desc">The mall's public areas and garages had lighting and HVAC running at 100% capacity 24/7, resulting in astronomical utility bills.</p>
                    <ul class="project-vault-list">
                        <li>Installed a Building Management System (BMS) with motion sensors in the garages.</li>
                        <li>Programmed timers to reduce lighting and HVAC to 50% capacity post-midnight.</li>
                        <li>Slashed the electricity bill by <strong>35%</strong> with an ROI period of just <strong>4 months</strong>, while maintaining 100% visitor comfort.</li>
                    </ul>
                </div>
            </div>
"""

with open('projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert before the closing </div> of .container
html = html.replace('        </div>\n    \n        <!-- CTA -->', new_projects_en + '\n        </div>\n    \n        <!-- CTA -->')

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(html)


new_projects_ar = """
            <div class="project-vault-card">
                <img loading="lazy" decoding="async" src="assets/images/blog/cmms.jpg" alt="Intelligent Asset Management" class="project-vault-img" style="height:250px; object-fit:cover;">
                <div class="project-vault-content">
                    <h3 class="project-vault-title"><i class="fa-solid fa-qrcode"></i> الإدارة الذكية للأصول (22 فرعاً)</h3>
                    <p class="project-vault-desc">تنفيذ سجل أصول سحابي شامل لسلسلة مطاعم كبرى كانت تعاني من فقدان معدات المطابخ باهظة الثمن بين الفروع.</p>
                    <ul class="project-vault-list">
                        <li>جرد ميداني كامل وتركيب ملصقات باركود معدنية مقاومة للحرارة والمياه على كل أصل.</li>
                        <li>خفض المشتريات غير الضرورية بنسبة <strong>18%</strong> عبر إعادة توزيع الأصول الراكدة.</li>
                        <li>تحقيق تتبع مكاني دقيق بنسبة <strong>100%</strong> لجميع المعدات ذات القيمة العالية.</li>
                    </ul>
                </div>
            </div>

            <div class="project-vault-card">
                <img loading="lazy" decoding="async" src="assets/images/blog/it-ot.jpg" alt="Energy Solutions for Textile Factory" class="project-vault-img" style="height:250px; object-fit:cover;">
                <div class="project-vault-content">
                    <h3 class="project-vault-title"><i class="fa-solid fa-bolt"></i> حلول الطاقة: مصنع نسيج عملاق</h3>
                    <p class="project-vault-desc">ضواغط الهواء كانت تعمل بكامل طاقتها 24 ساعة، وتستهلك 30% من إجمالي فاتورة الكهرباء، مع شكوى مستمرة من ضعف الضغط في خطوط الإنتاج.</p>
                    <ul class="project-vault-list">
                        <li>إجراء مسح بالموجات فوق الصوتية لاكتشاف وعلاج <strong>85 نقطة تسريب هواء</strong>.</li>
                        <li>تركيب محولات تردد (VFD) على الضواغط الرئيسية.</li>
                        <li>تقليل استهلاك الضواغط بنسبة <strong>25%</strong> وتحسين استقرار الضغط بنسبة <strong>15%</strong>.</li>
                    </ul>
                </div>
            </div>

            <div class="project-vault-card">
                <img loading="lazy" decoding="async" src="assets/images/blog/greenfield.jpg" alt="Commercial Mall FM" class="project-vault-img" style="height:250px; object-fit:cover;">
                <div class="project-vault-content">
                    <h3 class="project-vault-title"><i class="fa-solid fa-city"></i> إدارة المرافق والأتمتة لمجمع تجاري</h3>
                    <p class="project-vault-desc">كانت الإضاءة والتكييف في المناطق العامة والجراجات تعمل بكامل طاقتها على مدار الساعة، مما أدى لفواتير كهرباء جنونية.</p>
                    <ul class="project-vault-list">
                        <li>تركيب أنظمة BMS بسيطة مع حساسات حركة في الجراجات.</li>
                        <li>برمجة أنظمة زمنية (Timers) لخفض الإضاءة والتكييف إلى النصف بعد منتصف الليل.</li>
                        <li>خفض فاتورة الكهرباء بنسبة <strong>35%</strong> مع استرداد الاستثمار خلال <strong>4 أشهر</strong> فقط، دون المساس براحة الزوار.</li>
                    </ul>
                </div>
            </div>
"""

with open('projects-ar.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert before the closing </div> of .container
html = html.replace('        </div>\n    \n        <!-- CTA -->', new_projects_ar + '\n        </div>\n    \n        <!-- CTA -->')

with open('projects-ar.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated projects pages successfully.")
