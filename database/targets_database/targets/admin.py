from django.contrib import admin
from import_export import resources
from .models import Target, TargetGroup
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field, widgets

        

class TargetResource(resources.ModelResource):
    group = Field(attribute='group', column_name='group', widget=widgets.ForeignKeyWidget(TargetGroup, 'name'))

    class Meta:
        model = Target
        skip_unchanged = True
        report_skipped = True
        # exclude = ('id',)
        import_id_fields = ('name',)
        fields = (
            'name', 'group', 'ra', 'dec', 'magnitude',
            'p', 'm0', 'cadence', 'priority', 'note'
        )

    def before_import_row(self, row, **kwargs):
        _, _ = TargetGroup.objects.get_or_create(
            name=row.get('group')
        )

@admin.register(Target)
class TargetAdmin(ImportExportModelAdmin):
    resource_class = TargetResource

    list_display = ('name', 'ra', 'dec', 'magnitude', 'priority', 'note')
    list_display_links = ('name',)
    list_editable = ('magnitude', 'priority')
    ordering = ('name',)

admin.site.register(TargetGroup)
