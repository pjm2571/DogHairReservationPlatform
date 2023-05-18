from django.contrib import admin
from django.urls import path, include
from .views import Login, Join, verifyEmail, verifyNickname


urlpatterns = [
    path('login/', Login.as_view()),
    path('join/', Join.as_view()),
    path('join/verifyEmail', verifyEmail.as_view()),
    path('join/verifyNickname', verifyNickname.as_view()),
]
