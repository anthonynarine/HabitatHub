from django.contrib import admin
from .models import Building, Floor, Apartment, Tenant


admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Apartment)
admin.site.register(Tenant)