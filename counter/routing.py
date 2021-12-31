from django.urls import path
from . import consumers

ws_urls = [

    path('count/',consumers.count.as_asgi()),
]

