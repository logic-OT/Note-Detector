from channels.generic.websocket import AsyncWebsocketConsumer
import json
import time
from django.contrib.auth.models import Group
from .models import *
from asgiref.sync import async_to_sync
from .analysis import note_finder

class count(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print('connectted')
        self.user = self.scope['user']
 
    async def receive(self,bytes_data=None):
        meta_data = self.scope
        note = note_finder(bytes_data,meta_data)
        await self.send(json.dumps({'note':note}))
        



