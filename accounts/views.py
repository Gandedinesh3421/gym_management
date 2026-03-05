from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        User.objects.create_user(username=username,email=email,password=password)
        return redirect('login')
    return render(request,'register.html')

def user_login(request):
    if request.method=='POST':
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        if user:
            login(request,user)
            return redirect('dashboard')
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('login')
