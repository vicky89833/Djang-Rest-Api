from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    department = models.CharField(max_length=100 ,  default='Unknown' )
    position = models.CharField(max_length=100  , null=True, blank=True , default='Unknown' )
    total_sell = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Assuming total sell is a monetary value
    # password = models.CharField(max_length=128)  # Add a separate password field

    def __str__(self):
        return self.user.username
