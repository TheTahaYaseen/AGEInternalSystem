# Generated by Django 4.2.6 on 2024-01-11 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_number',
            field=models.IntegerField(unique=True),
        ),
    ]
