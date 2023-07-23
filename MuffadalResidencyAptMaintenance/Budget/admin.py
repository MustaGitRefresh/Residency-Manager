from django.contrib import admin
from .models import BudgetModel


# Register your models here.

@admin.register(BudgetModel)
class BudgetModelAdmin(admin.ModelAdmin):
    class Meta:
        fields = "__all__"
