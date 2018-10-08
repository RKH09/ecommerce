from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views import generic
from django.template import loader
from django.views.generic import TemplateView
# Create your views here.

from .models import Products

def product_list(request):
    qs = Products.objects.all().order_by('id')
    paginator = Paginator(qs ,1)

    page =request.GET.get('page')
    lists = paginator.get_page(page)
    context = {
        'item_list':lists
    }
    return render(request, "products.html", context)

class DetailView(generic.DetailView):
    model = Products
    template_name = 'detail.html'
   # def post(self, request, pk):
   #     topic_id = request.POST.get("desc") 
    #    print(pk)
  #      return render(request, "talk/create.html")