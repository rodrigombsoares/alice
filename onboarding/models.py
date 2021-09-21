from django.db import models

class Target(models.Model):
    email = models.EmailField(unique=True)

class Manager(models.Model):
    name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    targets = models.ManyToManyField(Target)
