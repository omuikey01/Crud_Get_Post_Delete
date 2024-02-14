from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def homepage(request):
    return render(request, "index.html")

def formfun(request):
    name = request.GET['from']
    to = request.GET['to']
    km = request.GET['km']
    pr = request.GET['price']
 
    ProductEntry.objects.create(user_from = name,
                                user_to = to,
                                km = km,
                                price = pr)
    
    data = ProductEntry.objects.all()
    return render(request, "index.html", {"alldata" : data})

def showfun(request):
    data = ProductEntry.objects.all()
    return render(request, "index.html", {"alldata" : data})


def deleteFun(request):
    idd = request.GET['deleteid']
    ProductEntry.objects.get(id=idd).delete()
    data = ProductEntry.objects.all()
    return render(request, "index.html", {"alldata" : data})