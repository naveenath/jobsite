from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm
from .models import Profile

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            profile = Profile.objects.create(
                user=user,
                role=profile_form.cleaned_data['role'],
                company_name=profile_form.cleaned_data['company_name'],
                bio=profile_form.cleaned_data['bio'],
            )
            login(request, user)
            return redirect('jobs:list')
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'core/signup.html', {'form': form, 'profile_form': profile_form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('jobs:list')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('core:login')

def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'core/profile.html', {'form': form})
