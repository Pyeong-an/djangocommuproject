from django.contrib import admin
from .models import LogList_game
# Register your models here.

class LogList_gameAdmin(admin.ModelAdmin):
    list_display = ('charname', 'where', 'contents')

admin.site.register(LogList_game,LogList_gameAdmin)