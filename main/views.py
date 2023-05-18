from django.shortcuts import render
from rest_framework.views import APIView

from user.models import User

class Main(APIView):
    def get(self, request):

        # 로그인을 안한 상태로 사이트에 접속했을 경우
        if 'email' not in request.session:
            print('here')
            return render(request, 'user/login.html')

        email = request.session['email']
        # email 세션 정보를 통해 user 인식
        user = User.objects.filter(email=email).first()

        # 유저가 없을 경우
        if user is None:
            return render(request, 'user/login.html')

        return render(request, 'main/main.html', context=dict(user=user))

