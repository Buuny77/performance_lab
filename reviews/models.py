"""
models.py - تطبيق reviews
نماذج البيانات للمراجعات والأجهزة
"""
from django.db import models
from django.utils import timezone


class Device(models.Model):
    """
    نموذج الأجهزة - اللابتوبات وأجهزة اليد
    """
    DEVICE_TYPES = [
        ('laptop', 'لابتوب'),
        ('handheld', 'جهاز يد'),
        ('desktop', 'كمبيوتر مكتبي'),
    ]
    
    name = models.CharField(max_length=200, verbose_name='اسم الجهاز')
    brand = models.CharField(max_length=100, verbose_name='الشركة المصنعة')
    model = models.CharField(max_length=100, verbose_name='الموديل')
    device_type = models.CharField(
        max_length=20, 
        choices=DEVICE_TYPES, 
        verbose_name='نوع الجهاز'
    )
    
    # المواصفات التقنية
    processor = models.CharField(max_length=200, verbose_name='المعالج')
    ram = models.CharField(max_length=50, verbose_name='الذاكرة العشوائية')
    storage = models.CharField(max_length=100, verbose_name='التخزين')
    gpu = models.CharField(max_length=200, verbose_name='كرت الشاشة')
    display = models.CharField(max_length=200, verbose_name='الشاشة')
    battery = models.CharField(max_length=100, verbose_name='البطارية')
    
    # درجات الأداء
    benchmark_score = models.IntegerField(default=0, verbose_name='درجة الأداء')
    gaming_score = models.IntegerField(default=0, verbose_name='درجة الألعاب')
    ai_score = models.IntegerField(default=0, verbose_name='درجة الذكاء الاصطناعي')
    dev_score = models.IntegerField(default=0, verbose_name='درجة التطوير')
    
    # السعر والتوفر
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name='السعر'
    )
    affiliate_link = models.URLField(
        blank=True, 
        verbose_name='رابط الشراء'
    )
    
    # الصور
    image = models.ImageField(
        upload_to='devices/', 
        verbose_name='الصورة الرئيسية'
    )
    
    # الحالة
    is_active = models.BooleanField(default=True, verbose_name='نشط')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'جهاز'
        verbose_name_plural = 'الأجهزة'
        ordering = ['-benchmark_score']
    
    def __str__(self):
        return f'{self.brand} {self.name}'


class Game(models.Model):
    """
    نموذج الألعاب - للتحقق من توافقها مع الأجهزة
    """
    name = models.CharField(max_length=200, verbose_name='اسم اللعبة')
    genre = models.CharField(max_length=100, verbose_name='التصنيف')
    
    # المتطلبات الدنيا
    min_processor = models.CharField(max_length=200, verbose_name='المعالج الأدنى')
    min_ram = models.CharField(max_length=50, verbose_name='الذاكرة الأدنى')
    min_gpu = models.CharField(max_length=200, verbose_name='كرت الشاشة الأدنى')
    
    # المتطلبات الموصى بها
    rec_processor = models.CharField(max_length=200, verbose_name='المعالج الموصى به')
    rec_ram = models.CharField(max_length=50, verbose_name='الذاكرة الموصى بها')
    rec_gpu = models.CharField(max_length=200, verbose_name='كرت الشاشة الموصى به')
    
    # الأداء المتوقع
    expected_fps_low = models.IntegerField(default=30, verbose_name='أقل FPS')
    expected_fps_high = models.IntegerField(default=60, verbose_name='أعلى FPS')
    
    image = models.ImageField(upload_to='games/', verbose_name='صورة اللعبة')
    is_active = models.BooleanField(default=True, verbose_name='نشط')
    
    class Meta:
        verbose_name = 'لعبة'
        verbose_name_plural = 'الألعاب'
    
    def __str__(self):
        return self.name


class AI_Model(models.Model):
    """
    نموذج نماذج الذكاء الاصطناعي - للتحقق من توافقها مع الأجهزة
    """
    name = models.CharField(max_length=200, verbose_name='اسم النموذج')
    description = models.TextField(verbose_name='الوصف')
    
    # المتطلبات
    min_vram = models.IntegerField(verbose_name='الحد الأدنى للذاكرة الفيديو (GB)')
    rec_vram = models.IntegerField(verbose_name='الذاكرة الفيديو الموصى بها (GB)')
    min_ram = models.IntegerField(verbose_name='الحد الأدنى للذاكرة (GB)')
    
    # الأداء المتوقع
    inference_speed_slow = models.CharField(max_length=50, verbose_name='سرعة الاستدلاء البطيئة')
    inference_speed_fast = models.CharField(max_length=50, verbose_name='سرعة الاستدلاء السريعة')
    
    is_active = models.BooleanField(default=True, verbose_name='نشط')
    
    class Meta:
        verbose_name = 'نموذج ذكاء اصطناعي'
        verbose_name_plural = 'نماذج الذكاء الاصطناعي'
    
    def __str__(self):
        return self.name


class Component(models.Model):
    """
    نموذج المكونات - معالجات، كروت شاشة، إلخ
    """
    COMPONENT_TYPES = [
        ('cpu', 'معالج'),
        ('gpu', 'كرت شاشة'),
        ('ram', 'ذاكرة'),
        ('ssd', 'تخزين'),
        ('motherboard', 'لوحة أم'),
    ]
    
    name = models.CharField(max_length=200, verbose_name='اسم المكون')
    brand = models.CharField(max_length=100, verbose_name='الشركة')
    component_type = models.CharField(
        max_length=20, 
        choices=COMPONENT_TYPES, 
        verbose_name='نوع المكون'
    )
    
    # المواصفات
    specs = models.JSONField(verbose_name='المواصفات التفصيلية')
    
    # الأداء
    performance_score = models.IntegerField(default=0, verbose_name='درجة الأداء')
    
    # السعر
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name='السعر'
    )
    affiliate_link = models.URLField(blank=True, verbose_name='رابط الشراء')
    
    image = models.ImageField(upload_to='components/', verbose_name='الصورة')
    is_active = models.BooleanField(default=True, verbose_name='نشط')
    
    class Meta:
        verbose_name = 'مكون'
        verbose_name_plural = 'المكونات'
    
    def __str__(self):
        return self.name


class Extension(models.Model):
    """
    نموذج إضافات VS Code وأدوات المطورين
    """
    name = models.CharField(max_length=200, verbose_name='اسم الأداة')
    description = models.TextField(verbose_name='الوصف')
    category = models.CharField(max_length=100, verbose_name='التصنيف')
    
    # التقييم
    rating = models.DecimalField(
        max_digits=3, 
        decimal_places=2, 
        verbose_name='التقييم'
    )
    downloads = models.IntegerField(default=0, verbose_name='عدد التحميلات')
    
    # الروابط
    marketplace_link = models.URLField(verbose_name='رابط المتجر')
    
    # المميزات
    features = models.JSONField(verbose_name='المميزات')
    
    image = models.ImageField(
        upload_to='extensions/', 
        blank=True, 
        verbose_name='الصورة'
    )
    is_active = models.BooleanField(default=True, verbose_name='نشط')
    
    class Meta:
        verbose_name = 'إضافة'
        verbose_name_plural = 'الإضافات'
    
    def __str__(self):
        return self.name


class Review(models.Model):
    """
    نموذج المراجعات - المقالات التقنية
    """
    REVIEW_TYPES = [
        ('device', 'جهاز'),
        ('component', 'مكون'),
        ('extension', 'إضافة'),
        ('comparison', 'مقارنة'),
    ]
    
    title = models.CharField(max_length=300, verbose_name='العنوان')
    slug = models.SlugField(unique=True, verbose_name='الرابط')
    summary = models.TextField(verbose_name='الملخص')
    content = models.TextField(verbose_name='المحتوى')
    
    # النوع والارتباط
    review_type = models.CharField(
        max_length=20, 
        choices=REVIEW_TYPES, 
        verbose_name='نوع المراجعة'
    )
    device = models.ForeignKey(
        Device, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name='الجهاز'
    )
    component = models.ForeignKey(
        Component, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name='المكون'
    )
    extension = models.ForeignKey(
        Extension, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name='الإضافة'
    )
    
    # الوسائط
    featured_image = models.ImageField(
        upload_to='reviews/', 
        verbose_name='الصورة المميزة'
    )
    
    # التقييم
    overall_score = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        verbose_name='التقييم العام'
    )
    
    # الحالة
    is_published = models.BooleanField(default=False, verbose_name='منشور')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'مراجعة'
        verbose_name_plural = 'المراجعات'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
