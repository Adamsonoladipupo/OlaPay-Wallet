from decimal import Decimal
from plistlib import UID
from wallet.models import Wallet, Transaction, Ledger
from django.db import transaction


def transfer_wallet_to_wallet(sender: Wallet, receiver: Wallet, amount: Decimal, idempotency_key: UID, description: str = None):
    amount = Decimal(amount)
    if sender.pk == receiver.pk:
        raise Exception('cannot transfer to self')
    if amount > sender.balance:
        raise Exception('sender balance exceeds receiver balance')

    existing_tx = Transaction.objects.filter(idempotency_key = idempotency_key).first()
    if existing_tx:
        return existing_tx

    with transaction.atomic():
        receiver_wallet = Wallet.objects.select_for_update().get(pk=receiver.pk)
        sender_wallet = Wallet.objects.select_for_update().get(pk=sender.pk)

    sender_wallet.balance -= amount
    receiver_wallet.balance += amount
    sender_wallet.save(update_fields = ['balance'])
    receiver_wallet.save(update_fields = ['balance'])

    tx = Transaction.objects.create(
        sender = sender,
        receiver = receiver,
        amount = amount,
        description = description,
        transaction_type = 'CREDIT',
        idempotency_key = idempotency_key,
    )

    Ledger.objects.create(
        transaction = tx,
        amount = amount,
        wallet = sender_wallet,
        balance = sender.balance,
        transaction_type = 'DEBIT'
    )

    Ledger.objects.create(
        transaction = tx,
        amount = amount,
        wallet = receiver_wallet,
        balance_after = receiver.balance,
        transaction_type = 'CREDIT'
    )

    return tx