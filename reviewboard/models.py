from django.db import models
from user.models import User
from main.views import Main
#from reviewboard import views

class ReviewPost(models.Model):
    title = models.CharField(max_length=200) #게시글 제목
    content = models.TextField() #게시글 내용
    created_at = models.DateTimeField(auto_now_add=True) #게시일자
    updated_at = models.DateTimeField(auto_now=True) #수정일자
    author = models.CharField(max_length=50, null=True, default='') #게시글 작성자
    imgfile = models.ImageField(null=True, upload_to="", blank=True) #이미지, [upload_to="", ]는 MEDIA_ROOT를 의미
    liked_num = models.IntegerField(default='0') # 좋아요 수

    class Meta:
        app_label = 'reviewboard'

    def __str__(self):
        return self.title

class Recommended_ReviewPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(ReviewPost, on_delete=models.CASCADE)

    class Meta:
        app_label = 'reviewboard'

    def __str__(self):
        return f"User : {self.user.nickname}, Post ID : {self.post.id}"
