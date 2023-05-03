from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,  authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    return render(request, 'index.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')


            except IntegrityError:
                return render(request, 'signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'Это имя пользователя уже занято. Пожалуйста, выберите нового пользователя'})

        else:
            return render(request, 'signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Пароль не подходит'})




def signinuser(request):
    if request.method == 'GET':
        return render(request, 'signinuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signinuser.html',
                          {'form': AuthenticationForm(), 'error': 'Имя пользователя или пароль не совпадают'})
        else:
            login(request, user)
            return redirect('home')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main')
def home(request):
    tours = Tour.objects.all()
    hotels = Hotel.objects.all()
    reviews = Review.objects.all()

    context = {
        'tours': tours,
        'hotels': hotels,
        'reviews': reviews
    }
    return render(request, 'home.html', context=context)