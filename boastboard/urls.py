from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.boast_post_list, name='boast_post_list'),
    path('boast_post/<int:pk>/', views.boast_post_detail, name='boast_post_detail'),
    path('boast_post/new/', views.boast_post_create, name='boast_post_create'),
    path('boast_post/<int:pk>/edit/', views.boast_post_edit, name='boast_post_edit'),
    path('boast_post/<int:pk>/delete/', views.boast_post_delete, name='boast_post_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

