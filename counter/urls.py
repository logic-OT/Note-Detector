from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.Login),
    path('chat/<str:name>',views.chat,name='chat'),
    path('download/<str:file>',views.download),
    path('group_call/',views.group_call, name='group_call')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)