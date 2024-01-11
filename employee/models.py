from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=255)
    associated_role = models.ForeignKey("role.Role", on_delete=models.SET_NULL, null=True)
    associated_bank_account = models.ForeignKey("bank_account.BankAccount", on_delete=models.SET_NULL, null=True)    
    associated_user = models.ForeignKey(User, on_delete=models.CASCADE)