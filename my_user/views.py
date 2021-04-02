from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth .decorators import login_required

from django.contrib .auth import authenticate, login, logout , get_user_model
from my_user .forms import userlogin ,userregisterform 
from .models import userregisterform 

@login_required

def login_views(request):
    form = userlogin(request.POST)
    username = 'not yet logged in db'
    if request.method =='POST':
        login_views = form
        if form.is_valid():
            username =  form.cleaned_data['username']
            password = form.cleaned_data['password']
            return render(request , 'home.html' ) 
        else:
             form = userlogin() 
    

    return render(request , 'login.html' , {'form':form })


def sign_views(request):
    signform = userregisterform(request.POST)
    if request.method =='POST':
        if signform.is_valid :
            new_user = signform.objects.Create_user( username = request.POST['username'] , email = request.POST['email address'] , password= request.POST['password'])
            email1 = signform.cleaned_data['email address:' ]
            email2 = signform.cleaned_data['confirm email:' ]
            password = signform.cleaned_data[ 'password:']
            return render(request , 'home.html')
        else:
            return signform()   
    return render(request, 'sign.html' , {'form':signform })    
            

