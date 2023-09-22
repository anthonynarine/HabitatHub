from rest_framework import serializers
from .models import Building, Floor, Apartment, Tenant


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = "__all__"


class ApartmentSerializer(serializers.ModelSerializer):
    tenants = TenantSerializer(many=True, read_only=True)
    is_occupied = serializers.ReadOnlyField()

    class Meta:
        model = Apartment
        fields = "__all__"


class FloorSerializer(serializers.ModelSerializer):
    apartments = ApartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Floor
        fields = "__all__"


class BuildingSerializer(serializers.ModelSerializer):
    total_apartments = (
        serializers.IntegerField()
    )  # Using the method you defined in the model
    total_building_expenses = serializers.FloatField()
    total_building_income = serializers.FloatField()

    class Meta:
        model = Building
        fields = [
            "id",
            "street",
            "city",
            "num_floors",
            "total_apartments",
            "total_building_expenses",
            "total_building_income",
        ]
