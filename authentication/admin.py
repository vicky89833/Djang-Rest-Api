from django.contrib import admin

# Register your models here.
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Employee

# class EmployeeAdmin(UserAdmin):
#     model = Employee
#     list_display = ['username', 'email', 'department']
    
#     search_fields = ('username', 'email')
#     ordering = ('username',)

admin.site.register(Employee)
