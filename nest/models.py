from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Building(models.Model):
    # Address details
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=100, blank=True, null=True)  
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, default="USA")  
    
    num_floors = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.street}, {self.city}"
    
    def total_apartments(self):
        return sum(floor.apartments.count() for floor in self.floors.all())

    def total_building_expenses(self):
        return sum(floor.total_floor_expenses() for floor in self.floors.all())

    def total_building_income(self):
        return sum(floor.total_floor_income() for floor in self.floors.all())
    
    

class Floor(models.Model):
    floor_number = models.PositiveIntegerField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="floors")
    num_apartments = models.PositiveIntegerField(default=1)


    def total_floor_expenses(self):
        return sum(apartment.apartment_expense for apartment in self.apartments.all())

    def total_floor_income(self):
        return sum(apartment.apartment_income for apartment in self.apartments.all())

    def __str__(self):
        return f"Building {self.building.city} - Floor {self.floor_number}"
    
    class Meta:
        ordering = ['floor_number']

    

class Apartment(models.Model):
    apartment_number = models.PositiveIntegerField()
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name="apartments")
    num_bedrooms = models.PositiveIntegerField(default=0)
    num_bathrooms = models.PositiveIntegerField(default=0)
    cost_to_rent = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # This could be considered as part of apartment_income
    apartment_expense = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    apartment_income = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # icon = models.ImageField(upload_to='apartment_icons/', blank=True, null=True)

    @property
    def is_occupied(self):
            return self.tenants.exists()
        
    def save(self, *args, **kwargs):
        self.apartment_income = self.cost_to_rent - self.apartment_expense
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Floor {self.floor.floor_number} - Building {self.floor.building.city} - Apt {self.apartment_number} - {self.num_bedrooms} bedrooms"
    
    class Meta:
        ordering = ['floor__floor_number', 'apartment_number']


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
    
   
#SIGNALS
@receiver(post_save, sender=Building)
def create_floors_for_building(sender, instance, created, **kwargs):
    if created:
        for i in range(1, instance.num_floors + 1):
            Floor.objects.create(building=instance, floor_number=i)   
            
@receiver(post_save, sender=Floor)
def create_apartments_for_floor(sender, instance, created, **kwargs):
    if created:
        for i in range(1, instance.num_apartments + 1):
            Apartment.objects.create(floor=instance, apartment_number=i)