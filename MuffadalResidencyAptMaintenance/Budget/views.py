from django.shortcuts import render
from . import forms


# Create your views here.
def home(request):
    form = forms.BudgetForm()
    return render(request, "Budget/html/forms.html", {"forms": form})
