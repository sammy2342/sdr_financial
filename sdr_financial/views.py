from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate


def home(request):
    return render(request, "base.html", {})
