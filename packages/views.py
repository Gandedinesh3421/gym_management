from django.shortcuts import render,redirect
from .models import Package,Membership

def package_list(request):
    packages=Package.objects.all()
    return render(request,'packages.html',{'packages':packages})

def buy_package(request,id):
    package=Package.objects.get(id=id)
    Membership.objects.create(user=request.user,package=package)
    return redirect('dashboard')
