from django.contrib import admin

# Register your models here.
from eggs.models import *

admin.site.register(IncomingEggStock)
admin.site.register(OutgoingEggStock)