# Generated by Django 3.2 on 2022-07-16 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('новая', 'новая'), ('завершена', 'завершена'), ('в процессе', 'в процессе')], default='новая', max_length=20),
        ),
    ]