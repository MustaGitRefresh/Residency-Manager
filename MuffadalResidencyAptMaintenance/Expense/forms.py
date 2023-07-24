from django.forms import ModelForm
from .models import ExpenseModel


class ExpenseForm(ModelForm):
    class Meta:
        model = ExpenseModel
        fields = "__all__"
