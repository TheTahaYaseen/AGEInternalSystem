# Generated by Django 4.2.6 on 2024-01-11 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bank_account', '0002_alter_bankaccount_account_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('associated_bank_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bank_account.bankaccount')),
            ],
        ),
    ]
