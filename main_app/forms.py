from django import forms
from .models import Application, Client, Accountant

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class AccountantForm(forms.ModelForm):
    class Meta:
        model = Accountant
        fields = '__all__'

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'