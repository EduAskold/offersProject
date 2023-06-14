from django.db import models
from django.contrib.auth.models import User


class Finder(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    photo = models.ImageField(upload_to ='finder/image/', null=True, blank=True)
    location = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    min_sellary = models.IntegerField(null=True, blank=True)
    resume = models.FileField(upload_to='finder/image/', null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length= 255, null=True, blank=True)
    email = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

# Create your models here.
