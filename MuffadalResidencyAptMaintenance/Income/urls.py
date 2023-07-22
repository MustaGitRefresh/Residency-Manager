from django.urls import path
from . import views

urlpatterns = [
    path('income/', views.home),
]