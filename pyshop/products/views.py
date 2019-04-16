from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Product
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})

def new(request):
    return render(request,'checkout.html')

def signup(request):
    if request.method=='POST':
          if request.POST['password1']==request.POST['password2']:
              try:
                  user=User.objects.get(username=request.POST['username'])
                  return render(request, 'signup.html',{"error":'Username is already taken'})
              except User.DoesNotExist:
                  user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                  auth.login(request,user)
                  return redirect('index')
          else:
               return render(request, 'signup.html',{"error":'password does not match'})
    else:
       return render(request,'signup.html')
def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user!=None:
            auth.login(request,user)

            return redirect('index')
        else:
            return render(request, 'login.html',{'error':'username and password is incorrect'})
    else:
       return render(request,'login.html')
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('index')
