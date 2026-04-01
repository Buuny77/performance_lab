"""
روابط تطبيق reviews - المراجعات التقنية
"""
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.reviews_index, name='index'),  # صفحة المراجعات الرئيسية
    path('laptops/', views.laptop_reviews, name='laptops'),  # مراجعات اللابتوبات
    path('handhelds/', views.handheld_reviews, name='handhelds'),  # أجهزة اليد
    path('components/', views.component_reviews, name='components'),  # المكونات
    path('extensions/', views.extension_reviews, name='extensions'),  # إضافات VS Code
    path('detail/<int:review_id>/', views.review_detail, name='detail'),  # تفاصيل مراجعة
]
