from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Account
import random



# Create your views here.


@login_required
def create_new_account(request):
    a = Account(balance=request.POST['balance'],
                type=request.POST['type'], user=request.user)
    a.number = f"{rn()}-{rn()}-{rn()}-{rn()}"
    a.save()
    return redirect('dashboard')


@login_required
def dashboard(request):
    context = {
        'accounts': request.user.account_set.all()
    }
    return render(request, 'dashboard.html', context)




@login_required
def add_transaction(request):
    print(request.POST)
    return redirect('dashboard')


def rn():
    return random.randrange(1000, 9999)
