from django.contrib import admin

# Register your models here.
from feed.models import *

admin.site.register(FeedS13_Incoming)
admin.site.register(FeedS13_Outgoing)

admin.site.register(FeedS16_Incoming)
admin.site.register(FeedS16_Outgoing)