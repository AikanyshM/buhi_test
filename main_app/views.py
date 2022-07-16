from os import stat
from django.shortcuts import render
from .models import User, Application, Accountant, Client
from .serializers import ApplicationSerializer, AccountantSerializer, ClientSerializer
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication


from .permissions import IsAdminOrAccountant, IsAccountant, IsAdmin


class ClientListView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminOrAccountant, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]


class ApplicationCreateAPIView(CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, ]

    

class ApplicationListView(ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminOrAccountant, ]


class AccountantListAPIView(ListAPIView):
    queryset = Accountant.objects.all()
    serializer_class = AccountantSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminOrAccountant, ]


