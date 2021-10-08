from django.contrib import messages
from django.shortcuts import redirect, render
from .protector import is_valid
from django.contrib.auth import authenticate,login

# Create your views here.


def user_login(request):

    if not request.user.is_authenticated:
        if request.method=='POST':
            uid = request.POST["uid"]
            password = request.POST["password"]

            if is_valid(request,uid,password):

                user = authenticate(uid=uid,password=password)

                if user is not None:
                    login(request,user)
                    return redirect('index')
                    
                else:
                    messages.error(request,"invalid credentials")
        
        return render(request,'login.html')


    
    return redirect('index')

    