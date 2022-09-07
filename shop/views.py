from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator
from product.models import Product

# Create your views here.
def shop(request):
    products = Product.objects.all()
    print("products", products)
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    # ?page=2
    products = paginator.get_page(page)
    template = loader.get_template('shop.html')
    return HttpResponse(template.render({'products':products,'request':request}))