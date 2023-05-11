from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.market_post_list, name='market_post_list'),
    path('market_post/<int:pk>/', views.market_post_detail, name='market_post_detail'),
    path('market_post/new/', views.market_post_create, name='market_post_create'),
    path('market_post/<int:pk>/edit/', views.market_post_edit, name='market_post_edit'),
    path('market_post/<int:pk>/delete/', views.market_post_delete, name='market_post_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

