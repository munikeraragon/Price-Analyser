from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def login(request):
    return render(request,'userApp/login.html')
def register(request):
    if(request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'userApp/register.html', {'form':form})