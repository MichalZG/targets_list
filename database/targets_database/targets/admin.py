from django.contrib import admin

from .models import Target


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    model = Target

    list_display = ('name', 'ra', 'dec', 'magnitude', 'importance', 'priority')
    list_display_links = ('name',)
    list_editable = ('magnitude', 'importance', 'priority')
    ordering = ('name',)