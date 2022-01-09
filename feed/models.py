from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class FeedS13_Incoming(models.Model):
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField()
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.quantity)


class FeedS13_Outgoing(models.Model):
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField()
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.quantity)


class FeedS16_Incoming(models.Model):
    f16_price = models.IntegerField(default=0)
    f16_quantity = models.IntegerField(default=0)
    f16_date = models.DateTimeField()
    f16_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.f16_quantity)


class FeedS16_Outgoing(models.Model):
    f16_quantity = models.IntegerField(default=0)
    f16_date = models.DateTimeField()
    f16_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.f16_quantity)