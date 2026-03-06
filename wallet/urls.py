from django.urls import path, include
from .views import transfer_wallet


urlpatterns = [
    path("transfer/", transfer_wallet, name="transfer"),
]