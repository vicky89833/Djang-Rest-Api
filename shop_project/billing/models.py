from django.db import models

# Create your models here.
from django.db import models
from products.models import Product
from customers.models import Customer
from authentication.models import Employee
from django.db.models.signals import post_save
from django.dispatch import receiver

class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)

    def __str__(self):
        return f"Bill #{self.id} for {self.customer} - Total: ${self.total_amount}"

@receiver(post_save, sender=Bill)
def create_or_update_customer(sender, instance, created, **kwargs):
    """
    Automatically create or update a customer when a new bill is created.
    """
    if created:
        # If the bill is newly created, check if the customer exists
        customer_name = instance.customer
        customer, created = Customer.objects.get_or_create(name=customer_name)
        # Update the bill with the created customer
        instance.customer = customer
        instance.save()