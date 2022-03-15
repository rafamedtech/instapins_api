from django.urls import path
from .views import GetPins, PostPin, CommentPin


app_name = 'pins'

urlpatterns = [
    path('', GetPins.as_view()),
    path('create/', PostPin.as_view()),
    path('comment/<str:id>/', CommentPin.as_view()),
]