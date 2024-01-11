from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=255)

# Create your models here.
class BankAccount(models.Model):
    associated_bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    account_number = models.IntegerField(unique=True)