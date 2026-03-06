from django.core.serializers import serialize
from django.shortcuts import render

from .serializer import UserSerializer, LoginSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from services.onboarding_service import create_user_and_wallet

# Create your views here.

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user, wallet = create_user_and_wallet(serializer.validated_data)

    return Response({'message':'Registration Successful'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    return Response(
        serializer.validated_data,
        status=status.HTTP_200_OK
    )

