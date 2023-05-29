import json

from django.shortcuts import render

from parkmap.models import Park
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
    parks = Park.objects.all()
    context['parks'] = parks
    return render(request, 'parkmap/main.html', context)


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

    parks = Park.objects.all()
    context['parks'] = parks

    return render(request, 'parkmap/maplist.html', context)


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

    park_title = request.GET.get('title')

    park = Park.objects.filter(title=park_title).first()
    context['park'] = park

    return render(request, 'parkmap/details.html', context)
