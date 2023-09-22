from django.contrib import admin
from .models import Building, Floor, Apartment, Tenant

from django.contrib import admin
from .models import Building, Floor, Apartment, Tenant

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('street', 'num_floors', 'total_apartments_in_building')

    def total_apartments_in_building(self, obj):
        return obj.total_apartments()
    total_apartments_in_building.short_description = 'Total Apartments'

@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('building', 'floor_number', 'num_apartments')
    # Other configurations...

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('floor', 'apartment_number') 
    
    def save_model(self, request, obj, form, change):
        obj.apartment_income = obj.cost_to_rent - obj.apartment_expense
        super().save_model(request, obj, form, change)
    # Other configurations...

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_building', 'get_floor', 'get_apartment_number')  

    def get_building(self, obj):
        return obj.apartment.floor.building.city
    get_building.short_description = 'Building'

    def get_floor(self, obj):
        return obj.apartment.floor.floor_number
    get_floor.short_description = 'Floor'

    def get_apartment_number(self, obj):
        return obj.apartment.apartment_number
    get_apartment_number.short_description = 'Apartment Number'
