from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    age=models.IntegerField(max_length=100)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=6)
