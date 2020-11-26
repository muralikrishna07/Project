from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    address = models.TextField()
    img = models.ImageField(upload_to='pics')


class employe(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    address = models.TextField()
    img = models.ImageField(upload_to='media/')