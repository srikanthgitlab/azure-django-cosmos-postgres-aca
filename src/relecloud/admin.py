from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Cruise)
admin.site.register(models.Destination)
admin.site.register(models.InfoRequest)
admin.site.register(models.Restaurant)
admin.site.register(models.Review)