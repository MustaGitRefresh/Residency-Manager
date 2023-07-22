from django.db import models


# Create your models here.
class IncomeModel(models.Model):
    flat_no = models.IntegerField(primary_key=True, null=False)
    date = models.DateField()
    Amount = models.IntegerField(default="Not paid")
    maintenance_giver = models.CharField(max_length=30)

