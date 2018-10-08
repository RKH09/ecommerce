from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, Loginform, SignUpForm
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
    key = request.session.session_key
    if key is None:
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
    else:
        return redirect('/')
    return render(request,"login.html", context)
    

def signup(request):
    key = request.session.session_key
    if key is None:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/')
        else:
            form = SignUpForm()
            return render(request, 'signup.html', {'form': form})
    else:
        return redirect('/')
    return render(request,"signup.html", {'form': form})



def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('../login')

    return render(request, "logout.html", {})
    




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