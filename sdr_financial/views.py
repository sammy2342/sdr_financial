from django.shortcuts import render, redirect
from django.contrib.auth import logout
import requests


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, "home.html", {})

def logout_user(request):
    logout(request)
    return redirect('home')

def coins(request):
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1')
    data = response.json()
    return render(request, 'coins.html', {'data': data})