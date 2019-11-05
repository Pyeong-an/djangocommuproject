from django.contrib import admin
from .models import SubLogList
# Register your models here.

class SubLogListAdmin(admin.ModelAdmin):
    list_display = ('mainlog','charname', 'where', 'contents')

admin.site.register(SubLogList,SubLogListAdmin)