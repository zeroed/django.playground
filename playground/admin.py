from django.contrib import admin

from django.contrib import admin
from playground.models import Detector
from playground.models import Result
from playground.models import Taskmeta

admin.site.register(Taskmeta)

"""
Relevant Docs:
https://docs.djangoproject.com/en/dev/ref/contrib/admin/
"""

def make_processed(modeladmin, request, queryset):
    queryset.update(status='p')

make_processed.short_description = "Mark selected result as processed"


def upper_case_name(obj):
    return ("%s" % (obj.name, )).upper()
upper_case_name.short_description = 'Name'


class DetectorAdmin(admin.ModelAdmin):
    list_display = (upper_case_name, 'description', 'last_run_date', 'run_count')
    readonly_fields = ('last_run_date', 'run_count', 'created_at')

admin.site.register(Detector, DetectorAdmin)

class ResultAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['content', 'detector', 'value', 'duration']
    ordering = ['created_at']
    actions = [make_processed]
    readonly_fields = list_display

admin.site.register(Result, ResultAdmin)
