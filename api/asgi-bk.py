import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from django.core.asgi import get_asgi_application
from chat.consumers import PersonalChatConsumer
import chat.routing
from chat.channelsmiddleware import JwtAuthMiddleware


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': JwtAuthMiddleware(
            URLRouter(
                chat.routing.websocket_urlpatterns

            )
        )
})