from django.contrib import admin

# Register your models here.
from employee.models import *

admin.site.register(employee_data)
admin.site.register(SalaryPaid)

