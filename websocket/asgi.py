"""
ASGI config for websocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os


from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket.settings')
asgi_app = get_asgi_application()

import django
django.setup()
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLResolver, URLRouter
from counter.routing import ws_urls

application = ProtocolTypeRouter({
    'http':asgi_app,
    'websocket':AuthMiddlewareStack(URLRouter(ws_urls))
})

