# Generated by Django 3.2 on 2022-07-16 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20220716_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='approval_status',
            field=models.CharField(choices=[('на рассмотрении', 'на рассмотрении'), ('одобрено', 'одобрено')], default='на рассмотрении', max_length=20),
        ),
    ]
