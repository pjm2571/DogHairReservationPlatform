from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.freeboard_post_list, name='freeboard_post_list'),
    path('freeboard_post/<int:pk>/', views.freeboard_post_detail, name='freeboard_post_detail'),
    path('freeboard_post/new/', views.freeboard_post_create, name='freeboard_post_create'),
    path('freeboard_post/<int:pk>/edit/', views.freeboard_post_edit, name='freeboard_post_edit'),
    path('freeboard_post/<int:pk>/delete/', views.freeboard_post_delete, name='freeboard_post_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

