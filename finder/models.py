from django.db import models



class Finder(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    photo = models.ImageField(upload_to ='main/CSS/finder.img')
    location = models.CharField(max_length=255)
    min_sellary = models.IntegerField()
    resume = models.FileField(upload_to='main/CSS/finder.img')
    phone = models.CharField(max_length=255)
    telegram = models.CharField(max_length= 255)
    email = models.CharField(max_length=255)

# Create your models here.
