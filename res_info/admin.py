from django.contrib import admin
from .models import GeneralInformation


# Register your models here.

class GIAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')


admin.site.register(GeneralInformation)
