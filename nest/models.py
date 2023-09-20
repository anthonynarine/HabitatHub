from django.db import models
from django.db.models import Sum

# Tenant Model
class Tenant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='tenant_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Expense Model
class Expense(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_incurred = models.DateField()

    def __str__(self):
        return f"{self.description} - ${self.amount}"

# Rental Income Model
class RentalIncome(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_received = models.DateField()
    apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE, related_name='rental_incomes')

    def __str__(self):
        return f"${self.amount} on {self.date_received}"

# Apartment Model
class Apartment(models.Model):
    floor_number = models.PositiveIntegerField()
    num_bedrooms = models.PositiveIntegerField()
    num_bathrooms = models.PositiveIntegerField()
    cost_to_rent = models.DecimalField(max_digits=10, decimal_places=2)
    tenants = models.ManyToManyField(Tenant, blank=True, related_name="apartments")
    expenses = models.ManyToManyField(Expense, blank=True, related_name="apartments")
    icon = models.ImageField(upload_to='apartment_icons/', blank=True, null=True)

    def __str__(self):
        return f"Floor {self.floor_number} - {self.num_bedrooms} bedrooms"

    def total_expenses(self):
        return self.expenses.aggregate(Sum('amount'))['amount__sum'] or 0

# Building Model
class Building(models.Model):
    location = models.CharField(max_length=255)
    apartments = models.ManyToManyField(Apartment, blank=True, related_name="buildings")
    monthly_expense = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    yearly_taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    icon = models.ImageField(upload_to='building_icons/', blank=True, null=True)

    def __str__(self):
        return self.location

    def total_apartment_expenses(self):
        return sum(apartment.total_expenses() for apartment in self.apartments.all())