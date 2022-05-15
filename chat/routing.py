from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('ws/<int:id>/', consumers.PersonalChatConsumer.as_asgi()),
    # path('ws/<int:id>/', PersonalChatConsumer)
    # re_path(r'^messages/(?P<username>[\w.@+-]+)/$', consumers.ChatConsumer.as_asgi()),
]