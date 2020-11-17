from django.shortcuts import render,HttpResponse
from . models import Category,Image

def home(request):
    cats=Category.objects.all()
    images=Image.objects.all()
    d={'images':images,'cats':cats}
    return render(request,"home.html",d)

def category(request,cid):
    cats=Category.objects.all()

    categor=Category.objects.get(pk=cid)
    
    images=Image.objects.filter(cat=categor)

    d={'images':images,'cats':cats}
    return render(request,"home.html",d)
