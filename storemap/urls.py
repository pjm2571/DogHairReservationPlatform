from django.urls import path, include

from .views import map, details

urlpatterns = [
    path('', map, name='map'),
    path('details/', details, name='details')
]
