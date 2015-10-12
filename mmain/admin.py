from django.contrib import admin
from mmain.models import Cereal, Manufacturer


class CerealAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'calories')


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Cereal, CerealAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
