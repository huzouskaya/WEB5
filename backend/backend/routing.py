from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app import routing

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        routing.websocket_urlpatterns
    ),
})
