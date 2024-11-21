from django.http import HttpResponse
from django.shortcuts import render
from .models import arts, places

def home(request):
    #return HttpResponse('Hello, World! Home')
    return render(request, 'website/base.html')

def about(request):
    return render(request, 'website/base2.html')

def contact(request):
    data = arts.objects.all()
    data2 = places.objects.all()
    return render(request, 'website/base2.html', {'data': data})