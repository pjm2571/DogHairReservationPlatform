from django.contrib import admin
from django.urls import path, include

from .views import Main

urlpatterns = [
    path('admin/', admin.site.urls),                # admin 
    path('', Main.as_view()),                       # main화면
    path('user/', include('user.urls')),            # 로그인, 회원가입
    path('boardlist/', include('boardlist.urls')),  # 게시판
    path('storemap/', include('storemap.urls')),    # 반려동물미용 맵
    path('chatgpt/',include('gptjango.urls')),      # chatgpt
    path('parkmap/', include('parkmap.urls')),      # 공원 맵
    path('doglist/', include('doglist.urls')),      # 견종 리스트
]
