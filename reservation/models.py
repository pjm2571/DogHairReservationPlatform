from django.db import models

from storemap.models import Store
from user.models import User


# Create your models here.

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    menus = models.CharField(max_length=200)
    dog = models.CharField(max_length=255, null=True)
    date = models.DateField(default='2023-06-06')

    class Meta:
        db_table = 'reservation'

    def __str__(self):
        return f"User : {self.user.nickname}, Store ID : {self.store.name}"
