from django.urls import path

from . import views

urlpatterns = [
    path('', views.GetCountryCode, name='Get Country Code'),
    path('generate/', views.GenerateExcel, name='Generate Excel'),
    path('upload/', views.UploadFile, name="Upload Excel")
]