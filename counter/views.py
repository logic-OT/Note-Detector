from django.http.response import HttpResponse
from django.shortcuts import render,redirect

from counter.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
import mimetypes
from websocket import settings

@login_required(login_url='login/')
def home(request):
    
    if request.method == "POST":
        sumitted_file = request.FILES.get('file')
        print(sumitted_file)
        audio.objects.create(file = sumitted_file)
    audio_files = audio.objects.all()
    contacts = Client.objects.exclude(user = request.user)
    context = {'contacts':contacts,'audio_files':audio_files}
    return render(request, 'home.html',context)

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            print('logged')
            return redirect('home')

    return render(request,'login.html')

def chat(request,name):
    to = Client.objects.get(user__username=name)
    context = {'to':to}
    return render(request,'chat.html',context)

import os
def download(request,file):
    direc = '/media/'+file
    file_path = str(settings.BASE_DIR) + direc
    print(file_path)
    opened = open(file_path,'rb')
    type,_ = mimetypes.guess_type(file_path)
    response = HttpResponse(opened,content_type=type)
    response['Content-Disposition'] = 'attachment;filename={}'.format(file)
    return response

def group_call(request):
    print(request.headers)
    return render(request,'group_chat.html')