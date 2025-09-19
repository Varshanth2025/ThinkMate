from django.shortcuts import render,redirect
from .models import Room,Topic,Message,User
from django.db.models import Q
from .forms import RoomForm,UserForm,CustomUserCreationForm
from django.http import HttpResponseForbidden
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def LoginPage(request):
    page='login'    
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user=User.objects.get(email=email)
        except:
            messages.error(request, "User does not exist ")   
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password")

    context={'page':page}
    return render(request,'base/login_register.html',context)



def LogoutPage(request):
    logout(request)
    return redirect('login')

def RegisterPage(request):
    form=CustomUserCreationForm()
    if request.method =='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            if user.username:
                user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')

    return render(request,'base/login_register.html',{'form':form})




def home(request):
    q=request.GET.get("q") if request.GET.get('q')!=None else ''
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
        )
    room_messages=Message.objects.filter(Q(room__topic__name__icontains=q))
    room_count=rooms.count()
    topics=Topic.objects.all()[0:5]
    context={"rooms":rooms,"topics":topics,"room_count":room_count,"room_messages":room_messages}
    return render(request,"base/home.html",context)

def userProfile(request,pk):
    user=User.objects.get(id=pk)
    rooms=user.room_set.all()
    room_messages=user.message_set.all()
    topics=Topic.objects.all()
    context={"user":user,"rooms":rooms,"room_messages":room_messages,"topics":topics}
    return render(request,"base/profile.html",context)


def room(request,pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')
        body = request.POST.get('body')
        if body:
            Message.objects.create(
                user=request.user,
                room=room,
                body=body
            )
            room.participants.add(request.user)
            return redirect('room', pk=room.id)

    context = {"room": room, "room_messages": room_messages, "participants": participants}
    return render(request, "base/room.html", context)



@login_required(login_url='login')
def create_room(request):
    form=RoomForm()
    topics=Topic.objects.all()
    if request.method=="POST":
        topic_name=request.POST.get('topic')
        topic,created=Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        return redirect('home')
    context={'form':form,"topics":topics}
    return render(request,"base/room_form.html",context)



@login_required(login_url='login')
def update_room(request,pk):
    topics=Topic.objects.all()
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    if request.user!=room.host:
        return HttpResponseForbidden("You are not allowed to do this")

    if request.method=="POST":
        topic_name=request.POST.get('topic')
        topic,created=Topic.objects.get_or_create(name=topic_name)
        room.topic=topic
        room.name=request.POST.get('name')
        room.description=request.POST.get('description')
        room.save()
        return redirect("home")
    context={'form':form,"topics":topics,"room":room}
    return render(request,"base/room_form.html",context)

@login_required(login_url='login')
def delete_room(request,pk):
     
     room=Room.objects.get(id=pk)
     if request.user!=room.host:
        return HttpResponseForbidden("You are not allowed to do this")
     if request.method=="POST":
         room.delete()
         return redirect("home")
     return render(request,"base/delete.html",{'obj':room}) 



@login_required(login_url="login")
def deleteMessage(request,pk):
    message=Message.objects.get(id=pk)

    if request.user!=message.user:
        return HttpResponseForbidden('you are not allowed here!!')
    if request.method=="POST":
        message.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':message})

@login_required(login_url="login")
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html',{'form':form})

def topicsPage(request):
    q=request.GET.get("q") if request.GET.get('q')!=None else ''
    topics=Topic.objects.filter(name__icontains=q)
    return render(request,"base/topics.html",{"topics":topics})

def activityPage(request):
    room_messages=Message.objects.all()
    return render(request,"base/activity.html",{"room_messages":room_messages})