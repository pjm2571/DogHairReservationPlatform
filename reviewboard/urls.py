from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.review_post_list, name='review_post_list'),
    path('review_post/<int:pk>/', views.review_post_detail, name='review_post_detail'),
    path('review_post/new/', views.review_post_create, name='review_post_create'),
    path('review_post/<int:pk>/edit/', views.review_post_edit, name='review_post_edit'),
    path('review_post/<int:pk>/delete/', views.review_post_delete, name='review_post_delete'),
    path('like/', views.review_post_like.as_view(), name = 'review_post_like')
 ]


