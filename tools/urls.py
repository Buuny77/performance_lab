"""
روابط تطبيق tools - الأدوات التفاعلية
"""
from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('', views.tools_index, name='index'),  # صفحة الأدوات الرئيسية
    path('will-it-run/', views.will_it_run, name='will_it_run'),  # أداة "هل يعمل؟"
    path('compare/', views.compare_devices, name='compare'),  # مقارنة الأجهزة
    path('analyze/', views.analyze_performance, name='analyze'),  # تحليل الأداء
]
