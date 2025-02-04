from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'index.html')

def login_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid username or password")
            return redirect("login")

    return render(request,'login.html')

def register_view(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pwd1=request.POST.get('password1')
        pwd2=request.POST.get('password2')
        if pwd1!=pwd2:
            messages.error(request, "Password and confirm password are not the same.")
            return redirect('register')

        
        else:
            my_user=User.objects.create_user(uname,email,pwd1)
            my_user.save()
            return redirect('login')

    return render(request,'register.html')

def logout_view(request):
    return render(request,'logout.html')
