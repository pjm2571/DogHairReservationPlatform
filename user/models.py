from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models



class User(AbstractBaseUser):
    # TODO 회원가입
    """
    1) 이름
    2) 이메일
    3) 닉네임
    4) ID -> Default
    5) PW -> Default
    """
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(verbose_name='email', max_length=100, null=True, unique=True)
    nickname = models.CharField(max_length=30, blank=True, null=True, unique=True)

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.nickname

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'user'

class Dog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    breed = models.CharField(max_length=255)
    birth = models.DateField()
    size = models.CharField(max_length=255, default='')
