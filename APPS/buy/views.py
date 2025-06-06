from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    print(request.method)
    print(request.path)
    return HttpResponse('Hello World!')