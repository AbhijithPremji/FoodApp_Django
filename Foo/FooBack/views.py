from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from . models import NewCatDb,ItemsDb
# Create your views here.


def home(req):
    return render(req,"home.html")

def CatPage(req):
    data = NewCatDb.objects.all()
    return render(req,"CategoryPage.html",{'data':data})

def ItemsPage(req):
    data = ItemsDb.objects.all()
    return render(req,"ItemsPage.html",{'data':data})

def BookingsPage(req):
    return render(req,"BookingsPage.html")

def Notifications(req):
    return render(req,"Notifications.html")

def addCat(req):
    return render(req,"AddCat.html")

def EditCat(req,pk):
    data = NewCatDb.objects.get(id=pk)
    return render(req,"EditCat.html",{'data':data})

def editcatdata(req,pk):
     if req.method == 'POST':
        name = req.POST.get('name')
        org = req.POST.get('orgin')
        des = req.POST.get('des')
        try:
            img = req.FILES['image'] 
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = NewCatDb.objects.get(id=pk).Catimg
        NewCatDb.objects.filter(id=pk).update(Name=name,Orgin=org, Catimg=file, Desc=des)
        return redirect(CatPage)

def DeleteCat(req,pk):
    data = NewCatDb.objects.filter(id=pk)
    data.delete() 
    return redirect(CatPage)       

def addcatdata(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        org = req.POST.get('orgin')
        des = req.POST.get('des')
        img = req.FILES['image'] 
        dat = NewCatDb(Name=name, Orgin=org, Catimg=img, Desc=des)
        dat.save()
        return redirect(addCat)
    
def AddItems(req):
    cat = NewCatDb.objects.all()
    return render(req,"AddItems.html",{'cat':cat})

def EditItems(req,pk):
    data=ItemsDb.objects.get(id=pk)
    cat = NewCatDb.objects.all()
    return render(req,"EditItems.html",{'data':data,'cat':cat})

def Multierror(req):
    return render(req,"MultiError.html")

def additemdata(req):
    if req.method == "POST":
        cat = req.POST.get('cat')
        name = req.POST.get('name')
        price = req.POST.get('price')
        desc = req.POST.get('des')
        spice = req.POST.get('spice')
        try:
            image = req.FILES['image']
            fs = FileSystemStorage()
            file=fs.save(image.name,image)
        except MultiValueDictKeyError:
            redirect(Multierror)

    val = ItemsDb(Category=cat, Name = name, Price = price, Des = desc, Itemimg = file, spice = spice)
    val.save()
    return redirect(AddItems)

def saveitemedit(req,pk):
    if req.method == "POST":
            cat = req.POST.get('cat')
            name = req.POST.get('name')
            price = req.POST.get('price')
            desc = req.POST.get('des')
            spice = req.POST.get('spice')
            try:
                image = req.FILES['image']
                fs = FileSystemStorage()
                file=fs.save(image.name,image)
            except MultiValueDictKeyError:
                file = ItemsDb.objects.get(id=pk).Itemimg
            ItemsDb.objects.filter(id=pk).update(Category=cat, Name = name, Price = price, Des = desc, Itemimg = file, spice = spice)
    return redirect(ItemsPage)
        
   

def deleteitem(req,pk):
    data=ItemsDb.objects.filter(id=pk)
    data.delete()
    return redirect(ItemsPage)
        
    


            
