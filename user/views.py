from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages  # Add this import
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.http  import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'user/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("bookings:available_flights"))
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return HttpResponseRedirect(reverse("bookings:available_flights"))  # Redirect to bookings app home
    else:
        form = CustomAuthenticationForm()
    return render(request, 'user/login.html', {'form': form})
