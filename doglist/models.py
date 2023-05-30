from django.db import models

# Create your models here.
# Create your models here.
class Dog(models.Model):
    img_src = models.CharField(max_length=300)
    kind_kor = models.CharField(max_length=100)
    kind_eng = models.CharField(max_length=100)

    class Meta:
        db_table = 'doglist_dog'

