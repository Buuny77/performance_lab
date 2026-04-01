"""
admin.py - تطبيق reviews
إعدادات لوحة التحكم للمراجعات
"""
from django.contrib import admin
from .models import Device, Game, AI_Model, Component, Extension, Review


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'device_type', 'benchmark_score', 'price', 'is_active']
    list_filter = ['device_type', 'brand', 'is_active']
    search_fields = ['name', 'brand', 'model']
    list_editable = ['price', 'is_active']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'genre', 'expected_fps_low', 'expected_fps_high', 'is_active']
    list_filter = ['genre', 'is_active']
    search_fields = ['name']


@admin.register(AI_Model)
class AI_ModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'min_vram', 'rec_vram', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ['name', 'component_type', 'performance_score', 'price', 'is_active']
    list_filter = ['component_type', 'is_active']
    search_fields = ['name', 'brand']


@admin.register(Extension)
class ExtensionAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'rating', 'downloads', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'review_type', 'overall_score', 'is_published', 'created_at']
    list_filter = ['review_type', 'is_published', 'created_at']
    search_fields = ['title', 'summary']
    list_editable = ['is_published']
    date_hierarchy = 'created_at'
