from channels.generic.websocket import AsyncWebsocketConsumer
import json
import time

from django.contrib.auth.models import Group
from .models import *
from asgiref.sync import async_to_sync

class count(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print('connectted')
        self.user = self.scope['user']
        self.current_user = Client.objects.get(user=self.user)
        self.current_user.is_online = True
        channel_name = self.current_user.channel_name
        #print(self.channel_name,channel_name)
        self.current_user.channel_name = self.channel_name
        self.current_user.save()

 
    async def disconnect(self,code):
        self.current_user.is_online = False 
        self.current_user.save()
        self.current_user.channel_name = None
        print('disconnected')
    
    async def receive(self, text_data):
        print(self.scope)
        print(self.scope['url_route']) 
        data = json.loads(text_data)
        reciever = Client.objects.get(user__username=data['to'])
        print(reciever.channel_name,Client.objects.get(user=self.scope['user']).channel_name)
        await self.channel_layer.send(reciever.channel_name,{'type':'chat.message','message':data['message'],'from':self.user.username})
        await self.send(json.dumps({'message':data['message']}))

    async def chat_message(self,event):
        print(event)
        await self.send(json.dumps(event))
      
class call(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()

    async def receive(self,bytes_data=None,text_data=None):
        await self.channel_layer.group_send(self.group_name,{'type':'audio.message','audio':bytes_data})


    async def disconnect(self,code):
        await self.channel_layer.group_discard(self.group_name,self.channel_name)
    
    async def audio_message(self,event):
        await self.send(bytes_data=event['audio'])