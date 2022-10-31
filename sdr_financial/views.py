from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, "home.html", {})
