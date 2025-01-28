from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Produto, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('edit_profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'makeapp/conta.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def register(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        email = request.POST['email']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        profile = Profile(user=user)
        profile.save()
        redirect('login')

    return render(request, 'makeapp/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            messages.error(request, 'Username ou senha incorretos.')
    
    return render(request, 'makeapp/login.html')

@login_required
def menu(request):
    query = request.GET.get('search', '')
    if query:
        produtos = Produto.objects.filter(titulo__icontains=query)
    else:
        produtos = Produto.objects.all()

    profile = Profile.objects.get(user=request.user)
    return render(request, 'makeapp/menu.html', {"produtos": produtos, "profile": profile, "query": query})

@login_required
def sale(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    profile = Profile.objects.get(user=request.user)
    return render(request, 'makeapp/sale.html', {'produto': produto, 'profile': profile})