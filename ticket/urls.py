from django.db import router
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import TicketViewset

router = routers.DefaultRouter()
router.register("ticket", TicketViewset, basename="tickets")
# basename is requried here b/c a static queryset is not used 
# see this model's view and the views of the Building etc.

urlpatterns = [
    path('', include(router.urls)),
]
