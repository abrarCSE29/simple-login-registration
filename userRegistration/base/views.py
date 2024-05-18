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
    # frm = signupform(request.POST)
    # if request.method == 'POST':
    #     if frm.is_valid():
    #         frm.save()
    #         return redirect (login)
    # else:
    #     return HttpResponse('Signup not working')

    if request.method == 'POST':
        username = request.POST.get('username')
        userpassword = request.POST.get('userpassword')

        _user = user.objects.create(
            user_name = username,
            user_password = userpassword
        )
        _user.save()
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
                return dashboard(request,u)
        return HttpResponse('login failed')
            

def dashboard(request, user):
    return render (request, "base/dashboard.html" ,{'user':user})
    
    
                
