from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from reservation.models import Reservation
from storemap.models import Store
from user.models import User, Dog


# Create your views here.

class main(APIView):
    def get(self, request):
        context = {}

        store_id = request.GET.get('store_id')
        user_id = request.GET.get('user_id')
        user = User.objects.filter(id=user_id).first()
        store = Store.objects.filter(id=store_id).first()
        dogs = Dog.objects.filter(user=user)

        context['dogs'] = dogs
        context['store'] = store
        context['user'] = user

        return render(request, 'reservation/main.html', context)

    def post(self, request):
        user_id = request.data.get('user_id', None)
        store_id = request.data.get('store_id', None)
        menus = request.data.get('menus', None)
        date = request.data.get('date', None)
        price = request.data.get('price', None)
        dog = request.data.get('dog', None)

        user = User.objects.filter(id=user_id).first()
        store = Store.objects.filter(id=store_id).first()

        # 이미 존재하는 경우 오류 처리
        if Reservation.objects.filter(user=user, store=store, date=date, dog=dog).exists():
            return Response(status=400, data=dict(message="이미 예약이 되었습니다."))


        Reservation.objects.create(
            user=user,
            store=store,
            menus=menus,
            date=date,
            price=price,
            dog=dog
        )

        return Response(status=200, data=dict(message="예약이 완료되었습니다."))
