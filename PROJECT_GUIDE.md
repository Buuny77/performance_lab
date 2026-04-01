# دليل مشروع Performance Lab

## شرح تفصيلي لكل جزء من المشروع

---

## 1. هيكل المشروع

```
performance_lab/
├── performance_lab/          # إعدادات المشروع الرئيسية
│   ├── __init__.py
│   ├── settings.py          # إعدادات Django
│   ├── urls.py              # روابط المشروع الرئيسية
│   └── wsgi.py              # إعدادات WSGI
│
├── main/                     # تطبيق الصفحات الرئيسية
│   ├── templates/main/       # قوالب HTML
│   │   ├── home.html        # الصفحة الرئيسية
│   │   ├── about.html       # من نحن
│   │   └── contact.html     # اتصل بنا
│   ├── views.py             # العروض (Views)
│   ├── urls.py              # روابط التطبيق
│   └── admin.py             # إعدادات لوحة التحكم
│
├── reviews/                  # تطبيق المراجعات
│   ├── templates/reviews/    # قوالب المراجعات
│   │   ├── index.html       # قائمة المراجعات
│   │   ├── laptops.html     # مراجعات اللابتوبات
│   │   ├── handhelds.html   # أجهزة اليد
│   │   ├── components.html  # المكونات
│   │   ├── extensions.html  # إضافات VS Code
│   │   └── detail.html      # تفاصيل المراجعة
│   ├── models.py            # نماذج البيانات
│   ├── views.py             # عروض المراجعات
│   └── admin.py             # إعدادات لوحة التحكم
│
├── tools/                    # تطبيق الأدوات التفاعلية
│   ├── templates/tools/      # قوالب الأدوات
│   │   ├── index.html       # صفحة الأدوات
│   │   ├── will_it_run.html # أداة "هل يعمل؟"
│   │   ├── compare.html     # أداة المقارنة
│   │   └── analyze.html     # أداة التحليل
│   ├── views.py             # عروض الأدوات
│   └── urls.py              # روابط الأدوات
│
├── static/                   # الملفات الثابتة
│   ├── css/
│   │   ├── neon-theme.css   # أنماط النيون
│   │   └── animations.css   # أنماط الأنيميشن
│   └── js/
│       ├── main.js          # JavaScript الرئيسي
│       └── animations.js    # أنيميشن JavaScript
│
├── templates/                # القوالب المشتركة
│   ├── base.html            # القالب الأساسي
│   └── includes/
│       ├── navbar.html      # شريط التنقل
│       └── footer.html      # تذييل الصفحة
│
└── manage.py                 # أداة إدارة Django
```

---

## 2. شرح الملفات الرئيسية

### 2.1 settings.py

هذا الملف يحتوي على جميع إعدادات المشروع:

```python
# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'main',           # تطبيقنا الرئيسي
    'reviews',        # تطبيق المراجعات
    'tools',          # تطبيق الأدوات
]

# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# الملفات الثابتة
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# ملفات الوسائط
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### 2.2 urls.py (المشروع)

يحدد روابط URL الرئيسية للمشروع:

```python
urlpatterns = [
    path('admin/', admin.site.urls),           # لوحة التحكم
    path('', include('main.urls')),             # الصفحة الرئيسية
    path('tools/', include('tools.urls')),      # الأدوات
    path('reviews/', include('reviews.urls')),  # المراجعات
]
```

### 2.3 models.py (reviews)

يحتوي على نماذج البيانات:

- **Device**: الأجهزة (لابتوبات، أجهزة يد)
- **Game**: الألعاب
- **AI_Model**: نماذج الذكاء الاصطناعي
- **Component**: المكونات (معالجات، كروت شاشة)
- **Extension**: إضافات VS Code
- **Review**: المراجعات

---

## 3. شرح القوالب (Templates)

### 3.1 base.html

القالب الأساسي الذي يورثه جميع القوالب الأخرى:

```html
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- أنماطنا المخصصة -->
    <link rel="stylesheet" href="{% static 'css/neon-theme.css' %}">
</head>
<body>
    {% include 'includes/navbar.html' %}
    {% block content %}{% endblock %}
    {% include 'includes/footer.html' %}
</body>
</html>
```

### 3.2 navbar.html

شريط التنقل مع تأثيرات النيون:

```html
<nav id="navbar" class="fixed top-0 left-0 right-0 z-50">
    <!-- شعار الموقع -->
    <a href="{% url 'main:home' %}">
        <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-neon-blue to-neon-purple">
            <i class="fas fa-microchip"></i>
        </div>
        <span>Performance</span>
        <span>Lab</span>
    </a>
    
    <!-- روابط التنقل -->
    <div class="hidden md:flex">
        <a href="{% url 'main:home' %}">الرئيسية</a>
        <a href="{% url 'reviews:index' %}">المراجعات</a>
        <a href="{% url 'tools:index' %}">الأدوات</a>
    </div>
</nav>
```

---

## 4. شرح CSS (التصميم)

### 4.1 neon-theme.css

يحتوي على تأثيرات النيون:

```css
/* ألوان النيون */
:root {
    --neon-blue: #00f3ff;
    --neon-purple: #bc13fe;
    --neon-pink: #ff006e;
    --neon-green: #39ff14;
}

/* تأثير النيون للنص */
.neon-text-blue {
    color: var(--neon-blue);
    text-shadow: 
        0 0 5px var(--neon-blue),
        0 0 10px var(--neon-blue),
        0 0 20px var(--neon-blue);
}

/* تأثير النيون للحدود */
.neon-border-blue {
    border: 1px solid var(--neon-blue);
    box-shadow: 0 0 5px var(--neon-blue);
}

/* بطاقة النيون */
.neon-card {
    background: var(--card-bg);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    transition: all 0.3s ease;
}

.neon-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 40px rgba(0, 243, 255, 0.1);
}
```

### 4.2 animations.css

يحتوي على تأثيرات الحركة:

```css
/* ظهور تدريجي */
.fade-in {
    animation: fadeIn 0.5s ease-out forwards;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* ظهور من الأسفل */
.fade-in-up {
    animation: fadeInUp 0.6s ease-out forwards;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* نبض */
.pulse {
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}
```

---

## 5. شرح JavaScript

### 5.1 main.js

الوظائف الرئيسية:

```javascript
// شريط التنقل المتحرك
function initNavbar() {
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 50) {
            navbar.classList.add('bg-dark-bg/95', 'backdrop-blur-xl');
        } else {
            navbar.classList.remove('bg-dark-bg/95', 'backdrop-blur-xl');
        }
    });
}

// عداد الأرقام
function animateCounter(element) {
    const target = parseInt(element.getAttribute('data-target'));
    let current = 0;
    const step = target / (2000 / 16);
    
    const timer = setInterval(() => {
        current += step;
        if (current >= target) {
            element.textContent = target.toLocaleString();
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(current).toLocaleString();
        }
    }, 16);
}

// إشعار
function showNotification(message, type = 'success') {
    const toast = document.getElementById('toast');
    toastMessage.textContent = message;
    toast.classList.remove('translate-y-20', 'opacity-0');
    
    setTimeout(() => {
        toast.classList.add('translate-y-20', 'opacity-0');
    }, 3000);
}
```

---

## 6. شرح Views (العروض)

### 6.1 views.py (main)

```python
def home(request):
    """الصفحة الرئيسية"""
    # جلب آخر 3 مراجعات
    latest_reviews = Review.objects.filter(
        is_published=True
    ).order_by('-created_at')[:3]
    
    # جلب أفضل 4 أجهزة
    top_devices = Device.objects.filter(
        is_active=True
    ).order_by('-benchmark_score')[:4]
    
    context = {
        'latest_reviews': latest_reviews,
        'top_devices': top_devices,
    }
    return render(request, 'main/home.html', context)
```

### 6.2 views.py (tools)

```python
def will_it_run(request):
    """أداة 'هل يعمل؟'"""
    devices = Device.objects.filter(is_active=True)
    games = Game.objects.filter(is_active=True)
    ai_models = AI_Model.objects.filter(is_active=True)
    
    context = {
        'devices': devices,
        'games': games,
        'ai_models': ai_models,
    }
    return render(request, 'tools/will_it_run.html', context)
```

---

## 7. كيفية الإضافة والتعديل

### 7.1 إضافة مراجعة جديدة

1. ادخل إلى لوحة التحكم: `/admin/`
2. اختر "مراجعات" → "إضافة مراجعة"
3. املأ الحقول:
   - العنوان
   - النوع (جهاز/مكون/إضافة)
   - المحتوى
   - التقييم
   - الصورة

### 7.2 إضافة جهاز جديد

1. ادخل إلى لوحة التحكم
2. اختر "أجهزة" → "إضافة جهاز"
3. املأ المواصفات:
   - الاسم والشركة
   - المعالج والذاكرة
   - كرت الشاشة
   - درجات الأداء
   - السعر

### 7.3 تعديل التصميم

لتعديل الألوان، عدل ملف `static/css/neon-theme.css`:

```css
:root {
    --neon-blue: #00f3ff;    /* تغيير اللون الأزرق */
    --neon-purple: #bc13fe;   /* تغيير اللون البنفسجي */
    /* ... */
}
```

---

## 8. استراتيجيات الربح

### 8.1 Affiliate Marketing

أضف روابط الشراء في نموذج الجهاز:

```python
class Device(models.Model):
    # ...
    affiliate_link = models.URLField(
        blank=True,
        verbose_name='رابط الشراء بالعمولة'
    )
```

### 8.2 بيع الأدوات الرقمية

يمكنك إضافة قسم لبيع:
- سكربتات أتمتة
- قوالب جاهزة
- أدوات برمجية

### 8.3 SaaS مصغر

أضف ميزات مدفوعة:
- تحليل أداء متقدم
- تقارير مفصلة
- دعم فني

---

## 9. تحسين الأداء

### 9.1 تحسين الصور

```python
# استخدم Pillow لضغط الصور
from PIL import Image

def compress_image(image_path):
    img = Image.open(image_path)
    img.save(image_path, optimize=True, quality=85)
```

### 9.2 التخزين المؤقت

```python
# في settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}
```

---

## 10. الأمان

### 10.1 إعدادات الأمان

```python
# في settings.py

# حماية CSRF
CSRF_COOKIE_SECURE = True

# حماية الجلسات
SESSION_COOKIE_SECURE = True

# HSTS
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
```

### 10.2 التحقق من المدخلات

```python
from django.core.validators import validate_email

def contact_view(request):
    email = request.POST.get('email')
    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse({'error': 'بريد إلكتروني غير صالح'})
```

---

## 11. النشر (Deployment)

### 11.1 إعدادات الإنتاج

```python
# في settings.py

DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# قاعدة بيانات الإنتاج
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'performance_lab',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 11.2 استخدام Gunicorn

```bash
# تثبيت Gunicorn
pip install gunicorn

# تشغيل الخادم
gunicorn performance_lab.wsgi:application --bind 0.0.0.0:8000
```

### 11.3 استخدام Nginx

```nginx
server {
    listen 80;
    server_name yourdomain.com;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    
    location /static/ {
        alias /path/to/static/;
    }
    
    location /media/ {
        alias /path/to/media/;
    }
}
```

---

## 12. المراجع

- [Django Documentation](https://docs.djangoproject.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Font Awesome](https://fontawesome.com/)

---

**ملاحظة**: هذا المشروع قابل للتطوير والتخصيص حسب احتياجاتك. يمكنك إضافة المزيد من الميزات والتحسينات!
