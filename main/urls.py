from main.models import MonthlyDataUpload
from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'MonthlyDataUpload', views.MonthlyDataUploadViewSet)

urlpatterns = [
    path('', views.GetCountryCode, name='Get Country Code'),
    path('generate/', views.GenerateExcel, name='Generate Excel'),
    path('upload/', views.UploadFile, name="Upload Excel"),
    path('uploadscreen/',views.UploadScreen.as_view(), name="Upload Screen"),
    path('/api', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))
]