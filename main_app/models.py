from datetime import timedelta
from django.db import models
from account.models import User
from django.core import validators
from django.contrib.auth.models import AbstractUser
from datetime import date


class Client(models.Model):
    TYPES_USER = [
        ('клиент', 'клиент')
    ]
    client_type = models.CharField(max_length=30, choices=TYPES_USER, default = 'клиент', verbose_name = "Выберите свою роль")

    COMPANY_TYPES = [
        ('ОсОО', 'ОсОО'),
        ('ИП', 'ИП')
    ]
    company_form = models.CharField(max_length=10, choices = COMPANY_TYPES, default='ОсОО', verbose_name="Правовая форма")
    company_name = models.CharField(max_length=200, verbose_name = "Название компании")
    company_inn = models.CharField(max_length=14, verbose_name = "ИНН компании")
    phone_number = models.CharField(max_length=20, verbose_name = "Номер телефона")
    TAX_TYPE = [
        ('Общий налоговый режим', 'Общий налоговый режим'),
        ('Единый налог', 'Единый налог'),
        ('Патент', 'Патент'),
        ('Другое', 'Другое')
    ] 
    tax_regime = models.CharField(max_length=50, choices=TAX_TYPE, default='Общий налоговый режим', verbose_name = "Режим налогообложения")
    operation_amount = models.CharField(max_length=20, verbose_name = "Количество торговых операций")
    employees_quantity = models.CharField(max_length=10, verbose_name = "Количество сотрудников")
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.email


class Accountant(models.Model):
    first_last_name = models.CharField(max_length=100, verbose_name = "ФИО бухгалтера")
    birth_date = models.DateField(verbose_name = "Дата рождения")
    INN = models.CharField(max_length=14, verbose_name = "ИНН")
    accountant_phone_number = models.CharField(max_length=12, verbose_name = "Номер телефона")
    CITIES = [
        ('Бишкек', 'Бишкек'),
        ('Ош', 'Ош')
    ]
    city = models.CharField(max_length=50, choices = CITIES, default="Бишкек", verbose_name = "Выберите город")
    EDUCATION_TYPES = [
        ('Высшее', 'Высшее'),
        ('Курсы', 'Курсы'),
        ('Другое', 'Другое')
    ]
    education = models.CharField(max_length=50, choices=EDUCATION_TYPES, default="Высшее", verbose_name = "Образование")
    EXPERIENCE = [
        ('Есть', 'Есть'),
        ('Нет', 'Нет')
    ]
    experience = models.CharField(max_length=20, choices=EXPERIENCE, default='Есть', verbose_name = "Опыт работы")
    PAYMENT_TYPES = [
        ('Мбанк', 'Мбанк'),
        ('Элсом', 'Элсом')
        
    ]
    payment_methods = models.CharField(max_length=30, choices=PAYMENT_TYPES, default='Мбанк', verbose_name = "Способы оплаты")
    upload_files = models.FileField(upload_to='accountant_docs/', verbose_name = "Загрузить файлы (дипломы, сертификаты)")
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.user.email

class Application(models.Model):
    company_name = models.CharField(max_length=100)
    application_date = models.DateField(auto_now_add=True)
    TARIFF_TYPES = [
        ('Нулевой', 'Нулевой'),
        ('Базовый', 'Базовый'),
        ('Премиум', 'Премиум')
    ]
   
    tariff = models.CharField(max_length=50, choices=TARIFF_TYPES, default='Нулевой', blank=True, null=True)
    APPLICATION_STATUS = [
        ('в процессе', 'в процессе'),
        ('завершена', 'завершена'),
        ('свободная', 'свободная')

    ]
    status = models.CharField(max_length=20, choices=APPLICATION_STATUS, default='свободная', blank=False, null=False)

    SERVICES = [
        ('сдать ежемесячный отчет для ОсОО', 'сдать ежемесячный отчет для ОсОО'),
        ('сдать ежемесячный отчет для ИП', 'сдать ежемесячный отчет для ИП'),
        ('сдать декларацию', 'сдать декларацию')
    ]

    services = models.CharField(max_length=100, choices=SERVICES, blank=True, null=True)
    
    deadline = models.DateField(default=date.today() + timedelta(days=14))

    def __str__(self):
        return self.company_name



        

    