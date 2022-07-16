from django.urls import path, include
from .views import ApplicationCreateAPIView, ApplicationListView, ClientListView, AccountantListAPIView

urlpatterns = [
    path('create/apps/', ApplicationCreateAPIView.as_view(), name='create_apps'),
    path('apps/', ApplicationListView.as_view(), name='apps'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('accountants/', AccountantListAPIView.as_view(), name='accountants'),
]

