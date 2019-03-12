from django.shortcuts import render, redirect, get_object_or_404
from transection.models import Transection
from wallet.models import Wallet
from datetime import datetime
from category.models import Category

def index(request):
    transection = Transection.objects.all().order_by('-date')
    wallet = Wallet.objects.first()
    count = Wallet.objects.all().count()    #Queryเป็นจำนวนเต็ม
    context = {
        'transection' : transection,
        'wallet' : wallet
    }

    if count <= 0:  #เช็คเงินในกระเป๋า
        return redirect('wallet')  
         
    return render(request, 'transection/index.html', context)

def add_transection(request):
    income = Category.objects.filter(cat_type = 0)
    expenditure = Category.objects.filter(cat_type = 1)
    if request.method == 'POST':
        amount = request.POST['amount']
        income = request.POST['income']
        catid = request.POST['category']
        note = request.POST['note']
        date = request.POST['date']

        wallet = Wallet.objects.first()
        amounttransection = wallet.balance      
       
        if(income == '0'):      
            balance = (amounttransection + float(amount))
        else:
            balance = (amounttransection - float(amount))
        
        wallet.balance = balance 
        wallet.save() 

        category = Category.objects.get(id = catid) 
        transection = Transection(amount = amount, income = income, category = category, note = note, date = date)
        if transection:
           transection.save()
           return redirect('transection')
           
    context = {
        'expenditure' : expenditure,
        'income' : income
    }
    return render(request, 'transection/add-transection.html', context)

def edit_transection_form(request, transection_id):
    transection = Transection.objects.get(pk = transection_id)
    category = Category.objects.all()
    context = {
        'transection' : transection,
        'category' : category
    }
    return render(request, 'transection/edit-transection.html',context)

def edit_transection_save(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        income = request.POST['income']
        catid = request.POST['category']
        note = request.POST['note']
        date = request.POST['date']
        transectionid = request.POST['transectionid']
        category = Category.objects.get(id = catid) 

        wallet = Wallet.objects.first()
        transection = Transection.objects.get(pk = transectionid)
        amounttransection = wallet.balance
        
        oldamount = transection.amount
        if(income == '0'):
            if(oldamount >  float(amount)):     #เช็คจำนวนเงิน
               balance = (amounttransection - (float(oldamount) - float(amount)))
            else:
               balance = (amounttransection + (float(amount) - float(oldamount)))
        else:
            if(oldamount > float(amount)):
               balance = (amounttransection + (float(oldamount) - float(amount)))
            else:
               balance = (amounttransection - (float(amount) - float(oldamount)))
        
        wallet.balance = balance 
        wallet.save() 

        transection.amount = amount 
        transection.income = income
        transection.category = category
        transection.note = note 
        transection.date = date 
        transection.save()
    
    return redirect('transection')


def delete_transection(request, transection_id):
    delete = get_object_or_404(Transection, pk=transection_id)
    transection = Transection.objects.get(pk = transection_id)     
    wallet = Wallet.objects.first()
    balance = wallet.balance
    amounttransection = balance
    amount = transection.amount
    income = transection.income

    if(income == '0'):
        balance = (amounttransection - float(amount))
    else:
        balance = (amounttransection + float(amount))
        
    wallet.balance = balance 
    wallet.save()
    delete.delete() 
    return redirect('transection')    
