from django.shortcuts import render,redirect
from .models import Room,Message

# Create your views here.

def home(request):
    return render(request,"home.html")

def auth_req(request):
    room_namee=request.POST['room_name']
    user_namee=request.POST['user_name']
    if Room.objects.filter(room_name=room_namee):
        return redirect('/'+room_namee+'/?user_name='+user_namee)
    else:
        new_room = Room.objects.create(room_name=room_namee)
        new_room.save()
        return redirect('/'+room_namee+'/?username='+user_namee)    
