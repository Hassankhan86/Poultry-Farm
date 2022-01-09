from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class employee_data(models.Model):
    emp_name = models.CharField(max_length=20)
    emp_salary = models.IntegerField(default=0)
    emp_cnic = models.IntegerField(default=0)
    emp_num = models.IntegerField(default=0)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    emp_joining_date = models.DateTimeField()

    def __str__(self):
        return str(self.emp_name)


class SalaryPaid(models.Model):
    amount = models.IntegerField(default=0)
    date = models.DateTimeField()
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
