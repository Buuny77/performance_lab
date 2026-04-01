"""
views.py - تطبيق main
الصفحات الرئيسية للموقع
"""
from django.shortcuts import render
from django.http import JsonResponse
from reviews.models import Review, Device


def home(request):
    """
    الصفحة الرئيسية - تعرض Hero Section وأحدث المراجعات والأدوات
    """
    # جلب آخر 3 مراجعات
    latest_reviews = Review.objects.filter(is_published=True).order_by('-created_at')[:3]
    
    # جلب أفضل الأجهزة أداءً
    top_devices = Device.objects.filter(is_active=True).order_by('-benchmark_score')[:4]
    
    context = {
        'latest_reviews': latest_reviews,
        'top_devices': top_devices,
        'page_title': 'Performance Lab - مختبر الأداء',
        'page_description': 'مراجعات تقنية قائمة على البيانات للألعاب والبرمجة',
    }
    return render(request, 'main/home.html', context)


def about(request):
    """
    صفحة من نحن - تعرض معلومات عن الموقع
    """
    context = {
        'page_title': 'من نحن - Performance Lab',
        'page_description': 'تعرف على فريق Performance Lab ورسالتنا',
    }
    return render(request, 'main/about.html', context)


def contact(request):
    """
    صفحة اتصل بنا - نموذج للتواصل
    """
    context = {
        'page_title': 'اتصل بنا - Performance Lab',
        'page_description': 'تواصل مع فريق Performance Lab',
    }
    return render(request, 'main/contact.html', context)
