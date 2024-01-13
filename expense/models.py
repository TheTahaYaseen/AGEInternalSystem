from django.db import models

# Create your models here.
class ExpenseCategory(models.Model):
    category = models.CharField(max_length=255)

class Expense(models.Model):
    amount = models.IntegerField()
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    reason = models.TextField(null=True)
    reported_by = models.ForeignKey("employee.Employee", on_delete=models.SET_NULL, null=True)

    association = models.CharField(max_length=10)