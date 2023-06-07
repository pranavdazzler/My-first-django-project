from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=2500)
class users(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=200)

