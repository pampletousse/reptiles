from django.shortcuts import render,get_object_or_404
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

def delete(request,pk):

    template = loader.get_template("reptiles/liste.html")
    reptile = get_object_or_404(Reptile,pk=pk)
    context = {}
    Reptile.objects.filter(pk=pk).delete()

    return HttpResponse(template.render(context,request))

def liste(request):

    template = loader.get_template("reptiles/liste.html")
    reptiles = Reptile.objects.all()
    context = {"reptiles":reptiles}

    return HttpResponse(template.render(context,request))

def detail(request,pk):
    template = loader.get_template("reptiles/detail.html")

    reptile = get_object_or_404(Reptile,pk=pk)
    context = {
        "reptile":reptile
    }
    return HttpResponse(template.render(context,request))