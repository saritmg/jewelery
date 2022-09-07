from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def layout(request):
    template = loader.get_template('layout.html')
    return HttpResponse(template.render({"request":request}))