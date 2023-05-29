from django.urls import path, include

from .views import map, details, maplist

urlpatterns = [
    path('', map, name='map'),
    path('maplist/', maplist, name='maplist'),
    path('details/', details, name='details')
]
