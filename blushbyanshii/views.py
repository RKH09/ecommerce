from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render, redirect
from .forms import ContactForm, Loginform, SignUpForm, DeliveryForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from shopping_cart.models import Delivery
from accounts.models import contact_form
from products.models import SubCategorie, Products, Gallery, Category, Subscription
from shopping_cart.views import order_details, get_user_pending_order, Order, update_transaction_records, Wishlist, add_to_cart
from accounts.views import my_profile



def home_page(request):
	qs = Products.objects.filter(featured=True).order_by('-id')[:6]
	exclusive = Products.objects.filter(exclusive=True).order_by('-id')[:6]
	order_count = Order.get_cart_total
	gallery = Gallery.objects.all()
	username = request.user.username
	if request.user.is_authenticated:
		
		existing_order = get_user_pending_order(request)
		order_count = Order.objects.filter(owner=request.user.id, is_ordered=False)


		object_list = Products.objects.all()
		filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
		current_order_products = []

		filtered_wishlist = Wishlist.objects.filter(owner=request.user.profile, is_ordered=False)
		wishlist_order_products = []
		
		if filtered_orders.exists():
			user_order = filtered_orders[0]
			user_order_items = user_order.items.all()
			current_order_products = [product.product for product in user_order_items]


		if filtered_wishlist.exists():
			user_orders = filtered_wishlist[0]
			user_order_item = user_orders.items.all()
			wishlist_order_products = [product.product for product in user_order_item]

		context = {
			'order': existing_order,
			'feature':qs,
			'exc':exclusive, 
			'count': order_count,
			'username':username,
			'gallery':gallery,
			'count':order_count,
			'current_order_products': current_order_products,
			'wishlist_order_products': wishlist_order_products,
		}
	else:
		context = {
			'feature':qs,
			'exc':exclusive, 
			'username':username,
			'gallery':gallery,
		}
	return render(request, "home_page.html", context) 

def subscription(request):

	email = request.POST.get('email')
	save = Subscription.objects.create(email_id = email)
	
	return render(request, "home_page.html") 

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
	if request.method == "GET":
		logout(request)
		return redirect('../login')

	return render(request, "logout.html", {})
	
def categories(request):
	qs = SubCategorie.objects.all().order_by('-id')
	username = request.user.username
	gallery = Gallery.objects.all()
	context = {
		'feature':qs,
		'username':username,
		'gallery':gallery
	}
	return render(request, "categories.html", context) 



def contact_page(request):
	if request.method == "POST":
		fullname = request.POST.get('fullname')
		email	= request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('review_form_text')
		save 	= contact_form.objects.create(fullname=fullname, email=email, subject=subject, message=message)
		return redirect('contactus')
	return render(request, "contact_page.html",)

