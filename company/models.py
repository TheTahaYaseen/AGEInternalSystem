from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    associated_bank_account = models.ForeignKey("bank_account.BankAccount", on_delete=models.SET_NULL, null=True)