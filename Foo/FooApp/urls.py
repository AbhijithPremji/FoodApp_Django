from django.urls import path,include
from FooApp import views  




urlpatterns = [
   path('index/',views.index,name="index"),
   path('menu/',views.menupage, name="menupage"),
   path('about/',views.about,name="about"),
   path('table-book/',views.booktable,name="table-book"),
   
]


