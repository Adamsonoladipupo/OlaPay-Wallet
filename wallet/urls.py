from django.urls import path, include

from .services.fund_wallet import paystack_callback
from .views import transfer_wallet, dashboard, fundd_wallet, fund_wallet

urlpatterns = [
    path("transfer/", transfer_wallet, name="transfer"),

    path("deposit/", fund_wallet, name="deposit"),

    path("callback/", paystack_callback, name="paystack_callback"),

    path("fund/", fundd_wallet, name="fund_wallet"),

    path("dashboard/", dashboard, name="dashboard"),
]