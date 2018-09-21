from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
from django import template
from django.shortcuts import get_object_or_404

register = template.Library()

def index(request):
    return render(request, "index.html")

def placeform(request):
    return render(request, "addplace.html")

def addplace(request):
    try:
        name = request.POST['name']
        addr = request.POST['addr']
        p1 = Place(name=name, address=addr)
        p1.save()
        return HttpResponse("<script>alert('success'); window.location.href='./';</script>")
    except ValueError:
        return HttpResponse("<script>alert('Field can't be blank!'); window.location.href='./';</script>")

def restaurantform(request):
    context = {}
    context['places'] = Place.objects.all()
    return render(request, "addrestaurant.html", context)

def addrestaurant(request):
    try:
        place_pk = request.POST['place']
        hotdogs = request.POST['hotdogs']
        pizza = request.POST['pizza']
        place = get_object_or_404(Place, id=place_pk)
        r1 = Restaurant(place=place, serves_hot_dogs= hotdogs, serves_pizza=pizza)
        r1.save()
        return HttpResponse("<script>alert('success'); window.location.href='./';</script>")
    except ValueError:
        return HttpResponse("<script>alert('Field can't be blank!'); window.location.href='./';</script>")

def placelist(request):
    context = {}
    context['places'] = Restaurant.objects.all()
    return render(request, "display.html", context)



@register.filter
def replaceYesNo(value):
    if str(value)=="True":
        return "Yes"
    elif str(value)=="False":
        return "No"
    

def delrestaurant(request, r=None):
    p = Place.objects.get(name = r)
    p.delete()
    return HttpResponse("<script>alert('success'); window.location.href='../';</script>")