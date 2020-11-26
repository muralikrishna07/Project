from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from  .models import employee
from django.contrib import messages
# Create your views here.






def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        img = request.POST['myfile']
        
        user = employee.objects.create(name=name,phone=phone,email=email,address=address,img=img)
        user.save()
        messages.info(request,"user created")
        return render(request,'register.html')

        
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def details(request):
    dest = employee.objects.all()
    return render(request,"detail.html",{'dest':dest})