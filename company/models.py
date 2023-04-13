from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    count_workers = models.CharField(max_length=255)
    photo = models.ImageField(upload_to = 'main/CSS/company.img')
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # Create your models here.
