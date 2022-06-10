from django.contrib import admin
from .models import *


# Register your models here.

class CategoryStackedInline(admin.StackedInline):  # TabularInline
    model = Gun
    extra = 3


class GunAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'num', 'created_time', 'show_num']

    list_per_page = 1

    actions_on_top = True

    actions_on_bottom = True

    search_fields = ['id', 'name']

    fieldsets = (
        ('枪的名字', {'fields': ('name',)}),
        ('其他', {'fields': ('num', 'gt')}),
    )


admin.site.register(Gun, GunAdmin)


@admin.register(GunType)
class GunTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_time']
    inlines = [CategoryStackedInline]

# admin.site.register(GunType)
