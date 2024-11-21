from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse('Hello, World! Home')
    return render(request, 'website/base.html')

def about(request):
    return render(request, 'website/base2.html')

def contact(request):
    return HttpResponse('Hello, World!  Contact') 