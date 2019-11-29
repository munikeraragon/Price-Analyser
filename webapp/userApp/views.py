from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ItemForm
from .webScrape import *

# Create your views here.
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
        if(form.is_valid()):
            item = form.save(commit=False)
            item.currentUser = request.user
            data = form.cleaned_data
            url = data['itemURL']
            store = data['store']
            price = bestBuy(url)
            if(price != False):
                item.itemPrice = price
                item.save()
                return redirect('homelog')
    else:
        form = ItemForm()
    return render(request,'userApp/homelog.html',{'form':form})


