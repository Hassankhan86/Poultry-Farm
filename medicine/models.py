from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# Create your models here.


class medicine_data(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField()
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)
