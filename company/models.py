from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    count_workers = models.CharField(max_length=255)
    photo = models.ImageField(upload_to = 'company/image/')
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # user = models.ForeingKey(User, on_delete=models.CASCADE)
    # Create your models here.
