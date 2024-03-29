# Generated by Django 4.2.6 on 2024-01-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255, unique=True)),
                ('access_to_shop_management', models.BooleanField()),
                ('access_to_factory_management', models.BooleanField()),
            ],
        ),
    ]
