from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import user
from  .forms import signupform

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