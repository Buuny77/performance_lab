"""
روابط تطبيق main - الصفحات الرئيسية
"""
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),  # الصفحة الرئيسية
    path('about/', views.about, name='about'),  # من نحن
    path('contact/', views.contact, name='contact'),  # اتصل بنا
]
