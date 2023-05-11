from django.db import models

class MarketPost(models.Model):
    title = models.CharField(max_length=200) #게시글 제목
    content = models.TextField() #게시글 내용
    created_at = models.DateTimeField(auto_now_add=True) #게시일자
    updated_at = models.DateTimeField(auto_now=True) #수정일자
    image = models.ImageField(upload_to='images/', blank=True, null=True) #이미지를 추가

    class Meta:
        app_label = 'marketboard'

    def __str__(self):
        return self.title