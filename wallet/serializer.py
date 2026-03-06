from rest_framework import serializers

class WalletTransferSerializer(serializers.Serializer):
    receiver = serializers.CharField(max_length=10)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    idempotent_key = serializers.UUIDField()