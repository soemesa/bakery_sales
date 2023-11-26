from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views import View

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

class Inicio(View):
    template_name = 'index.html'