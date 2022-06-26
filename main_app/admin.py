from django.contrib import admin
from .models import Client, Accountant, AdminUser, Application

admin.site.register(Client)
admin.site.register(Accountant)
admin.site.register(AdminUser)
admin.site.register(Application)
