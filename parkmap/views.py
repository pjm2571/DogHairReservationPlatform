import json

from django.shortcuts import render

from parkmap.models import Park

def map(request):
    parks = Park.objects.all()
    context = {'parks': parks}
    return render(request, 'parkmap/main.html', context)

def details(request):
    return render(request, 'parkmap/details.html')
