
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100, )
    email = models.EmailField(null=True, blank=True)  # nullable and allow blank
    phone_number = models.CharField(max_length=15)
    address = models.TextField(null=True, blank=True)  # nullable and allow blank

    def __str__(self):
        return self.name