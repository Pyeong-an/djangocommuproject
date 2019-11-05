from django.contrib import admin
from .models import CharList
# Register your models here.

class CharListAdmin(admin.ModelAdmin):
    list_display = ('charname','charcon')

admin.site.register(CharList, CharListAdmin)
