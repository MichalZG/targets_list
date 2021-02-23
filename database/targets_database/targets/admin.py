from django.contrib import admin
from import_export import resources
from .models import Target, TargetGroup
from import_export.admin import ImportExportModelAdmin



class TargetResource(resources.ModelResource):

    class Meta:
        model = Target
        fields = ('id', 'name', 'ra', 'dec', 'magnitude', 'cadence', 'priority', 'note')

@admin.register(Target)
class TargetAdmin(ImportExportModelAdmin):
    resource_class = TargetResource

    list_display = ('name', 'ra', 'dec', 'magnitude', 'priority', 'note')
    list_display_links = ('name',)
    list_editable = ('magnitude', 'priority')
    ordering = ('name',)

admin.site.register(TargetGroup)
