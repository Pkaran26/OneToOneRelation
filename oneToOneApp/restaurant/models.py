from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True,)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return self.place.name