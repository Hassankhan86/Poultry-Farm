from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class IncomingEggStock(models.Model):
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField()
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)


class OutgoingEggStock(models.Model):
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField()
    rate = models.IntegerField(default=0)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

