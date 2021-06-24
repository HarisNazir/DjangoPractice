from django.urls import path

from . import views

urlpatterns = [
    path('', views.GetCountryCode, name='Get Country Code'),
]