from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render (request, "base/index.html")
def login(request):
    return render (request, "base/login.html")
def signup(request):
    return render (request, "base/signup.html")