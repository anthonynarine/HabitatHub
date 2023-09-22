
from rest_framework import viewsets, filters
from .models import Building, Floor, Apartment, Tenant
from .serializers import BuildingSerializer, FloorSerializer, ApartmentSerializer, TenantSerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']
    # http://127.0.0.1:8000/api/tenants/?search=julia