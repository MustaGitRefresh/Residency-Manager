from django.db import models


# Create your models here.

class UserRecord(models.Model):
    flat_number = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_phone_number = models.IntegerField()
