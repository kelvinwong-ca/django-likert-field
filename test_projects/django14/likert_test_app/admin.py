from django.contrib import admin
from .models import ParametersModel


class ParametersModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(ParametersModel, ParametersModelAdmin)
