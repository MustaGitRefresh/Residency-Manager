from django.contrib import admin
from .models import ExpenseModel

# Register your models here.


@admin.register(ExpenseModel)
class ExpenseModelAdmin(admin.ModelAdmin):
    class Meta:
        fields = "__all__"
