from django.contrib import admin

# Register your models here.
from expenses.models import Expenses

admin.site.register(Expenses)