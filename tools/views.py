"""
views.py - تطبيق tools
الأدوات التفاعلية للموقع
"""
from django.shortcuts import render
from django.http import JsonResponse
from reviews.models import Device, Game, AI_Model
import json


def tools_index(request):
    """
    صفحة الأدوات الرئيسية - تعرض جميع الأدوات المتاحة
    """
    context = {
        'page_title': 'الأدوات - Performance Lab',
        'page_description': 'أدوات تفاعلية لقياس وتحليل أداء الأجهزة',
    }
    return render(request, 'tools/index.html', context)


def will_it_run(request):
    """
    أداة "هل يعمل؟" - تتحقق من توافق الجهاز مع الألعاب أو نماذج الذكاء الاصطناعي
    """
    devices = Device.objects.filter(is_active=True)
    games = Game.objects.filter(is_active=True)
    ai_models = AI_Model.objects.filter(is_active=True)
    
    context = {
        'page_title': 'هل يعمل؟ - Performance Lab',
        'page_description': 'تحقق مما إذا كان جهازك قادراً على تشغيل الألعاب أو نماذج الذكاء الاصطناعي',
        'devices': devices,
        'games': games,
        'ai_models': ai_models,
    }
    return render(request, 'tools/will_it_run.html', context)


def compare_devices(request):
    """
    أداة مقارنة الأجهزة - مقارنة جانبية بين أجهزة مختلفة
    """
    devices = Device.objects.filter(is_active=True)
    
    context = {
        'page_title': 'مقارنة الأجهزة - Performance Lab',
        'page_description': 'قارن بين الأجهزة المختلفة لاختيار الأنسب لك',
        'devices': devices,
    }
    return render(request, 'tools/compare.html', context)


def analyze_performance(request):
    """
    أداة تحليل الأداء - تحليل تفصيلي لأداء الجهاز
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            device_id = data.get('device_id')
            workload_type = data.get('workload_type')  # 'gaming', 'ai', 'development'
            
            # هنا يمكن إضافة منطق التحليل الفعلي
            device = Device.objects.get(id=device_id)
            
            result = {
                'status': 'success',
                'device_name': device.name,
                'workload_type': workload_type,
                'estimated_fps': 60,  # قيمة افتراضية
                'recommendation': 'مناسب جداً',
            }
            return JsonResponse(result)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    devices = Device.objects.filter(is_active=True)
    context = {
        'page_title': 'تحليل الأداء - Performance Lab',
        'page_description': 'تحليل مفصل لأداء جهازك',
        'devices': devices,
    }
    return render(request, 'tools/analyze.html', context)
