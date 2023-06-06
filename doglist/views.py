from django.shortcuts import render, redirect
from rest_framework.views import APIView

from doglist.models import Doglist_Dog


# Create your views here.

class Main(APIView):
    def get(self, request):
        context = {}
        dogs = Doglist_Dog.objects.all()
        context['dogs'] = dogs
        return render(request, 'doglist/main.html', context)
    def post(self, request):
        return redirect('user/mypage/addmydog')