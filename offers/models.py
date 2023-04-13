from django.db import models
from company.models import Company
from finder.models import Finder

class Category(models.Model):
    name = models.CharField(max_length=255)

class Offer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    is_offers = models.TextField()
    location = models.CharField(max_length=255)
    min_selary = models.IntegerField()
    msx_selary = models.IntegerField()
    is_remote = models.BooleanField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Feedback(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    finder = models.ForeignKey(Finder, on_delete=models.CASCADE)








# Create your models here.
