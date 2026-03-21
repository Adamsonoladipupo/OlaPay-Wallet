from django.db import models

from django.conf import settings

from .util import generate_account_number, generate_reference_number

# Create your models here.

class Wallet(models.Model):
    CURRENCY_CHOICES = (
        ('NGN', 'Naira'),
        ('USD', 'Dollar'),
        ('EUR', 'Euro'),
    )
    wallet_number = models.CharField(max_length=11, unique=True, primary_key=True)
    account_number = models.CharField(max_length=11, unique=True, default=generate_account_number)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='wallet')

    # def __str__(self):
    #     return f"{"Wallet Number " + self.wallet_number }"


class Transaction(models.Model):
    reference = models.CharField(max_length=100, unique=True, default=generate_reference_number)
    TRANSACTION_TYPE = (
        ('CREDIT', 'Credit'),
        ('DEPOSIT', 'Deposit'),
    )
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    sender = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name='sender')
    receiver = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name='receiver')
    TRANSACTION_STATUS = (
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('REJECTED', 'Rejected'),
        ('FAILED', 'Failed'),
    )
    status = models.CharField(max_length=9, choices=TRANSACTION_STATUS, default='PENDING')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    idempotency_key = models.UUIDField(unique=True, blank=True, null=True, editable=False)
    reference_number = models.CharField(max_length=100, unique=True, default=generate_reference_number)



class Ledger(models.Model):
    TRANSACTION_TYPE = (
        ('CREDIT', 'Credit'),
        ('DEPOSIT', 'Deposit'),
    )
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT)
    transaction_key = models.CharField(max_length=11, unique=True, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPE, default='CREDIT')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction}  {self.transaction_type} {self.amount}"