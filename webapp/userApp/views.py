from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'userApp/login.html')
def register(request):
    return render(request,'userApp/register.html')