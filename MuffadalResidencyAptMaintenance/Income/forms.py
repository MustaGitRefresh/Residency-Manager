from django.forms import ModelForm
from .models import IncomeModel


class IncomeForm(ModelForm):
    class Meta:
        model = IncomeModel
        fields = "__all__"
