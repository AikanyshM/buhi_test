from rest_framework import serializers
from .models import User, Client, Application, Accountant



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ['user', ]


    
class AccountantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accountant
        fields = "__all__"
        read_only_fields = ['user', ]



class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"
