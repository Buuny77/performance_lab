#!/usr/bin/env python
"""
سكربت لإنشاء بيانات اختبارية للموقع
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'performance_lab.settings')
django.setup()

from reviews.models import Device, Game, AI_Model, Component, Extension, Review


def create_sample_data():
    print("جاري إنشاء البيانات الاختبارية...")
    
    # إنشاء أجهزة
    devices = [
        {
            'name': 'ROG Strix G15',
            'brand': 'ASUS',
            'model': 'G513',
            'device_type': 'laptop',
            'processor': 'AMD Ryzen 9 5900HX',
            'ram': '32GB DDR4',
            'storage': '1TB NVMe SSD',
            'gpu': 'NVIDIA RTX 3070 8GB',
            'display': '15.6" FHD 300Hz',
            'battery': '90Wh',
            'benchmark_score': 18500,
            'gaming_score': 95,
            'ai_score': 85,
            'dev_score': 90,
            'price': 7500,
        },
        {
            'name': 'Legion 5 Pro',
            'brand': 'Lenovo',
            'model': '16ACH6',
            'device_type': 'laptop',
            'processor': 'AMD Ryzen 7 5800H',
            'ram': '16GB DDR4',
            'storage': '512GB NVMe SSD',
            'gpu': 'NVIDIA RTX 3060 6GB',
            'display': '16" QHD 165Hz',
            'battery': '80Wh',
            'benchmark_score': 16200,
            'gaming_score': 88,
            'ai_score': 78,
            'dev_score': 85,
            'price': 5500,
        },
        {
            'name': 'Steam Deck',
            'brand': 'Valve',
            'model': 'LCD 512GB',
            'device_type': 'handheld',
            'processor': 'AMD APU Zen 2',
            'ram': '16GB LPDDR5',
            'storage': '512GB NVMe SSD',
            'gpu': 'AMD RDNA 2 8CU',
            'display': '7" LCD 1280x800',
            'battery': '40Wh',
            'benchmark_score': 8500,
            'gaming_score': 75,
            'ai_score': 45,
            'dev_score': 60,
            'price': 2400,
        },
    ]
    
    for device_data in devices:
        Device.objects.get_or_create(
            name=device_data['name'],
            brand=device_data['brand'],
            defaults=device_data
        )
    
    print(f"تم إنشاء {len(devices)} جهاز")
    
    # إنشاء ألعاب
    games = [
        {
            'name': 'Cyberpunk 2077',
            'genre': 'RPG',
            'min_processor': 'Intel Core i5-3570K',
            'min_ram': '8GB',
            'min_gpu': 'NVIDIA GTX 970',
            'rec_processor': 'Intel Core i7-4790',
            'rec_ram': '12GB',
            'rec_gpu': 'NVIDIA RTX 2060',
            'expected_fps_low': 30,
            'expected_fps_high': 60,
        },
        {
            'name': 'Elden Ring',
            'genre': 'Action RPG',
            'min_processor': 'Intel Core i5-8400',
            'min_ram': '12GB',
            'min_gpu': 'NVIDIA GTX 1060',
            'rec_processor': 'Intel Core i7-8700K',
            'rec_ram': '16GB',
            'rec_gpu': 'NVIDIA RTX 2070',
            'expected_fps_low': 45,
            'expected_fps_high': 60,
        },
    ]
    
    for game_data in games:
        Game.objects.get_or_create(
            name=game_data['name'],
            defaults=game_data
        )
    
    print(f"تم إنشاء {len(games)} لعبة")
    
    # إنشاء نماذج AI
    ai_models = [
        {
            'name': 'Stable Diffusion XL',
            'description': 'نموذج توليد صور متقدم',
            'min_vram': 8,
            'rec_vram': 12,
            'min_ram': 16,
            'inference_speed_slow': '5-10 ثواني/صورة',
            'inference_speed_fast': '1-3 ثواني/صورة',
        },
        {
            'name': 'LLaMA 2 7B',
            'description': 'نموذج لغوي كبير',
            'min_vram': 6,
            'rec_vram': 8,
            'min_ram': 16,
            'inference_speed_slow': '20-30 رمز/ثانية',
            'inference_speed_fast': '50-100 رمز/ثانية',
        },
    ]
    
    for model_data in ai_models:
        AI_Model.objects.get_or_create(
            name=model_data['name'],
            defaults=model_data
        )
    
    print(f"تم إنشاء {len(ai_models)} نموذج AI")
    
    # إنشاء مكونات
    components = [
        {
            'name': 'RTX 4090',
            'brand': 'NVIDIA',
            'component_type': 'gpu',
            'specs': {'vram': '24GB', 'cuda_cores': 16384, 'tdp': 450},
            'performance_score': 100,
            'price': 5500,
        },
        {
            'name': 'Ryzen 9 7950X',
            'brand': 'AMD',
            'component_type': 'cpu',
            'specs': {'cores': 16, 'threads': 32, 'base_clock': '4.5GHz'},
            'performance_score': 98,
            'price': 2800,
        },
    ]
    
    for component_data in components:
        Component.objects.get_or_create(
            name=component_data['name'],
            defaults=component_data
        )
    
    print(f"تم إنشاء {len(components)} مكون")
    
    # إنشاء إضافات
    extensions = [
        {
            'name': 'GitLens',
            'description': 'إضافة متقدمة لـ Git في VS Code',
            'category': 'التحكم بالإصدار',
            'rating': 4.8,
            'downloads': 25000000,
            'marketplace_link': 'https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens',
            'features': ['تاريخ Git', 'مقارنة الإصدارات', 'البحث في Git'],
        },
        {
            'name': 'Prettier',
            'description': 'منسق أكواد تلقائي',
            'category': 'التنسيق',
            'rating': 4.7,
            'downloads': 35000000,
            'marketplace_link': 'https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode',
            'features': ['تنسيق تلقائي', 'دعم لغات متعددة', 'قابل للتخصيص'],
        },
    ]
    
    for extension_data in extensions:
        Extension.objects.get_or_create(
            name=extension_data['name'],
            defaults=extension_data
        )
    
    print(f"تم إنشاء {len(extensions)} إضافة")
    
    print("\nتم إنشاء جميع البيانات الاختبارية بنجاح!")


if __name__ == '__main__':
    create_sample_data()
