from django.urls import path
from . import consumers

ws_urls = [

    path('count/',consumers.count.as_asgi()),
    path('<group_name>/',consumers.call.as_asgi())
]

