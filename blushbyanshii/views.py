from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, Loginform,SignUpForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


def home_page(request):
    context = {
        'title':'BLUSH by Anshii',
        'regular':'Regular User',
        'premium':'Premium User'
    }
    return render(request, "home_page.html", context) 

def login_page(request):
    form = Loginform(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            return redirect("/")
        else:
            print("Error")
    return render(request,"login.html", context)

def signup_page(request):
    return render(request, "signup.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title':'BLUSH Contact Page',
        'form':contact_form
    }
    if request.method == "POST":
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))

        if contact_form.is_valid():
            print(contact_form.cleaned_data)
    return render(request, "contact_page.html", context)