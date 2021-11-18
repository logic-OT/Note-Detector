from django.contrib.admin.filters import BooleanFieldListFilter
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import FileField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Client(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    channel_name = models.CharField(max_length=100,null=True,blank=True)
    is_online = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.user.username

class audio(models.Model):
    file = models.FileField(blank=True,null=True)

    def __str__(self):
        return self.file.name
@receiver(post_save,sender=User)
def create_client(sender,instance,created,*args,**kwargs):
    if created:
        Client.objects.create(user=instance)

