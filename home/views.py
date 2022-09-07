from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.template import RequestContext
import requests
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator

from product.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    print("products", products)

    paginator = Paginator(products, 4)

    page = request.GET.get('page')

    # ?page=2
    products = paginator.get_page(page)

    template = loader.get_template('index.html')
    return HttpResponse(template.render({'products':products, 'request':request}))


