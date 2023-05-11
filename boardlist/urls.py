from django.contrib import admin
from django.urls import path, include
from .views import  boardlist

urlpatterns = [
    path('', boardlist, name='boardlist'),
    path('boastboard/', include('boastboard.urls')),
    path('marketboard/', include('marketboard.urls')),
    path('reviewboard/', include('reviewboard.urls')),
    path('freeboard/', include('freeboard.urls')),
]
