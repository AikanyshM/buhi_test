from django.urls import path, include
from .views import ClientCreateAPIView, AdminCreateAPIView, AccountantCreateAPIView



urlpatterns = [
    path('register/client', ClientCreateAPIView.as_view(), name='register_client'),
    path('create/admin/', AdminCreateAPIView.as_view(), name='create_admin'),
    path('create/accountant/', AccountantCreateAPIView.as_view(), name='create_accountant'),


    
    
    
    ]