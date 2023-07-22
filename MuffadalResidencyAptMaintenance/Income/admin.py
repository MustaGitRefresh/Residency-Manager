from django.contrib import admin
from .models import IncomeModel


# Register your models here.
@admin.register(IncomeModel)
class IncomeAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['flat_no', 'date', "Amount", "maintenance_giver", "number"]
        fields = "__all__"
