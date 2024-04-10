from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            # login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password')
    return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        city=request.POST.get('city')
        country=request.POST.get('country')


        if password != confirm_password:
            return render(request,'signup.html',{'error':'Passwords do not match'})
        
        user=User.objects.create_user(username=email,email=email,password=password,first_name=first_name,last_name=last_name)

        UserProfile.objects.create(user=user, address=address, city=city, country=country, phone=phone)

        return redirect('login')

    return render(request,'signup.html')