from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Expenses(models.Model):
    title = models.CharField(max_length=56,)
    amount = models.CharField(max_length=56,)
    description = models.CharField(max_length=56)
    date = models.DateTimeField()
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
