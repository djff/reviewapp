from django.shortcuts import render

from .models import Signup

# Create your views here.

def signup(request):
    user = Signup.objects()
    return render(request, 'reviewhome/signup.html', {})

def index(request):
    return render(request, 'reviewhome/home.html', {})
