import json

from django.shortcuts import render

from storemap.models import Store
from user.models import User


def map(request):
    context = {}
    loginCheck = request.session.get('loginCheck', '')

    if loginCheck == '':
        context['loginCheck'] = False
        context['user'] = None
    else:
        context['loginCheck'] = True
        email = request.session['email']
        user = User.objects.filter(email=email).first()
        context['user'] = user

    stores = Store.objects.all()
    context['stores'] = stores
    return render(request, 'storemap/main.html', context)

def maplist(request):
    context = {}
    loginCheck = request.session.get('loginCheck', '')

    if loginCheck == '':
        context['loginCheck'] = False
        context['user'] = None
    else:
        context['loginCheck'] = True
        email = request.session['email']
        user = User.objects.filter(email=email).first()
        context['user'] = user

    stores = Store.objects.all()
    context['stores'] = stores

    return render(request, 'storemap/maplist.html', context)

def details(request):
    context = {}
    loginCheck = request.session.get('loginCheck', '')

    if loginCheck == '':
        context['loginCheck'] = False
        context['user'] = None
    else:
        context['loginCheck'] = True
        email = request.session['email']
        user = User.objects.filter(email=email).first()
        context['user'] = user

    store_title = request.GET.get('title')

    store = Store.objects.filter(name=store_title).first()
    context['store'] = store
    return render(request, 'storemap/details.html', context)
