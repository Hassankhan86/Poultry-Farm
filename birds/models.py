from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class AliveBirdsRecords(models.Model):
    birds_added = models.IntegerField(default=0)
    date = models.DateTimeField()
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)


class DeathBirdsRecords(models.Model):
    birds_died = models.IntegerField(default=0)
    date = models.DateTimeField()
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

