from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ItemForm
from django.contrib.auth.models import User
from .models import Item
from updatePrices.webScrape import *


def register(request):
    if(request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'userApp/register.html', {'form':form})

def homelog(request):
    if(request.method == 'POST'):
        form = ItemForm(request.POST)
        price = False
        if(form.is_valid()):
            item = form.save(commit=False)
            item.currentUser = request.user
            data = form.cleaned_data
            url = data['itemURL']
            store = data['store']
            if(store == "BestBuy"):
                price = bestBuy(url)
            elif(store == "Amazon"):
                price = amazon(url)
            elif(store == "Walmart"):
                price = walmart(url)
        if(price != False):
            item.itemPrice = price
            item.save()
            return redirect('myItems')
    else:
        form = ItemForm()
    return render(request,'userApp/homelog.html',{'form':form})

def myItems(request):
    userItems = Item.objects.filter(currentUser=request.user)
    return render(request,'userApp/myItems.html', {'userItems':userItems})
    
