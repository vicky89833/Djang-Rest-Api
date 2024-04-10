from django.contrib import admin

# Register your models here.
from .models import Bill , PaymentMethod
admin.site.register(PaymentMethod)
admin.site.register(Bill)