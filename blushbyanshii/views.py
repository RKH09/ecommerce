from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
def home_page(request):
    context = {
        'title':'BLUSH by Anshii'
    }
    return render(request, "home_page.html", context) 

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