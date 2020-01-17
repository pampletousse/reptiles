from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def home(request):
    template = loader.get_template("reptiles/home.html")
    context = {
        "homeText":"Accueil",
    }
    return HttpResponse(template.render(context,request))