from django.urls import path
from .views import RegisterUserView, LogoutUserView, GetUserView, GetAllUsers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', GetAllUsers.as_view()),
    path('user/', GetUserView.as_view()),
    path('register/', RegisterUserView.as_view()),
    path('logout/', LogoutUserView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]