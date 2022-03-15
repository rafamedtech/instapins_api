from django.urls import path
from .views import DownloadImage, UploadImage

app_name = 'uploads'

urlpatterns = [
    path('get/<str:pk>/', DownloadImage.as_view()),
    path('', UploadImage.as_view()),
]