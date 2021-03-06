from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login as auth_login

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('../userprofile/profile/add/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def login(request):
    return render(request, 'registration/login.html')

def logout(request):
    return render(request, 'registration/login.html')

