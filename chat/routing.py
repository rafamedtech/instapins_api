from django.urls import re_path
from django.urls import path

from .consumers import PersonalChatConsumer

websocket_urlpatterns = [
    path('ws/<int:id>/', PersonalChatConsumer.as_asgi()),
    # path('ws/<int:id>/', PersonalChatConsumer)
    # re_path(r'^messages/(?P<username>[\w.@+-]+)/$', consumers.ChatConsumer.as_asgi()),
]