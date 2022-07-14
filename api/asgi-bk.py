# import os
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import re_path
# from django.core.asgi import get_asgi_application
# # from chat.consumers import PersonalChatConsumer
# import chat.routing
# from chat.channelsmiddleware import JwtAuthMiddleware
# # from chat.middleware import UserAuthMiddleware


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': JwtAuthMiddleware(
#             URLRouter(
#                 chat.routing.websocket_urlpatterns,
#             )
#         )
# })

"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

application = get_asgi_application()
