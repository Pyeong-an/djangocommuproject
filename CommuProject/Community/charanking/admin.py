from django.contrib import admin
from .models import charanking
# Register your models here.

class charankingAdmin(admin.ModelAdmin):
    list_display = ('charname', 'logcount')

admin.site.register(charanking,charankingAdmin)
