from django.db import models

class Building(models.Model):
    location = models.CharField(max_length=255)
    # icon = models.ImageField(upload_to='building_icons/', blank=True, null=True)

    def __str__(self):
        return self.location

    def total_building_expenses(self):
        return sum(floor.total_floor_expenses() for floor in self.floors.all())

    def total_building_income(self):
        return sum(floor.total_floor_income() for floor in self.floors.all())

class Floor(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="floors")
    floor_number = models.PositiveIntegerField()

    def total_floor_expenses(self):
        return sum(apartment.apartment_expense for apartment in self.apartments.all())

    def total_floor_income(self):
        return sum(apartment.apartment_income for apartment in self.apartments.all())

    def __str__(self):
        return f"Building {self.building.location} - Floor {self.floor_number}"

class Apartment(models.Model):
    appartment_number = models.PositiveIntegerField()
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name="apartments")
    num_bedrooms = models.PositiveIntegerField()
    num_bathrooms = models.PositiveIntegerField()
    cost_to_rent = models.DecimalField(max_digits=10, decimal_places=2)  # This could be considered as part of apartment_income
    apartment_expense = models.DecimalField(max_digits=10, decimal_places=2)
    apartment_income = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # icon = models.ImageField(upload_to='apartment_icons/', blank=True, null=True)

    def __str__(self):
        return f"Floor {self.floor.floor_number} - Apt {self.pk} - {self.appartment_number} bedrooms"

class Tenant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    # image = models.ImageField(upload_to="tenant_images/", blank=True, null=True)
    apartment = models.ForeignKey(Apartment, on_delete=models.SET_NULL, null=True, blank=True, related_name='tenants')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
