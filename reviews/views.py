"""
views.py - تطبيق reviews
المراجعات التقنية للأجهزة والمكونات
"""
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Review, Device, Component, Extension


def reviews_index(request):
    """
    الصفحة الرئيسية للمراجعات - تعرض جميع المراجعات
    """
    reviews_list = Review.objects.filter(is_published=True).order_by('-created_at')
    paginator = Paginator(reviews_list, 9)  # 9 مراجعات في كل صفحة
    
    page_number = request.GET.get('page')
    reviews = paginator.get_page(page_number)
    
    context = {
        'page_title': 'المراجعات - Performance Lab',
        'page_description': 'مراجعات تقنية شاملة للأجهزة والمكونات',
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)


def laptop_reviews(request):
    """
    مراجعات اللابتوبات - تركز على أداء التطوير والألعاب
    """
    laptops = Device.objects.filter(
        device_type='laptop',
        is_active=True
    ).order_by('-benchmark_score')
    
    context = {
        'page_title': 'مراجعات اللابتوبات - Performance Lab',
        'page_description': 'أفضل اللابتوبات للمطورين واللاعبين',
        'laptops': laptops,
    }
    return render(request, 'reviews/laptops.html', context)


def handheld_reviews(request):
    """
    مراجعات أجهزة اليد المحمولة
    """
    handhelds = Device.objects.filter(
        device_type='handheld',
        is_active=True
    ).order_by('-benchmark_score')
    
    context = {
        'page_title': 'أجهزة اليد - Performance Lab',
        'page_description': 'أفضل أجهزة اليد المحمولة للألعاب',
        'handhelds': handhelds,
    }
    return render(request, 'reviews/handhelds.html', context)


def component_reviews(request):
    """
    مراجعات المكونات - معالجات، كروت شاشة، ذاكرة
    """
    components = Component.objects.filter(
        is_active=True
    ).order_by('-performance_score')
    
    context = {
        'page_title': 'المكونات - Performance Lab',
        'page_description': 'مراجعات المكونات والعتاد الداخلي',
        'components': components,
    }
    return render(request, 'reviews/components.html', context)


def extension_reviews(request):
    """
    مراجعات إضافات VS Code وأدوات المطورين
    """
    extensions = Extension.objects.filter(
        is_active=True
    ).order_by('-rating')
    
    context = {
        'page_title': 'أدوات المطورين - Performance Lab',
        'page_description': 'أفضل إضافات VS Code وأدوات الأتمتة',
        'extensions': extensions,
    }
    return render(request, 'reviews/extensions.html', context)


def review_detail(request, review_id):
    """
    صفحة تفاصيل المراجعة
    """
    review = get_object_or_404(Review, id=review_id, is_published=True)
    
    context = {
        'page_title': f'{review.title} - Performance Lab',
        'page_description': review.summary,
        'review': review,
    }
    return render(request, 'reviews/detail.html', context)
