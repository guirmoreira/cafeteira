from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False, default='no_email')
    cash = models.FloatField(default=0)
    # user = models.OneToOneField(User, related_name='profile')


class Product(models.Model):

    name = models.CharField(max_length=255, null=False)
    price = models.FloatField(default=0)


class Material(models.Model):
    name = models.CharField(max_length=255, null=False)
    quantidade = models.IntegerField(default=0, null=False)


class Orders(models.Model):

    product = models.CharField(max_length=255, null=False)
    token = models.IntegerField(default=0)
    delivered = models.BooleanField(null=False, default=False)

