from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Wallet
from .serializer import WalletTransferSerializer
from rest_framework.response import Response
from wallet.services.intra_transfer_service import transfer_wallet_to_wallet
from rest_framework.decorators import api_view, permission_classes


# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def transfer_wallet(request):
    sender = request.user.wallet
    serializer = WalletTransferSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)


    amount = serializer.validated_data['amount']
    idempotency_key = serializer.validated_data['idempotency_key']
    description = serializer.validated_data['description']

    receiver_wallet = serializer.validated_data['receiver_wallet']
    receiver = get_object_or_404(Wallet, wallet_number=receiver_wallet.pk)
    tx = transfer_wallet_to_wallet(sender, receiver, amount, idempotency_key, description)


    return Response(
        {
            "amount": tx.amount,
            "status": tx.status,
            "reference": tx.reference,
            "created_at": tx.created_at,

         }, status=status.HTTP_201_CREATED
    )