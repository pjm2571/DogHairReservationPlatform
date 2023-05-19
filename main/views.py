from django.shortcuts import render
from rest_framework.views import APIView

from user.models import User

class Main(APIView):
    def get(self, request):
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

        return render(request, 'main/main.html', context)

