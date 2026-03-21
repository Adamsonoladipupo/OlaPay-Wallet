from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Wallet
from .serializer import WalletTransferSerializer, DashboardSerializer, DepositSerializer, FundWalletSerializer
from rest_framework.response import Response
from wallet.services.intra_transfer_service import transfer_wallet_to_wallet
from rest_framework.decorators import api_view, permission_classes
from notification.services import create_transfer_notification
from .services.dashboard_service import get_dashboard_data
from .services.deposit import deposit
from .services.fund_wallet import initiate_paystack_payment


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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def fund_wallet(request):
    receiver = request.user.wallet
    serializer = DepositSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    amount = serializer.validated_data['amount']

    transaction = deposit(receiver, amount)
    create_transfer_notification(receiver.user, amount)

    return Response(
        {"reference": transaction.reference,
         "amount": transaction.amount,
         "status": transaction.status,
         "description": transaction.description,
         "created_at": transaction.created_at,
         }, status.HTTP_201_CREATED
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def fundd_wallet(request):
    serializer = FundWalletSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = request.user
    amount = serializer.validated_data['amount']

    payment_response = initiate_paystack_payment(user, amount)

    return Response(payment_response, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    user = request.user
    dashboard_data = get_dashboard_data(user)
    serializer = DashboardSerializer(dashboard_data)
    return Response(serializer.data , status=status.HTTP_200_OK)

