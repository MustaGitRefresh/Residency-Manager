from django.db import models
from Income.models import IncomeModel


# Create your models here.
class BudgetModel(IncomeModel):
    date = IncomeModel.date
    Amount = IncomeModel.Amount

