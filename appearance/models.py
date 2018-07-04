from django.db import models
from django.contrib.auth.models import User


class Appearance(models.Model):
    title = models.CharField(max_length=120)
    slogan = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='site_img/', default='default.png')

    def __str__(self):
        return self.title


class Socialsite(models.Model):
    title = models.CharField(max_length=120)
    icon = models.CharField(max_length=120)
    url = models.CharField(max_length=120)

    def __str__(self):
        return self.title
