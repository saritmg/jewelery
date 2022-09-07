from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from rest_framework import viewsets
from django.core.mail import send_mail, BadHeaderError
from rest_framework.response import Response
from . import models
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from . forms import ContactForm

from . import serializers

import requests

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):  # Modelviewset is parent class
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer

    # function or method of parent class, override
    def create(self, request):
        print("new request")
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            name = request.data.get("name")
            email = request.data.get("email")
            message = request.data.get("message")
            subject = request.data.get("subject")
            serializer.save()
            try:
                send_mail(subject + ": " + name,
                          message + "\n" + "User email: " + email, "", ['psuzy223@gmail.com'])
            except BadHeaderError:
                return Response(status=400, data={'msg': 'Invalid header found.'})
            return Response(status=200, data={"msg": "Your query has been submitted."})
        else:
            return Response(status=400, data={"msg": "Query is invalid."})

    # def list(self, request):
    #       return Response(status=403,data={"msg": "API not allowed."})

    def retrieve(self, request, pk=None):
        return Response(status=403, data={"msg": "API not allowed."})

    def update(self, request, pk=None):
        return Response(status=403, data={"msg": "API not allowed."})

    def partial_update(self, request, pk=None):
        return Response(status=403, data={"msg": "API not allowed."})

    def destroy(self, request, pk=None):
        return Response(status=403, data={"msg": "API not allowed."})


def contact(request):
    # template = loader.get_template('contact.html')

    if request.method == 'POST':
        form = ContactForm(request.POST)  # object create
        if form.is_valid():
            response = requests.post('http://localhost:8000/api/v1/contact/', request.POST)  # api call
            print('response', response.status_code)  # 200 response from ContactView - for debugging
            if response.status_code == 200:
                return redirect('success/')
            else:
                return HttpResponse("Your query could not be submitted. Please try again.")

    contact_form = ContactForm()
    csrfContext = RequestContext(request)
    return render(
        request, 'contact.html',
        {
            'form': contact_form
        },
        csrfContext
    )

def contact_success(request):
   return render(request,'contact_success.html')