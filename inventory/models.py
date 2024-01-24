from django.db import models

# Create your models here.
class FibreBale(models.Model):
    weight = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey("employee.Employee", on_delete=models.SET_NULL, null=True)
    association = models.CharField(max_length=10)

class RopeBundle(models.Model):
    weight = models.IntegerField()
    size = models.IntegerField()
    produced = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey("employee.Employee", on_delete=models.SET_NULL, null=True)
    association = models.CharField(max_length=10)