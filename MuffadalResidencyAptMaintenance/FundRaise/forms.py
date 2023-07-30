from .models import FundRaiseModel
from django.forms import ModelForm


class FundRaiseForm(ModelForm):
    class Meta:
        model = FundRaiseModel
        fields = "__all__"
