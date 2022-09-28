from django.db import models

# Create your models here.

class Newsletter(models.Model):
    email = models.EmailField(max_length=254)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=1000)

class Admin(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=500)