from django.contrib import admin
from .models import Client, Accountant, Application

admin.site.register(Client)
admin.site.register(Accountant)
#admin.site.register(AdminUser)
admin.site.register(Application)
