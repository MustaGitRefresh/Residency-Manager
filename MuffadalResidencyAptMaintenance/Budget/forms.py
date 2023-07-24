from django.forms import ModelForm
from .models import BudgetModel


class BudgetForm(ModelForm):
    class Meta:
        model = BudgetModel
        fields = "__all__"
