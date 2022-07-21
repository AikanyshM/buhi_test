from datetime import timedelta
from django.db import models
from account.models import User
from django.core import validators
from django.contrib.auth.models import AbstractUser
from datetime import date


class Client(models.Model):    
    COMPANY_TYPES = [
        ('ОсОО', 'ОсОО'),
        ('ИП', 'ИП')
    ]
    company_form = models.CharField(max_length=10, choices = COMPANY_TYPES, default='ОсОО', verbose_name="Правовая форма")
    company_name = models.CharField(max_length=200, verbose_name = "Название компании")
    company_inn = models.PositiveSmallIntegerField(verbose_name = "ИНН компании", unique=True)
    phone_number = models.PositiveSmallIntegerField(verbose_name = "Номер телефона")
    TAX_TYPE = [
        ('Общий налоговый режим', 'Общий налоговый режим'),
        ('Единый налог', 'Единый налог'),
        ('Патент', 'Патент'),
        ('Другое', 'Другое')
    ] 
    tax_regime = models.CharField(max_length=50, choices=TAX_TYPE, default='Общий налоговый режим', verbose_name = "Режим налогообложения")
    operation_amount = models.PositiveSmallIntegerField(verbose_name = "Количество торговых операций")
    employees_quantity = models.PositiveSmallIntegerField(max_length=10, verbose_name = "Количество сотрудников")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')


    def __str__(self):
        return self.user.email


class Accountant(models.Model):
    first_last_name = models.CharField(max_length=100, verbose_name = "ФИО бухгалтера")
    birth_date = models.DateField(verbose_name = "Дата рождения")
    INN = models.PositiveSmallIntegerField(verbose_name = "ИНН", unique=True)
    accountant_phone_number = models.PositiveSmallIntegerField(max_length=12, verbose_name = "Номер телефона")
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, verbose_name='Пользователь')

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
   
    tariff = models.CharField(max_length=50, choices=TARIFF_TYPES, default='Нулевой', blank=False, null=False)
    APPLICATION_STATUS = [
        ('новая', 'новая'),
        ('завершена', 'завершена'),
        ('в процессе', 'в процессе')

    ]
    status = models.CharField(max_length=20, choices=APPLICATION_STATUS, default='новая', blank=False, null=False)

    SERVICES = [
        ('сдать ежемесячный отчет для ОсОО', 'сдать ежемесячный отчет для ОсОО'),
        ('сдать ежемесячный отчет для ИП', 'сдать ежемесячный отчет для ИП'),
        ('сдать декларацию', 'сдать декларацию')
    ]

    services = models.CharField(max_length=100, choices=SERVICES, blank=True, null=True)
    
    deadline = models.DateField(default=date.today() + timedelta(days=14))
    
    APPROVAl_STATUS = [
        ('на рассмотрении', 'на рассмотрении'),
        ('одобрено', 'одобрено')

    ]
    approval_status = models.CharField(max_length=20, choices=APPROVAl_STATUS, default='на рассмотрении', blank=False, null=False)

    def __str__(self):
        return self.company_name



        

    