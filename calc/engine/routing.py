from django.urls import path
from .consumers import PensionConsumer


ws_urlpatterns = [
    path("ws/pension/", PensionConsumer.as_asgi())
]