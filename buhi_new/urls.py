from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('main/', include('main_app.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),

]




