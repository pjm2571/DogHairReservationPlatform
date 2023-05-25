from django.db import models

# Create your models here.
class Park(models.Model):
    # TODO 공원 등록
    """
    1) 공원 이름
    2) 공원 위치

    --- 위도, 경도 쉽게 처리를 위해 추가하자 ---
    3) 위도 [latitude]
    4) 경도 [longitude]
    """
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    latitude = models.CharField(max_length=50, default='')
    longitude = models.CharField(max_length=50, default='')
