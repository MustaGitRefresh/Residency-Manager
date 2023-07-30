from django.shortcuts import render
from .forms import ExpenseForm


# Create your views here.
def home(request):
    form = ExpenseForm()
    return render(request, 'FundRaise/html/home.html', {"forms": form})
