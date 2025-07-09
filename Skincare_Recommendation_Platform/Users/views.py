from django.shortcuts import render , HttpResponse 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

def SignupUser(request):
    is_empty = False
    not_match = False
    username_exists = False

    if(request.method == 'POST'):
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        repeat_password = request.POST.get('password_confirmation')  

        if(password != repeat_password):
            not_match = True

        if(not username or not password):
            is_empty = True

        if(User.objects.filter(username=username).exists()):
            username_exists = True

        if not(is_empty or not_match or username_exists):
        
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            return redirect('home_page')
        else:
            return render(request, 'Users/Signup.html', {'is_empty': is_empty, 'not_match': not_match, 'username_exists': username_exists})
    else:

        return render(request, 'Users/Signup.html', {})


def LoginUser (request):
    is_empty = False
    is_wrong = False
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if(username == '' or password == ''):
            is_empty = True
        user = authenticate(request , username = username , password = password)
        if(user is not None):
            login(request, user)
            messages.success(request, ("You have successfully logged in"))
            return redirect("home_page")
        
        else:
            is_wrong = True
            messages.success(request, ("error"))
            return render(request, 'Users/Login.html', {'is_empty': is_empty, 'is_wrong': is_wrong})
    else:
        return render(request, 'Users/Login.html', {})


def LogoutUser (request):
    logout(request)
    return redirect("home_page")