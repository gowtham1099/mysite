from django.contrib import admin

from .models import Registration


# Register your models here.

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Mobile_No', 'Area', 'Postal', 'State']


admin.site.register(Registration, RegistrationAdmin)
