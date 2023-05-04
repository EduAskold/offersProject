from django.db import models
from django.contrib.auth.models import User


class Finder(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    photo = models.ImageField(upload_to ='finder/image/')
    location = models.CharField(max_length=255)
    min_sellary = models.IntegerField()
    resume = models.FileField(upload_to='finder/image/')
    phone = models.CharField(max_length=255)
    telegram = models.CharField(max_length= 255)
    email = models.CharField(max_length=255)
    # user = models.ForeingKey(User, on_delete=models.CASCADE)
# Create your models here.
