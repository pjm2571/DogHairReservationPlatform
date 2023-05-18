from django.db import models
import csv

# Create your models here.
class Store(models.Model):
    # TODO 가게 등록
    """
    1) 가게 이름
    2) 가게 위치
    3) 오픈 시간
    4) 전화번호
    5) 별점
    6) 방문자 리뷰
    7) 블로그 리뷰
    8) 홈페이지 주소

    --- 위도, 경도 쉽게 처리를 위해 추가하자 ---
    9) 위도 [latitude]
    10) 경도 [longitude]
    """
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    open_hours = models.TextField()
    phone_number = models.CharField(max_length=20)
    rating = models.CharField(max_length=50)
    visitor_review = models.CharField(max_length=20)
    blog_review = models.CharField(max_length=20)
    website = models.TextField()

    latitude = models.CharField(max_length=50, default='')
    longitude = models.CharField(max_length=50, default='')
