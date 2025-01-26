from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Card
from .forms import UserForm

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao criar a conta.')
    else:
        form = UserForm()

    return render(request, 'pokeapp/register.html', {'form': form})

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

def pokemonologia(request):
    cards = Card.objects.all()
    return render(request, 'pokeapp/pokemonologia.html', {"cards": cards})
