from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Card, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        email = request.POST['email']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        profile = Profile(user=user)
        profile.save()
        redirect('Pokemonologia')

    return render(request, 'pokeapp/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('Pokemonologia')
        else:
            messages.error(request, 'Username ou senha incorretos.')
    
    return render(request, 'pokeapp/login.html')

@login_required
def pokemonologia(request):
    cards = Card.objects.all()
    return render(request, 'pokeapp/pokemonologia.html', {"cards": cards})
