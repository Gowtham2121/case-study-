# services/models.py

from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=1  # Replace '1' with the ID of the default user
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name


class ServiceRequest(models.Model):
    SERVICE_CHOICES = [
        ('Installation', 'Installation'),
        ('Repair', 'Repair'),
        ('Inquiry', 'Inquiry'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request by {self.customer.name} - {self.request_type}"
