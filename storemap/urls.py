from django.urls import path, include

from .views import map

urlpatterns = [
    path('', map, name='map'),
]
