from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Reptile

# Create your views here.
def home(request):
    template = loader.get_template("reptiles/home.html")
    context = {
        "homeText":"Accueil",
    }
    return HttpResponse(template.render(context,request))

def create(request):

    if request.method == 'GET':
        print("get")
        template = loader.get_template("reptiles/form.html")
    elif request.method == 'POST':
        print("post")
        template = loader.get_template("reptiles/form.html")
    else:
        print("rien")

    return HttpResponse(template.render(context,request))

def liste(request):

    template = loader.get_template("reptiles/liste.html")
    reptiles = Reptile.objects.all()
    context = {"reptiles":reptiles}

    return HttpResponse(template.render(context,request))