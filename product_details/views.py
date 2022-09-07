from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from product.models import Product

# Create your views here.
def new_product_detail(request, id):
   print("id", id)
   products = Product.objects.get(id=id)
   material = []
   for material_obj in products.pmaterial.all():
      material.append(material_obj.material)

   print(material)
   print(products.pimage)
   template = loader.get_template('product_details.html')
   return HttpResponse(template.render({"material":material,"products":products,"request":request}))

def product_details(request):
    template= loader.get_template('product_details.html')
    return HttpResponse(template.render())