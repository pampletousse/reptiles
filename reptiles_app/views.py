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

def create(request):

    if request.method == 'GET':
        print("get")
        #template = loader.get_template("landing/form.html")
        #form = RucheModelForm()
        #context = {"form":form}
    elif request.method == 'POST':
        #from ipdb import set_trace
        #set_trace()
        print("post")
        #template = loader.get_template("landing/form.html")
        #form = RucheModelForm()
        #context = {"form":form}
        # contexte pour sauvegarde du form
        #validation
        #save 
    else:
        print("rien")

    return HttpResponse(template.render(context,request))