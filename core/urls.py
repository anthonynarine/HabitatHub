
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
        path("api/", include("nest.urls")),
        path("api/", include("ticket.urls")),
]
