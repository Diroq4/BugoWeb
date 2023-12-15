from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    def __str__(self):
        return f"User: {self.name} Phone: {self.phone}"

class Distributor(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"Distributor: {self.name} {self.phone} {self.email }"