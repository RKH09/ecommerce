from django.shortcuts import render

def cart_home(request):

    context = {
        'title':'Blush - Cart',
    }
    return render(request, "carts/home.html", context)
