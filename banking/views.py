from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Account
from .forms import TransactionForm
import random


@login_required
def create_new_account(request):
    a = Account(balance=request.POST['balance'],
                type=request.POST['type'], user=request.user)
    a.number = f"{rn()}-{rn()}-{rn()}-{rn()}"
    a.save()
    return redirect(f"dashboard/{a.id}")


@login_required
def dashboard(request, pk):
    context = {
        'accounts': request.user.account_set.all()
    }
    if request.user.account_set.first():
        try:
            account = request.user.account_set.get(id=pk)
        except:
            account= request.user.account_set.first()
        context["account"] = account
    if 'account' in context:
        context['transactions'] = context['account'].transaction_set.all()
    # breakpoint()
    return render(request, 'dash.html', context)


@login_required
def add_transaction(request):
    form = TransactionForm(request.POST)
    if form.is_valid():
        transaction = form.save()
        account = request.user.account_set.get(id=request.POST['account'])
        transaction.account = account
        if transaction.type == 'W' or transaction.type == 'P':
            if transaction.amount > account.balance:
                messages.add_message(request, messages.INFO,
                                     'Amount entered is greater than balance')
                transaction.delete()
                return redirect(f"dashboard/{account.id}")
            transaction.remaining_balance = account.balance - transaction.amount
        else:
            transaction.remaining_balance = account.balance + transaction.amount
        account.balance = transaction.remaining_balance
        transaction.save()
        account.save()
        messages.add_message(request, messages.INFO, 'Transaction saved')
        print([transaction.amount, account.balance])
    return redirect(f"dashboard/{account.id}")


@login_required
def delete_transaction(request, account_id, pk):
    account = request.user.account_set.get(id=account_id)
    if account:
        transaction = account.transaction_set.get(id=pk)
        if transaction:
            if transaction.type == 'W' or transaction.type == 'P':
                account.balance = account.balance + transaction.amount
            else:
                account.balance = account.balance - transaction.amount
            transaction.delete()
            account.save()
            messages.add_message(request, messages.INFO,
                                 'Transaction successfully deleted')
    return redirect(f"/dashboard/{account.id}")


def rn():
    return random.randrange(1000, 9999)
