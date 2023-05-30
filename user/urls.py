from django.contrib import admin
from django.urls import path, include
from .views import Login, Join, verifyEmail, verifyNickname, Logout, Mypage, Addmydog


urlpatterns = [
    path('logout/', Logout, name='Logout'),
    path('login/', Login.as_view(), name='Login'),
    path('join/', Join.as_view(), name='Join'),
    path('mypage/', Mypage.as_view(), name='Mypage'),
    path('mypage/addmydog', Addmydog.as_view(), name='Addmydog'),
    path('join/verifyEmail', verifyEmail.as_view()),
    path('join/verifyNickname', verifyNickname.as_view()),
]
