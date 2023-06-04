from django.db import models

from user.models import User


class FreePost(models.Model):
    title = models.CharField(max_length=200) #게시글 제목
    content = models.TextField() #게시글 내용
    created_at = models.DateTimeField(auto_now_add=True) #게시일자
    updated_at = models.DateTimeField(auto_now=True) #수정일자
    author = models.CharField(max_length=50, null=True, default='')  # 게시글 작성자
    image = models.ImageField(upload_to='images/', blank=True, null=True) #이미지를 추가
    liked_num = models.IntegerField(default='0')

    class Meta:
        app_label = 'freeboard'

    def __str__(self):
        return self.title


class Recommended_FreePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(FreePost, on_delete=models.CASCADE)

    class Meta:
        app_label = 'freeboard'

    def __str__(self):
        return f"User : {self.user.nickname}, Post ID : {self.post.id}"