from django.urls import path
from .views import DeleteImage, UploadImage

app_name = 'uploads'

urlpatterns = [
    
    path('delete/<str:pk>/', DeleteImage.as_view()),
    path('', UploadImage.as_view()),
]