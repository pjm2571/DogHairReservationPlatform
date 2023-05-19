import json

from django.shortcuts import render

from storemap.models import Store

def map(request):
    stores = Store.objects.all()
    context = {'stores': stores}
    return render(request, 'storemap/main.html', context)

def details(request):
    return render(request, 'storemap/details.html')
