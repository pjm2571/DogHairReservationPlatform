from django.contrib import admin
from django.urls import path, include
from .views import Login, Join, verifyEmail, verifyNickname, Logout


urlpatterns = [
    path('logout/', Logout, name='Logout'),
    path('login/', Login.as_view(), name='Login'),
    path('join/', Join.as_view(), name='Join'),
    path('join/verifyEmail', verifyEmail.as_view()),
    path('join/verifyNickname', verifyNickname.as_view()),
]
