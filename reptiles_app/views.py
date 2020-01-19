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
        template = loader.get_template("reptiles/formCreate.html")
        form = ReptileModelForm()
        context = {"form":form,
        "typeEnvoi":"create",}
        print(request.META.get('HTTP_REFERER'))
    elif request.method == 'POST':
        template = loader.get_template("reptiles/formCreate.html")
        context={"form":ReptileModelForm(request.POST),
        "typeEnvoi":"create"}
        if context["form"].is_valid():
            s = context["form"].save()
        

    return HttpResponse(template.render(context,request))

def update(request,pk):

    reptile = get_object_or_404(Reptile,pk=pk)
    form = ReptileModelForm(request.POST or None, instance=reptile)
    template = loader.get_template("reptiles/formUpdate.html")
    context = {"form":form,"typeEnvoi":"update","pk":pk}
    if form.is_valid():
        s = form.save()

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