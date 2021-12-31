from django.http.response import HttpResponse
from django.shortcuts import render,redirect

from counter.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
import random,string
from websocket import settings

def home(request):
    unique_key = gen_string = 'MACEZ_'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    context = {'unique_key':unique_key}
    return render(request, 'home.html',context)


