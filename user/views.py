from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
import re


class Login(APIView):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if email == "":
            return Response(status=500, data=dict(message='이메일을 입력해주세요'))

        if password == "":
            return Response(status=500, data=dict(message='비밀번호를 입력해주세요'))

        # list중 하나를 return하기 위해 .first()
        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=500, data=dict(message='이메일로 가입된 아이디가 없습니다.'))

        if check_password(password, user.password) is False:
            return Response(status=500, data=dict(message='비밀번호가 잘못되었습니다.'))

        request.session['loginCheck'] = True

        # 접속한 사람의 정보를 쉽게 파악하기 위해 email로 설정 -> 하드코딩 불필요
        request.session['email'] = user.email

        return Response(status=200, data=dict(message='로그인에 성공했습니다.'))


class Join(APIView):
    def get(self, request):
        return render(request, 'user/join.html')

    def post(self, request):
        email = request.data.get('email')
        name = request.data.get('name')
        nickname = request.data.get('nickname')
        password = request.data.get('password')

        # 공백 check
        if email == "":
            return Response(status=500, data=dict(message='이메일을 입력해주세요.'))
        if nickname == "":
            return Response(status=500, data=dict(message='닉네임을 입력해주세요.'))
        if name == "":
            return Response(status=500, data=dict(message='이름을 입력해주세요.'))
        if password == "":
            return Response(status=500, data=dict(message='비밀번호를 입력해주세요.'))

        # 이메일의 형식에 맞게 적용하는지 확인
        if not re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[.]?\w{2,3}$', email):
            return Response(status=500, data=dict(message='올바른 이메일 양식을 입력해주세요.'))

        # 회원가입 시, email 중복 여부 database 접속 없이 파악
        if User.objects.filter(email=email).exists():
            return Response(status=500, data=dict(message='해당 이메일 주소가 존재합니다.'))

        # 회원가입 시, nickname 중복 여부 databse 접속 없이 파악
        elif User.objects.filter(nickname=nickname).exists():
            return Response(status=500, data=dict(message='사용자 이름 "' + nickname + '"이(가) 존재합니다.'))

        User.objects.create(password=make_password(password),
                            email=email,
                            name=name,
                            nickname=nickname)
        return Response(status=200, data=dict(message="회원가입 성공했습니다. 로그인해주세요."))
