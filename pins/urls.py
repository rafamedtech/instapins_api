from django.urls import path
from .views import DeleteComment, GetPins, PostPin, DeletePin, CommentPin, LikePin, GetSinglePin, updatePin


app_name = 'pins'

urlpatterns = [
    path('', GetPins.as_view()),
    path('details/<str:pk>/', GetSinglePin.as_view()),
    path('details/<str:pk>/edit/', updatePin.as_view()),
    path('create/', PostPin.as_view()),
    path('delete/<str:pk>/', DeletePin.as_view()),
    path('comment/<str:id>/', CommentPin.as_view()),
    path('comment/<str:id>/<str:pk>/', DeleteComment.as_view()),
    path('like/<str:id>/', LikePin.as_view()),
]   