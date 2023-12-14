from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()

class Distributor(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=15)
    email = models.EmailField()