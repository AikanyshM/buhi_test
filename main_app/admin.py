from django.contrib import admin
from .models import Client, Accountant, Application
from .forms import ApplicationForm, ClientForm, AccountantForm

class ClientAdmin(admin.ModelAdmin):
    form = ClientForm
    list_display = ('user', 'company_form', 'company_name', 'company_inn', 
    'phone_number', 'tax_regime', 'operation_amount', 'employees_quantity')
    

class AccountantAdmin(admin.ModelAdmin):
    form = AccountantForm
    list_display = ('user','first_last_name', 'birth_date', 'INN', 'accountant_phone_number', 
    'city', 'education', 'experience', 'payment_methods')


class ApplicationAdmin(admin.ModelAdmin):
    form = ApplicationForm
    list_display = ('company_name', 'application_date', 'status','approval_status', 'tariff', 
    'services', 'deadline')
    list_editable = ('approval_status', )
    date_hierarchy = 'deadline'

admin.site.register(Client, ClientAdmin)
admin.site.register(Accountant, AccountantAdmin)
admin.site.register(Application, ApplicationAdmin)
