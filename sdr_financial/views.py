from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, "home.html", {})

def logout_user(request):
    logout(request)
    return redirect('home')
