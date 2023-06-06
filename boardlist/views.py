from django.shortcuts import render

from user.models import User


def boardlist(request):
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

    return render(request, 'boardlist/boardlist.html', context)
