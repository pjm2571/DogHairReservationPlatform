# DjangoProject
종설 프로젝트

* 프로젝트 다운받는 법
1) CODE 버튼 클릭
![image](https://github.com/pjm2571/DjangoProject/assets/97939207/07b212d1-17e9-4340-8782-144d4931f7bc)



2) 1번을 누르면 GIT을 통해서 설치.. 복잡음
   2번을 누르면 자동으로 Project가 .zip 형태로 받아짐 .. 이게 좀 쉬운 듯!
   ![image](https://github.com/pjm2571/DjangoProject/assets/97939207/ecee6bbb-56ae-46ba-b84e-cfbe0602d4e8)

  
  
  
3) 알집파일을 압축 풀면 위와 같이 나옴
![image](https://github.com/pjm2571/DjangoProject/assets/97939207/12760725-ef90-4f5e-acb2-273c6260fcd1)



4) 파이참으로 실행법 
- File - Open Folder - ![image](https://github.com/pjm2571/DjangoProject/assets/97939207/e3566c31-7fe3-4297-81f4-d01cd34f1819)




하면 됨

5) VSCODE 실행법
- File - Open Folder - ![image](https://github.com/pjm2571/DjangoProject/assets/97939207/5eb72d21-9433-4068-9b4f-a913230abebb)







* Venv 설정법
1) python -m venv venv --> 가상환경 설정.. 이것까지 commit하는 건 연습중 ㅠㅠ
---- 가상환경 설정은 다들 할 줄 아는걸로 알고 깊게 설명 x [powershell 오류 시 : https://infinitt.tistory.com/43 ] 
2) pip install django
3) python.exe -m pip install --upgrade pip   // 이런 식으로 설치하라고 뜨는데 뭐 선택사항인디.. 난 했음!
4) pip install djangorestframework           // django rest frame work
5) python -m pip install Pillow              // image rendering
----- 까지 설치하면 잘 돌아갈겁니둥


* 사용법
1) Venv까지 잘 설치하고 나면, 터미널 창에 > python manage.py runserver 를 치면 서버가 구동됨.
![image](https://github.com/pjm2571/DjangoProject/assets/97939207/18e6914c-9251-4dfe-9559-f03e73264d7c)

이 화면이 뜨면 성공적으로 실행된 것이고, 해당 주소로 들어가면 됨

2) 주소창에 http://127.0.0.1:8000/main/ 이라고 치면 메인화면

-> 로그인 안했을 시
3) login, join 버튼 보임

-> 로그인 했을 시
3) logout, mypage 버튼보임

4) 게시판 버튼 누르면 게시판으로 이동
5) 맵 버튼 누르면 맵으로 이동





---------------------------------
version 1.2 변경점

병합:
1) login.html & loginStyle.css
2) join.html & joinStyle.css
3) main.html & mainStyle.css

추가:
1) storemap app 추가
2) 네이버 지도 api -> 카카오 맵 api 사용
3) static 폴더 추가

---------------------------------

