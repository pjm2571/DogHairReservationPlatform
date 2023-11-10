from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from doglist.models import Doglist_Dog
from reservation.models import Reservation
from storemap.models import Store
from user.models import User, Dog
import re


def Logout(request):
    request.session.flush()
    return redirect('/')


class Mypage(APIView):
    def get(self, request):
        context = {}
        # Session 이용하여 유저 정보 가져옴
        email = request.session['email']
        user = User.objects.filter(email=email).first()

        # 강아지 정보 가져옴
        dogs = Dog.objects.filter(user=user)

        context['user'] = user
        context['dogs'] = dogs

        return render(request, 'user/mypage.html', context)

    def post(self, request):
        return render(request, 'user/mypage.html')


class Addmydog(APIView):
    def get(self, request):
        context = {}

        breed = request.GET.get('breed')

        if breed == None:
            return render(request, 'user/addmydog.html')

        context['breed'] = breed

        return render(request, 'user/addmydog.html', context)

    def post(self, request):
        name = request.data.get('name')
        sex = request.data.get('sex')
        breed = request.data.get('breed')
        birth = request.data.get('birth')

        # 공백 check
        if name == "":
            return Response(status=500, data=dict(message='반려견의 이름을 입력해주세요.'))
        if sex == None:
            return Response(status=500, data=dict(message='반려견의 성별을 선택해주세요.'))
        if breed == "":
            return Response(status=500, data=dict(message='견종을 입력해주세요.'))
        if birth == "":
            return Response(status=500, data=dict(message='반려견의 생일을 입력해주세요.'))

        # Session 이용하여 유저 정보 가져옴
        email = request.session['email']
        user = User.objects.filter(email=email).first()

        dogs = Dog.objects.filter(user=user)

        for doggy in dogs:
            if doggy.name == name:
                return Response(status=500, data=dict(message='동일한 반려견이 존재합니다. 반려견 이름을 확인해주세요.'))

        dogsize = Doglist_Dog.objects.filter(kind_kor=breed).first().kind_size

        dog = Dog.objects.create(
            user=user,
            name=name,
            sex=sex,
            birth=birth,
            breed=breed,
            size=dogsize
        )

        return Response(status=200, data=dict(message='반려견 등록에 성공했습니다. 추가 반려견이 있다면, 마이페이지에서 등록해주세요.'))


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

        # 접속한 사람의 nicknname도 설정
        request.session['nickname'] = user.nickname

        return Response(status=200, data=dict(message='로그인에 성공했습니다.'))


class Join(APIView):
    def get(self, request):
        return render(request, 'user/join.html')

    def post(self, request):
        email = request.data.get('email')
        name = request.data.get('name')
        nickname = request.data.get('nickname')
        raw_password = request.data.get('raw_password')
        password = request.data.get('password')

        # 공백 check
        if email == "":
            return Response(status=500, data=dict(message='이메일을 입력해주세요.'))
        if nickname == "":
            return Response(status=500, data=dict(message='닉네임을 입력해주세요.'))
        if name == "":
            return Response(status=500, data=dict(message='이름을 입력해주세요.'))
        if raw_password == "":
            return Response(status=500, data=dict(message='비밀번호를 입력해주세요.'))
        if password == "":
            return Response(status=500, data=dict(message='비밀번호를 한 번 더 입력해주세요.'))

        # 이메일의 형식에 맞게 적용하는지 확인
        if not re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[.]?\w{2,3}$', email):
            return Response(status=500, data=dict(message='올바른 이메일 양식을 입력해주세요.'))

        # 회원가입 시, email 중복 여부 database 접속 없이 파악
        if User.objects.filter(email=email).exists():
            return Response(status=500, data=dict(message='해당 이메일 주소가 존재합니다.'))

        # 회원가입 시, nickname 중복 여부 databse 접속 없이 파악
        elif User.objects.filter(nickname=nickname).exists():
            return Response(status=500, data=dict(message='사용자 이름 "' + nickname + '"이(가) 존재합니다.'))

        # 회원가입 시, password 확인
        if raw_password != password:
            return Response(status=500, data=dict(message='비밀번호가 일치하지 않습니다. 비밀번호를 확인해주세요.'))

        User.objects.create(password=make_password(password),
                            email=email,
                            name=name,
                            nickname=nickname)
        return Response(status=200, data=dict(message="회원가입 성공했습니다. 로그인해주세요."))


class verifyEmail(APIView):
    def post(self, request):
        email = request.data.get('email')

        # 이메일이 공백일 경우
        if email == "":
            return Response(status=500, data=dict(message='이메일은 공백이 될 수 없습니다.'))

        # 이메일의 형식에 맞게 적용하는지 확인
        if not re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[.]?\w{2,3}$', email):
            return Response(status=500, data=dict(message='올바른 이메일 양식을 입력해주세요.'))

        # 회원가입 시, email 중복 여부 database 접속 없이 파악
        if User.objects.filter(email=email).exists():
            return Response(status=500, data=dict(message='해당 이메일 주소가 존재합니다.'))

        return Response(status=200, data=dict(message="사용할 수 있는 이메일입니다."))


class verifyNickname(APIView):
    def post(self, request):
        nickname = request.data.get('nickname')

        # 닉네임이 공백인 경우
        if nickname == "":
            return Response(status=500, data=dict(message='닉네임은 공백이 될 수 없습니다.'))

        # 회원가입 시, nickname 중복 여부 databse 접속 없이 파악
        if User.objects.filter(nickname=nickname).exists():
            return Response(status=500, data=dict(message='사용자 이름 "' + nickname + '"이(가) 존재합니다.'))

        return Response(status=200, data=dict(message="사용할 수 있는 닉네임입니다."))


class Reservation_view(APIView):
    def get(self, request):
        context = {}
        # Session 이용하여 유저 정보 가져옴
        email = request.session['email']
        user = User.objects.filter(email=email).first()

        context['user'] = user
        reservations = Reservation.objects.filter(user=user).order_by('date')
        context['reservations'] = reservations

        return render(request, 'user/reservation.html', context)
