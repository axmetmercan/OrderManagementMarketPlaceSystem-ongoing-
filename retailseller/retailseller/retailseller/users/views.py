from os import renames
from . forms import LoginForm, Registration
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):

    form = LoginForm(request.POST or None)


    if request.method =='GET':
        context = {
        'form': form,
        }
        return render(request, 'homepage.html', context)

    elif request.method == 'POST':
        if form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')

            user = authenticate(username = user_name, password = password)

            if user is None:
                messages.info(request, 'There is no such user ')
                return redirect('users:signup')

            messages.success(request, 'Succesfully Logged in')
            login(request, user)
            return redirect('users:dashboard')



def signup(request):

    form = Registration(request.POST or None)
    if form.is_valid():
        
        user_name = form.cleaned_data.get('user_name')
        password = form.cleaned_data.get('password')

        new_user = User(username = user_name)
        new_user.set_password(password)
        new_user.save()

        login(request, new_user)

        messages.success(request, 'Succesfully signed in...')

        return redirect('index')
    
    context = {
            'form' : form,
            }
    return render(request, 'signup.html', context)


@login_required(login_url='index')
def user_logout(request):
    logout(request)

    return redirect('index')

@login_required(login_url='index')
def dashboard(request):
    return render(request, 'dashboard.html')

    
@login_required(login_url='index')
def user_profile(request):
    return render(request, 'profile.html')