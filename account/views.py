from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token 
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from .permissions import IsAdminOrAccountant, IsAccountant, IsAdminOrAuthenticated

from main_app.serializers import ClientSerializer
from .serializers import ClientUserCreateSerializer, AccountantUserCreateSerializer
from .models import User
from account.serializers import UserCreateSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]


    def perform_create(self, serializer):
        serializer.validated_data['is_staff'] = False
        serializer.validated_data['is_superuser'] = False
        serializer.save() 
    
    

class ClientCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ClientUserCreateSerializer
    permission_classes = [AllowAny, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def perform_create(self, serializer):
        serializer.validated_data['is_staff'] = False
        serializer.validated_data['is_superuser'] = False
        serializer.save() 
    


class AdminCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAdminUser, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]


    def perform_create(self, serializer):
        serializer.validated_data['is_staff'] = False
        serializer.validated_data['is_superuser'] = True
        serializer.save()
    

class AccountantCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AccountantUserCreateSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [AllowAny, ]

    def perform_create(self, serializer):
        serializer.validated_data['is_staff'] = True
        serializer.validated_data['is_superuser'] = False
        serializer.save()