from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token 
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from .permissions import IsAdminOrAccountant, IsAccountant, IsAdminOrAuthenticated



from main_app.serializers import ClientSerializer
from .serializers import ClientUserCreateSerializer, AccountantUserCreateSerializer, AdminUserCreateSerializer
from .models import User


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
        }, status=status.HTTP_201_CREATED, headers=headers)

class ClientCreateAPIView(UserCreateAPIView):
    serializer_class = ClientUserCreateSerializer
    permission_classes = [AllowAny, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def perform_create(self, serializer):
        serializer.validated_data['is_staff'] = False
        serializer.validated_data['is_superuser'] = False
        serializer.save()
    


class AdminCreateAPIView(UserCreateAPIView):
    serializer_class = AdminUserCreateSerializer
    permission_classes = [IsAdminUser, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]


    def perform_create(self, serializer):
        serializer.validated_data['is_staff'] = False
        serializer.validated_data['is_superuser'] = True
        serializer.save()
    

class AccountantCreateAPIView(UserCreateAPIView):
    serializer_class = AccountantUserCreateSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [AllowAny, ]

    def perform_create(self, serializer):
        serializer.validated_data['is_staff'] = True
        serializer.validated_data['is_superuser'] = False
        serializer.save()