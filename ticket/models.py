from django.apps import AppConfig
from django.db import models
from nest.models import Building, Apartment
from django.conf import settings

class Ticket(models.Model):
    STATUS_CHOICES = (
        ("open", "Open"),
        ("closed", "Closed"),
        ("in_progress", "In Progress"),   
    )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    appartment = models.ForeignKey(Apartment, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.CharField(STATUS_CHOICES, default="open", max_length=50 )
    
    def __str__(self):
     return f"{self.building} - {self.appartment} - {self.status} - {self.created_at}"