from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . models import Employee,Role,Department
from datetime import datetime

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
        else:
            my_user=User.objects.create_user(uname,email,pwd1)
            my_user.save()
            return redirect('login')

    return render(request,'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def all_emp(request):
    employee=Employee.objects.all()
    context={
        'employee':employee
    }
    return render(request,'all_emp.html',context)


def add_emp(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        phone=int(request.POST['phone'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        bonus=int(request.POST['bonus'])
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,phone=phone,dept_id=dept,role_id=role,bonus=bonus,hire_date=datetime.now)
        new_emp.save()
        return HttpResponse("Employee added successfully")
    elif request.method=="GET":
         return render(request,'add_emp.html')

    else:
        return HttpResponse("an exception occured! employee has not been added")    
       
def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_remove=Employee.objects.get(id=emp_id)
            emp_to_be_remove.delete()
            return HttpResponse("employee removed successfully")
        except:
            return HttpResponse("please enter a valid employee_id")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }

    return render(request,'remove_emp.html',context)


def filter_emp(request):
    return render(request,'filter_emp.html')


    
