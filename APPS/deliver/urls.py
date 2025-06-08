from django.urls import re_path as url

from . import views
from django.urls import path

app_name = 'deliver'

urlpatterns = [
    path('query/', views.query),
    path('search/', views.search_view, name='delivery-search'),

    # 处理查询请求并显示结果
    path('result/', views.result_view, name='delivery-result'),
]
