from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import user
from  .forms import loginForm, signupform

# Create your views here.
def home(request):
    return render (request, "base/index.html")
def login(request):
    return render (request, "base/login.html")
def signup(request):
    frm = signupform()
    return render (request, "base/signup.html", {'form' : frm})



def processRequest(request):
    if request.method == 'POST':
        frm = signupform(request.POST)
        frm.save()
        return redirect (login)
    else:
        return HttpResponse('Signup not working')
    


def getCredentials(request):
    # frm = loginForm()
    # return render (request, "base/login.html", {'form' : frm} )
    if request.method == "POST":
        username = request.POST.get('username')
        userpassword = request.POST.get('userpassword')
        allusers = user.objects.all()
        
        for u in allusers:
            if(u.user_name==username and u.user_password==userpassword):
                return HttpResponse('Successful login')
        return HttpResponse('login failed')
            
    
                
