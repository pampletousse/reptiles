from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponse
from .models import Reptile,User
from .forms import ReptileModelForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    template = loader.get_template("reptiles/home.html")
    context = getUserContext(request)
    return HttpResponse(template.render(context,request))

@login_required(login_url='/connexion/')
def create(request):

    if request.method == 'GET':
        template = loader.get_template("reptiles/formCreate.html")
        form = ReptileModelForm()
        context = getUserContext(request)
        context["form"]=form
        context["typeEnvoi"]="create"
        return HttpResponse(template.render(context,request))

    elif request.method == 'POST':
        template = loader.get_template("reptiles/formCreate.html")
        context = getUserContext(request)
        context["form"]=ReptileModelForm(request.POST)
        context["typeEnvoi"]="create"

        if context["form"].is_valid():
            s = context["form"].save()
        return redirect("/liste/")
        
    

@login_required(login_url='/connexion/')
def update(request,pk):
    reptile = get_object_or_404(Reptile,pk=pk)
    form = ReptileModelForm(request.POST or None, instance=reptile)
    template = loader.get_template("reptiles/formUpdate.html")
    context = getUserContext(request)
    context['form']=form
    context['typeEnvoi']='update'
    context['pk']=pk

    if request.method == 'GET':
        return HttpResponse(template.render(context,request))

    elif request.method == 'POST':
        if form.is_valid():
            s = form.save()

        return redirect("/liste/")

@login_required(login_url='/connexion/')
def delete(request,pk):

    template = loader.get_template("reptiles/liste.html")
    reptile = get_object_or_404(Reptile,pk=pk)
    context = getUserContext(request)
    Reptile.objects.filter(pk=pk).delete()

    return redirect("/liste/")

def liste(request):
    template = loader.get_template("reptiles/liste.html")
    reptiles = Reptile.objects.all()
    context = getUserContext(request)
    context['reptiles'] = reptiles

    return HttpResponse(template.render(context,request))

def detail(request,pk):

    template = loader.get_template("reptiles/detail.html")
    reptile = get_object_or_404(Reptile,pk=pk)
    context = getUserContext(request)
    context['reptile']=reptile

    return HttpResponse(template.render(context,request))

def connexion(request):
    template = loader.get_template("reptiles/connexion.html")
    context = {}
    if request.method == 'POST':
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return redirect("/liste/")
        else:
            template = loader.get_template("reptiles/connexion.html")
            context = {}

    return HttpResponse(template.render(context,request))

def deconnexion(request):
    logout(request)
    template = loader.get_template("reptiles/home.html")
    context = getUserContext(request)
    return HttpResponse(template.render(context,request))

def getUserContext(request):
    context={}
    if request.user.is_authenticated == False:
        nom = ""
        codeco = "connexion"
    else:
        nom = request.user.username
        codeco = "deconnexion"
    context["userContext"]=nom
    context["codeco"]=codeco

    return context
    