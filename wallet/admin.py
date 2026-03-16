from pyclbr import Class

from django.contrib import admin
from .models import Wallet, Transaction, Ledger
# Register your models here.

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['wallet_number', 'account_number', 'balance', 'currency', 'status']
    list_editable = ['status']
    list_per_page = 10


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['reference', 'idempotency_key', 'amount', 'receiver', 'sender', 'reference_number', 'status']

@admin.register(Ledger)
class LedgerAdmin(admin.ModelAdmin):
    list_display = ['transaction', 'transaction_key', 'balance', 'amount', 'transaction_type', 'created_at']