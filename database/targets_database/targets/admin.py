from django.contrib import admin

from .models import Target, TargetGroup


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    model = Target

    list_display = ('name', 'ra', 'dec', 'magnitude', 'priority', 'note')
    list_display_links = ('name',)
    list_editable = ('magnitude', 'priority')
    ordering = ('name',)

admin.site.register(TargetGroup)
