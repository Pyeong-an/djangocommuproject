from django.contrib import admin
from .models import LogList
# Register your models here.

class LogListAdmin(admin.ModelAdmin):
    list_display = ('charname', 'where', 'contents')

admin.site.register(LogList,LogListAdmin)