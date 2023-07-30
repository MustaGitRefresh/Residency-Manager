from django.shortcuts import render
from . import forms


# Create your views here.
def home(request):
    form = forms.FundRaiseForm()
    return render(request, "FundRaise/html/home.html", {"forms": form})
