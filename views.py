from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from  django.contrib import messages

# Create your views here.

def index(request):
    
    return render(request,'index.html')

def Login(request):
    if request.method=='POST':
        #check if user has entered correct credentials
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged in")
            return redirect('index.html')
        else:
            messages.success(request,"Invalid Credentials,Please try Again")
            return render(request,'index.html')
    return render(request,'Login.html')

def Logout(request):
    
    return render(request,'Logout.html')




