from django.shortcuts import render
from FooBack.models import NewCatDb,ItemsDb
# Create your views here.

def index(req):
    cat = NewCatDb.objects.all()
    item = ItemsDb.objects.all()

    classes = ['.pizza', '.pasta', '.fries', '.burger']
    veg_list = ItemsDb.objects.filter(spice=0).all()
    non_list = ItemsDb.objects.filter(spice=1).all()
    cxt = {'cat':cat,'item':item,'classes':classes,'veg_list':veg_list,'non_list':non_list,}
    return render(req,"index.html",cxt)


def menupage(req):
    return render(req,"menupage.html")

def about(req):
    return render(req,"about.html")

def booktable(req):
    return render(req,"TableBook.html")