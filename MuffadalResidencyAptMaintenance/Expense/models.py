from django.db import models

# Create your models here.


class ExpenseModel(models.Model):
    EXPENSE_TYPES = [
        ('RC', 'Recreational',),
        ('ELC', 'Electricity',),
        ('LM', 'Lift_maintain',),
    ]
    Exp_date = models.DateField()
    Exp_type = models.CharField(max_length=30, choices=EXPENSE_TYPES)
    Amt = models.IntegerField()
