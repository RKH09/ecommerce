from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views import generic
from django.template import loader
from django.views.generic import TemplateView
from django.template import RequestContext
from .models import Products, Tags, Category, SubCategorie
from shopping_cart.models import Order

app_name = 'products'



def product_list(request):
    qs = Products.objects.all().order_by('-id')
    tags = Tags.objects.all().order_by('-id')
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
    	user_order = filtered_orders[0]
    	user_order_items = user_order.items.all()
    	current_order_products = [product.product for product in user_order_items]

    paginator = Paginator(qs ,25)

    page =request.GET.get('page')
    lists = paginator.get_page(page)
    context = {
        'item_list':lists,
        'current_order_products': current_order_products,
        'tags':tags
    }
    return render(request, "products.html", context)

def search_list(request):
    q = request.POST.get('q',"None")
    lookups = Q(title__icontains=q) | Q(description__icontains=q) | Q(tags__name__icontains=q)
    qs = Products.objects.filter(lookups).distinct()
    paginator = Paginator(qs ,20)
    page =request.GET.get('page')
    lists = paginator.get_page(page)
    context = {
        'query':q,
        'item_list':lists
    }
    return render(request, "search.html", context)
    '''
    __icontains = field contains this
    __iexact    = field is exactly this

    '''

def tag_list(request):
    q = request.GET.get('q',"None")
    lookups = Q(tags__name__iexact=q)
    qs = Products.objects.filter(lookups).distinct()
    paginator = Paginator(qs ,20)

    page =request.GET.get('page')
    lists = paginator.get_page(page)
    context = {
        'query':q,
        'item_list':lists
    }
    return render(request, "tags.html", context)


def category_list(request):
    q = request.GET.get('q',"None")
    qs = Products.objects.filter(category__title__iexact=q).order_by('-id')
    paginator = Paginator(qs ,20)

    page =request.GET.get('page')
    lists = paginator.get_page(page)
    context = {
        'query':q,
        'item_list':lists
    }
    return render(request, "category.html", context)



def product_featured_list(request):
    qs = Products.objects.filter(featured=True).order_by('-id')
    paginator = Paginator(qs ,20)

    page =request.GET.get('page')
    lists = paginator.get_page(page)
    context = {
        'item_list':lists
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
