from django.db import router
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import BuildingViewSet, FloorViewSet, ApartmentViewSet, TenantViewSet

router = routers.DefaultRouter()
router.register("buildings", BuildingViewSet)
router.register("floors", FloorViewSet)
router.register("apartments", ApartmentViewSet)
router.register("tenants", TenantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
