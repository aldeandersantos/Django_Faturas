# Generated by Django 5.0.1 on 2024-01-28 23:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_faturas', '0003_remove_compra_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Fatura',
        ),
    ]
