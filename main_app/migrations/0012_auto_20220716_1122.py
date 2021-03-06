# Generated by Django 3.2 on 2022-07-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_application_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='approval_status',
            field=models.CharField(choices=[('неодобрено', 'неодобрено'), ('одобрено', 'одобрено')], default='неодобрено', max_length=20),
        ),
        migrations.AlterField(
            model_name='application',
            name='tariff',
            field=models.CharField(choices=[('Нулевой', 'Нулевой'), ('Базовый', 'Базовый'), ('Премиум', 'Премиум')], default='Нулевой', max_length=50),
        ),
    ]
