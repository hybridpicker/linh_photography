from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_view, name='portfolio_view'),
]
