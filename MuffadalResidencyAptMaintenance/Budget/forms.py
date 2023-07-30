from django import forms


class BudgetForm(forms.Form):
    date = forms.DateField()
    Amount = forms.IntegerField()
