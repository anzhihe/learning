from django.contrib import admin
from .models import *


# Register your models here.
class NewManager(admin.ModelAdmin):
    list_display = ['id', 'vnum', 'isdelete']


admin.site.register(Category)
admin.site.register(News, NewManager)
