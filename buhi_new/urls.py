from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('main/', include('main_app.urls'))

]



if settings.DEBUG:
    urlpatterns += [
        path('', include('rest_framework.urls')),

    ]