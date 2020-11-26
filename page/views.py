from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login('index')
            return render(request,'index.html')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def index(request):
    return render(request,'index.html')