from django.contrib import admin
from django.urls import path, include

from .views import Main

urlpatterns = [
    path('admin/', admin.site.urls),                # admin 
    path('main/', Main.as_view()),                  # main화면
    path('user/', include('user.urls')),            # 로그인, 회원가입
    path('boardlist/', include('boardlist.urls')),  # 게시판
    path('storemap/', include('storemap.urls')),    # 반려동물미용 맵
]
