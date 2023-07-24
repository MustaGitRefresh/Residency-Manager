from django.forms import ModelForm
from .models import FundRaiseModel


class FundRaiseForm(ModelForm):
    class Meta:
        model = FundRaiseModel
        fields = "__all__"
