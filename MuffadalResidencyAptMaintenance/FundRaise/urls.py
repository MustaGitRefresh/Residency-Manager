from django.urls import path
from . import views

urlpatterns = [
    path('fund-raise/', views.home)
]