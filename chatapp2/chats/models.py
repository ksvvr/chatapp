from django.db import models
from datetime import datetime


# Create your models here.

class Room(models.Model):
    room_name=models.CharField(max_length=50)
class Message(models.Model):
    msg_value = models.CharField(max_length=10000)
    msg_date = models.DateTimeField(default=datetime.now, blank=True)
    msg_user = models.CharField(max_length=100)
    msg_room = models.CharField(max_length=50)    
