from django.urls import path
from .views import MessageAPIView


urlpatterns = [
    path('', MessageAPIView.as_view()),
    path('<str:username>/', MessageAPIView.as_view()),
]