from django.shortcuts import render, redirect, get_object_or_404
from wallet.models import Wallet
from transection.models import Transection
from datetime import datetime

def index(request):
    wallet = Wallet.objects.first()
    count = Wallet.objects.all().count()
    context = {
        'wallet' : wallet,
        'count' : count
    }
    return render(request, 'wallet/index.html', context)

def add_wallet(request):
    if request.method == 'POST':
        name = request.POST['name']
        balance = request.POST['balance']
        wallet = Wallet(name = name, balance = balance, begin = balance)
        if wallet:
           wallet.save()
           return redirect('transection')
    return render(request, 'wallet/add-wallet.html')

def edit_wallet(request):
    if request.method == 'POST':
        name = request.POST['name']
        balance = request.POST['balance']
        wallet = Wallet.objects.first()
        wallet.name = name 
        wallet.balance = balance 
        wallet.begin = balance 
        wallet.save() 
        return redirect('transection')

