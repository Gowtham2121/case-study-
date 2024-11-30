# services/admin.py

from django.contrib import admin
from .models import Customer, ServiceRequest  # Import your models here

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'description', 'status')
