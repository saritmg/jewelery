from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.template import RequestContext
from checkout.forms import CheckoutForm
from . import models
from . import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.mail import send_mail, BadHeaderError
from cart.models import Cart
from cart.views import get_price_details
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='../login/')
def checkout(request):
   carts = Cart.objects.all()
   price_details = get_price_details(carts)

   csrfContext = RequestContext(request)
   checkout_form = CheckoutForm()
   return render(request,'checkout.html',
      {
         'form': checkout_form,
         "carts": carts,
         "price_details": price_details,
         "request": request
      },
      csrfContext)

class CheckoutViewSet(viewsets.ModelViewSet):
   queryset = models.Checkout.objects.all()
   serializer_class = serializers.CheckoutSerializer

   def create(self, request):
      print("new request")
      print(request.data)
      data = {}

      name = request.data.get("name")
      data["name"] = name

      first_address = request.data.get("first_address")
      data["first_address"] = first_address

      second_address = request.data.get("second_address")
      data["second_address"] = second_address

      town = request.data.get("town")
      data["town"] = town

      email_address = request.data.get("email_address")
      data["email_address"] = email_address

      phone_number = request.data.get("phone_number")
      data["phone_number"] = phone_number

      carts = Cart.objects.all()
      price_details = get_price_details(carts)
      print(price_details)
      data["sub_total"] = price_details["sub_total"]
      data["shipping"] = price_details["delivery_charge"]
      data["discount"] = price_details["discount"]
      data["order_total"] = price_details["total"]
      print(carts)
      cart_ids = []
      product_info = ""
      for cart in carts:
         product_info = product_info + "\n{} x {} = {}".format(cart.quantity, cart.product.pname, cart.total)
         cart_ids.append(cart.id)
      print(cart_ids)
      data["products"] = cart_ids
      serializer = self.get_serializer(data=data)
      if serializer.is_valid():
         serializer.save()

         message = "Name: " + name + "\nFirst Address: " + first_address + "\nSecond Addrress: " + second_address + "\nTown: " + town + "\nEmail Address: " + email_address + "\nPhone Number: " + str(
            phone_number) + "\n\nProducts:" + str(product_info) + "\n\nSub Total: " + str(
            data["sub_total"]) + "\nShipping Cost: " + str(data["shipping"]) + "\nDiscount: " + str(
            data["discount"]) + "\nOrder Total: " + str(data["order_total"])

         try:
            send_mail("New Order",
                      message, "", ['sakurinkim@gmail.com'])
         except BadHeaderError:
            return Response(status=500, data={'msg': 'Invalid header found.'})
         return Response(status=200, data={"msg": "Your order has been submitted."})
      else:
         return Response(status=500, data={"msg": "Order is invalid."})

   def retrieve(self, request, pk=None):
      return Response(status=403, data={"msg": "API not allowed."})

   def update(self, request, pk=None):
      return Response(status=403, data={"msg": "API not allowed."})

   def partial_update(self, request, pk=None):
      return Response(status=403, data={"msg": "API not allowed."})

   def destroy(self, request, pk=None):
      return Response(status=403, data={"msg": "API not allowed."})