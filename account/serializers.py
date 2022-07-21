from tabnanny import verbose
from rest_framework import serializers
from .models import User
from main_app.serializers import ClientSerializer, AccountantSerializer
from main_app.models import Client, Accountant, Application


class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = ["username", "password", "password2"]

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Пароли должны совпадать')
        return data

    def save(self):
        user = User(username=self.validated_data['username'], 
                    is_staff=self.validated_data['is_staff'],
                    is_superuser=self.validated_data['is_superuser']
                    )
        user.set_password(self.validated_data['password'])
        user.save()




class ClientUserCreateSerializer(UserCreateSerializer):
    client = ClientSerializer()

    class Meta:
        model = User
        fields = ["client", "username", "password", "password2"]

    def save(self):
        user = User(username=self.validated_data['username'], 
                    is_staff=self.validated_data['is_staff'],
                    is_superuser=self.validated_data['is_superuser']
                    )
        user.set_password(self.validated_data['password'])
        user.save()
        try:
            client = Client(
                user=user, client_type = self.validated_data['client']['client_type'],
                company_form = self.validated_data['client']['company_form'],
                company_name=self.validated_data['client']['company_name'],
                company_inn=self.validated_data['client']['company_inn'],
                phone_number=self.validated_data['client']['phone_number'],
                tax_regime=self.validated_data['client']['tax_regime'],
                operation_amount=self.validated_data['client']['operation_amount'],
                employees_quantity=self.validated_data['client']['employees_quantity']
                )
            client.save()
        except Exception as e:
            print(e)
            user.delete()
        else:
            return user


class AccountantUserCreateSerializer(UserCreateSerializer):
    accountant = AccountantSerializer()

    class Meta:
        model = User
        fields = ["accountant", "username", "password", "password2"]

    def save(self):
        user = User(username=self.validated_data['username'],
                    is_staff=self.validated_data['is_staff'],
                    is_superuser=self.validated_data['is_superuser']
                    )
        user.set_password(self.validated_data['password'])
        user.save()
        try:
            accountant = Accountant(
                user=user, 
                first_last_name = self.validated_data['accountant']['first_last_name'],
                birth_date = self.validated_data['accountant']['birth_date'],
                INN=self.validated_data['accountant']['INN'],
                accountant_phone_number=self.validated_data['accountant']['accountant_phone_number'],
                city=self.validated_data['accountant']['city'],
                education=self.validated_data['accountant']['education'],
                experience=self.validated_data['accountant']['experience'],
                payment_methods=self.validated_data['accountant']['payment_methods'],
                upload_files = self.validated_data['accountant']['upload_files']
            )
            accountant.save()
        except Exception as e:
            print(e)
            user.delete()
        else:
            return user
