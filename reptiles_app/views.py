from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Reptile
from .forms import ReptileModelForm

# Create your views here.
def home(request):
    template = loader.get_template("reptiles/home.html")
    context = {
        "homeText":"Accueil",
    }
    return HttpResponse(template.render(context,request))

def create(request):

    if request.method == 'GET':
        template = loader.get_template("reptiles/form.html")
        form = ReptileModelForm()
        context = {"form":form}
    elif request.method == 'POST':
        template = loader.get_template("reptiles/form.html")
        context={"form":ReptileModelForm(request.POST)}
        if context["form"].is_valid():
            s = context["form"].save()
        #template = loader.get_template("reptiles/form.html")

    return HttpResponse(template.render(context,request))

def liste(request):

    template = loader.get_template("reptiles/liste.html")
    reptiles = Reptile.objects.all()
    context = {"reptiles":reptiles}

    return HttpResponse(template.render(context,request))