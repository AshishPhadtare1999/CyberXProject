from pyexpat import model
from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    location=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)