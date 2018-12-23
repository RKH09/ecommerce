from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views import generic
from django.template import loader
from django.views.generic import TemplateView
from django.template import RequestContext
from .models import Products, Tags, Category, SubCategorie, Gallery
from shopping_cart.models import Order
from shopping_cart.views import order_details, get_user_pending_order, Wishlist, Order

app_name = 'products'



def product_list(request):
	title = "Clothings"
	feat = Products.objects.filter(featured=True).order_by('?')[:4]
	qs = Products.objects.filter(accessories=False).order_by('-id')
	tags = Tags.objects.all().order_by('-id')[:20]
	if request.user.is_authenticated:
		existing_order = get_user_pending_order(request)
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

			paginator = Paginator(qs ,15)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				'item_list':lists,
				'current_order_products': current_order_products,
				'tags':tags,
				'order': existing_order,
				'feat':feat,
				'wishlist_order_products': wishlist_order_products,
				'title':title,
			}
		else:
			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
	else:
		paginator = Paginator(qs ,15)
		page =request.GET.get('page')
		lists = paginator.get_page(page)
		title = "Clothings"
		context = {
			'item_list':lists,
			'tags':tags,
			'feat':feat,
			'title':title,
		}
	
	return render(request, "products.html", context)

def search_list(request):
	feat = Products.objects.filter(featured=True).order_by('?')[:4]
	q = request.GET.get('q',"None")
	title = q
	lookups = Q(title__icontains=q) | Q(tags__name__icontains=q)
	qs = Products.objects.filter(lookups).distinct().order_by('-id')
	tags = Tags.objects.all().order_by('-id')[:15]

	if request.user.is_authenticated:
		existing_order = get_user_pending_order(request)
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

			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				'query':q,
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
		else:
			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
	else:
		paginator = Paginator(qs ,20)
		page =request.GET.get('page')
		lists = paginator.get_page(page)
		context = {
				'query':q,
				'item_list':lists,
				'tags':tags,
				'feat':feat,
				'title':title,
		}
	
	return render(request, "search.html", context)
	'''
	__icontains = field contains this
	__iexact    = field is exactly this

	'''

def tag_list(request):
	feat = Products.objects.filter(featured=True).order_by('?')[:4]
	q = request.GET.get('q',"None")
	title = q
	lookups = Q(tags__name__iexact=q)
	qs = Products.objects.filter(lookups).distinct().order_by('-id')
	tags = Tags.objects.all().order_by('-id')[:15]

	if request.user.is_authenticated:
		existing_order = get_user_pending_order(request)
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

			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				'query':q,
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
		else:
			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
	else:
		paginator = Paginator(qs ,20)
		page =request.GET.get('page')
		lists = paginator.get_page(page)
		context = {
				'query':q,
				'item_list':lists,
				'tags':tags,
				'feat':feat,
				'title':title,
		}
	return render(request, "tags.html", context)


def category_list(request):
	
	q = request.GET.get('q',"None")
	if q == '1':
		title  = "Sarees"
	elif q == '2':
		title = "Lehenga"
	elif q == '3':
		title = "Kurti"
	elif q == '4':
		title = "Ethnic Gown"
	elif q == '5':
		title = "Two Piece Suit"
	elif q == '6':
		title = "Top & Tees"
	elif q == '7':
		title = "Gowns"
	elif q == '8':
		title = "Dresses"
	elif q == '9':
		title = "Prom Dresses"
	elif q == '10':
		title = "Crop Top & Skirt"
	elif q == '11':
		title = "Drape Style"
	elif q == '12':
		title = "Kurti Plazzo"
	elif q == '13':
		title = "Three Piece Set"
	else:
		title = "None"


	search = title
	feat = Products.objects.filter(featured=True).order_by('?')[:4]
	qs = Products.objects.filter(category__id__iexact=q).order_by('-id')
	tags = Tags.objects.all().order_by('-id')
	if request.user.is_authenticated:
		existing_order = get_user_pending_order(request)
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

			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				'query':q,
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
		else:
			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
	else:
		paginator = Paginator(qs ,20)
		page =request.GET.get('page')
		lists = paginator.get_page(page)
		context = {
				'query':q,
				'item_list':lists,
				'tags':tags,
				'feat':feat,
				'title':title,
		}
	return render(request, "category.html", context)



def product_featured_list(request):
	feat = Products.objects.filter(featured=True).order_by('?')[:4]
	qs = Products.objects.filter(featured=True).order_by('-id')
	tags = Tags.objects.all().order_by('-id')
	title = "Lookbook"

	if request.user.is_authenticated:
		existing_order = get_user_pending_order(request)
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

			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
		else:
			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
	else:
		paginator = Paginator(qs ,20)
		page =request.GET.get('page')
		lists = paginator.get_page(page)
		context = {
				
				'item_list':lists,
				'tags':tags,
				'feat':feat,
				'title':title,
		}
	return render(request, "products.html", context)


def product_inspired_list(request):
	feat = Products.objects.filter(featured=True).order_by('?')[:4]
	qs = Products.objects.filter(inspiredOutfit=True).order_by('-id')
	tags = Tags.objects.all().order_by('-id')
	existing_order = get_user_pending_order(request)
	paginator = Paginator(qs ,20)
	title = "Inspired Outfit"

	if request.user.is_authenticated:
		existing_order = get_user_pending_order(request)
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

			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
		else:
			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
	else:
		paginator = Paginator(qs ,20)
		page =request.GET.get('page')
		lists = paginator.get_page(page)
		context = {
				
				'item_list':lists,
				'tags':tags,
				'feat':feat,
				'title':title,
		}
	return render(request, "products.html", context)

def product_celebrity_list(request):
	title = "Celebrity Inspired"
	feat = Products.objects.filter(featured=True).order_by('?')[:4]
	qs = Products.objects.filter(celebrity=True).order_by('-id')
	tags = Tags.objects.all().order_by('-id')

	if request.user.is_authenticated:
		existing_order = get_user_pending_order(request)
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

			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
		else:
			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
	else:
		paginator = Paginator(qs ,20)
		page =request.GET.get('page')
		lists = paginator.get_page(page)
		context = {
				
				'item_list':lists,
				'tags':tags,
				'feat':feat,
				'title':title,
		}
	return render(request, "products.html", context)

def product_exclusive_list(request):
	title = "Exclusive Outfits"
	feat = Products.objects.filter(featured=True).order_by('?')[:4]
	qs = Products.objects.filter(exclusive=True).order_by('-id')
	tags = Tags.objects.all().order_by('-id')

	if request.user.is_authenticated:
		existing_order = get_user_pending_order(request)
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

			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
		else:
			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
	else:
		paginator = Paginator(qs ,20)
		page =request.GET.get('page')
		lists = paginator.get_page(page)
		context = {
				
				'item_list':lists,
				'tags':tags,
				'feat':feat,
				'title':title,
		}
	return render(request, "products.html", context)

def accessories_list(request):
	title = "Accessories"
	feat = Products.objects.filter(featured=True).order_by('?')[:4]
	qs = Products.objects.filter(accessories=True).order_by('-id')
	tags = Tags.objects.all().order_by('-id')
	if request.user.is_authenticated:
		existing_order = get_user_pending_order(request)
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

			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
		else:
			paginator = Paginator(qs ,20)
			page =request.GET.get('page')
			lists = paginator.get_page(page)
			context = {
				
				'item_list':lists,
				'tags':tags,
				'order': existing_order,
				'current_order_products': current_order_products,
				'wishlist_order_products': wishlist_order_products,
				'feat':feat,
				'title':title,
			}
	else:
		paginator = Paginator(qs ,20)
		page =request.GET.get('page')
		lists = paginator.get_page(page)
		context = {
				'item_list':lists,
				'tags':tags,
				'feat':feat,
				'title':title,
			}
	
	return render(request, "products.html", context)


class DetailView(generic.DetailView):
	model = Products
	template_name = "detail.html"
	

	#def get_object(self, *args, **kwargs):
		#request  =self.request
		#slug = self.kwargs.get('slug')

		#try:
	  #      instance = Products.objects.get(slug=slug)
	   # except Products.DoesNotExist:
	   #     raise Http404("Not found")

	def post(self, request, pk):
		print(pk)
		desc = request.POST.get("desc") 
		
		return render(request, "detail.html", RequestContext(request))


def gallery(request):
	qs = Gallery.objects.all()
	context = {
		'image':qs,
	}
	return render(request, "gallery.html", context)
