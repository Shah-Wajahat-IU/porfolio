from django.contrib.auth import  authenticate ,login,logout
from django.db import IntegrityError
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,JsonResponse
from .models import User, InformationModel,EducationModel,ExprienceModel,ProjectModel,SkillSetModel,MessageModel
 # Create your views here.

def index_view(request):

    return render(request, template_name="user_interface/index.html")



def login_view(request, *args,**kwargs):
    if request.method=="POST":

        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "user_interface/login.html",{"message":"Invalid username or password."})
    else:
        return render(request, "user_interface/login.html")

def  logout_view(request):
    logout(request)


def register_view(request,*args, **kwargs):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST['email']

        password=request.POST['password']
        confirmation=request.POST['confirmation']

        if password !=confirmation:
            return render(request, "user_interface/register.html",{"message":"Password does not match"})


        try:
            user= User.objects.create_user(username,email,password)
            user.save()
        except IntegrityError:
            return render(request,"user_interface/register.html",{"message":"Username already exists"})
        login(request,user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request,"user_interface/register.html")