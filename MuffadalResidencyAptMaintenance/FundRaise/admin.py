from django.contrib import admin
from .models import FundRaiseModel

# Register your models here.


@admin.register(FundRaiseModel)
class FundRaiseAdmin(admin.ModelAdmin):
    class Meta:
        fields = "__all__"
