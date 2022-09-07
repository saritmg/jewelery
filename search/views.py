from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.template import RequestContext
import requests
from django.views.decorators.csrf import csrf_protect

from product.models import Product

def search(request):
   if request.method == 'POST':
         srch = request.POST['srh']

         if srch:
            match = Product.objects.filter(Q(pname__icontains=srch) |
                                           Q(pid__icontains=srch)
                                           )
            if match:
               return render(request, 'search.html', {'sr': match})
            else:
               messages.error(request, 'no result found')
         else:
            return HttpResponseRedirect('/search')

   return render(request, 'search.html')
