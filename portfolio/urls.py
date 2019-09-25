from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_view, name='portfolio_view'),
    path('about', views.about_view, name='about_view'),
    path('contact', views.contact_view, name='contact_view'),
    path('site_notice', views.site_notice_view, name='site_notice_view'),
    path('faq', views.faq_view, name='faq_view'),
]
