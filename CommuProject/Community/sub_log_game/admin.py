from django.contrib import admin
from .models import SubLogList_game
# Register your models here.

class SubLogList_gameAdmin(admin.ModelAdmin):
    list_display = ('mainlog','charname', 'where', 'contents')

admin.site.register(SubLogList_game,SubLogList_gameAdmin)