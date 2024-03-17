from django.urls import path,include
from FooBack import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('catpage/',views.CatPage,name="catpage"),
    path('items/',views.ItemsPage,name="items"),
    path('bookings/',views.BookingsPage,name="bookings"),
    path('notifications/',views.Notifications,name="notifications"),
    path('addcat/',views.addCat,name="addcat"),
    path('savecat/',views.addcatdata,name="savecat"),
    path('catedit/<int:pk>',views.EditCat,name="catedit"),
    path('editcatdata/<int:pk>',views.editcatdata,name="editcatdata"),
    path('delcat<int:pk>',views.DeleteCat,name="delcat"),
    path('additems/',views.AddItems,name="additems"),
    path('error/',views.Multierror,name="error"),
    path('saveitem/',views.additemdata,name="saveitem"),
    path('edititems/<int:pk>',views.EditItems,name="edititems"),
    path('saveitemedit/<int:pk>',views.saveitemedit,name="saveitemedit"),
    path('delitem/<int:pk>',views.deleteitem,name="delitem")
    

]
