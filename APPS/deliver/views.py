from django.db.models import Avg, Max, Min
from django.shortcuts import render, redirect
# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import DeliveryTasks, DeliveryItems, TemperatureLog, DispatchOrders
def query(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@require_http_methods(["GET"])
def search_view(request):
    """渲染物流查询页面"""
    error = request.GET.get('error', '')
    return render(request, 'deliver/deliver_search.html', {'error': error})


def result_view(request):
    """处理查询请求并展示结果"""
    if request.method == 'GET':
        delivery_id = request.GET.get('delivery_id')

        if not delivery_id:
            return redirect('delivery-search', error='请输入配送ID')

        try:
            # 查询主任务信息
            task = DeliveryTasks.objects.get(delivery_id=delivery_id)

            # 查询关联数据
            items = DeliveryItems.objects.filter(delivery_id=delivery_id)
            temperature_logs = TemperatureLog.objects.filter(
                delivery_id=delivery_id
            ).order_by('-time')[:10]

            # 计算温度统计数据
            temp_stats = temperature_logs.aggregate(
                min_temp=Min('temperature'),
                max_temp=Max('temperature'),
                avg_temp=Avg('temperature')
            )

            dispatch_orders = DispatchOrders.objects.filter(delivery_id=delivery_id)

            return render(request, 'deliver/deliver_result.html', {
                'task': task,
                'items': items,
                'temperature_logs': temperature_logs,
                'temp_stats': temp_stats,
                'dispatch_orders': dispatch_orders,
            })

        except ObjectDoesNotExist:
            return redirect('delivery-search', error=f'配送任务 {delivery_id} 不存在')
        except Exception as e:
            return redirect('delivery-search', error=f'查询出错: {str(e)}')

    # 如果不是GET请求，重定向到查询页面
    return redirect('delivery-search')