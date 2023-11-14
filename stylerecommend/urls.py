from django.urls import path
from .views import getStyleRecommend, calculateStyle

urlpatterns = [
    path('', getStyleRecommend),
    path('calculateStyle/', calculateStyle.as_view()),
]
