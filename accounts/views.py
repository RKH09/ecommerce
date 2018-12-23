from django.shortcuts import render, get_object_or_404, redirect

from shopping_cart.models import Order, Delivery
from .models import Profile
from shopping_cart.views import order_details, get_user_pending_order, Wishlist, Order
from django.contrib.auth.models import User


def my_profile(request):
	user_profile 	= 	get_object_or_404(Profile, user=request.user)
	my_user_profile = Profile.objects.filter(user=request.user).first()
	my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
	existing_order = get_user_pending_order(request)
	my_address  = Delivery.objects.filter(delivery=True, owner=user_profile).order_by('-id')[:1]
	username = request.user.username
	context = {
		'my_orders': my_orders,
		'address':my_address,
		'username': username,
		'order': existing_order,
	}

	return render(request, "profile.html", context)


def deliveryAccount(request):
	if request.method == "POST":
		user_profile 	= 		get_object_or_404(Profile, user=request.user)
		fname 			= 		request.POST.get('firstname')
		lname 			= 		request.POST.get('lastname')
		email 			= 		request.POST.get('email')
		country 		= 		request.POST.get('country')
		address 		= 		request.POST.get('address')
		town 			= 		request.POST.get('town')
		zipcode 		= 		request.POST.get('zipcode')
		phoneno 		= 		request.POST.get('phoneno')
		comment 		= 		request.POST.get('checkout_comment')

  
		save = Delivery.objects.create(owner= user_profile, first_name=fname, last_name=lname, email=email, country=country, address=address, 
											town=town, zipcode=zipcode, phone=phoneno, comment=comment, delivery=True)
				
		return redirect('profile')
	return render(request, "profile.html")
						