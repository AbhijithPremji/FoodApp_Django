from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
def default_date():
    return timezone.now()

class NewCatDb(models.Model):
    Name = models.CharField( max_length=100, null=True,blank =True)
    Orgin = models.CharField( max_length=100, null=True,blank =True)
    Catimg = models.ImageField( upload_to="media/", null=True,blank=True)
    Desc = models.CharField( max_length=100, null=True,blank =True)
    Data_date = models.DateTimeField(blank=True, default=timezone.now)

 
    
    def __str__(self):
        return self.Name
    


class ItemsDb(models.Model):
    Category = models.CharField(max_length=150,null=True,blank=True)
    Name = models.CharField( max_length=100, null=True,blank =True)
    Price = models.IntegerField(null= True, blank =True)
    Des = models.CharField( max_length=100, null=True,blank =True)
    Itemimg = models.ImageField( upload_to="media/", null=True ,blank=True)
    spice = models.BooleanField(null=True,blank = True)
    Date_data = models.DateTimeField(blank=True, default=timezone.now)


    def __str__(self):
        return self.Name

class BookTable(models.Model):
     Name = models.CharField( max_length=100, null=True,blank =True)
     Mob = models.IntegerField(null= True, blank =True)
     Email = models.EmailField( max_length=254, null=True, blank=True )
     PCount = models.IntegerField(null= True, blank =True)
     Date_data = models.DateField(blank=True,null=True)

     def __str__(self):
         return self.name + " " + self.Mob
     
