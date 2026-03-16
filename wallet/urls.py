from django.urls import path, include
from .views import transfer_wallet, dashboard

urlpatterns = [
    path("transfer/", transfer_wallet, name="transfer"),

    path("dashboard/", dashboard, name="dashboard"),
]