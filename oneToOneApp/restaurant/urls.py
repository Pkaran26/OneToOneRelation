from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('placeform', views.placeform, name="placeform"),
    path('addplace', views.addplace, name="addplace"),
    path('restaurantform', views.restaurantform, name="restaurantform"),
    path('addrestaurant', views.addrestaurant, name="addrestaurant"),
    path('placelist', views.placelist, name="placelist"),
    path('(?P<r>[0-9]+)/delrestaurant', views.delrestaurant, name="delrestaurant"),    
]
