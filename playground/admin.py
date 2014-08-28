from django.contrib import admin
from foobar.custom_admin import custom_admin_site
from django.utils.http import urlquote
from playground.models import Detector
from playground.models import Result
from playground.tasks import slow_add
import random


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


def launch_sample_run(modeladmin, request, queryset):
    for counter in range(5):
        result = slow_add.apply_async((random.randint(10, 100), random.randint(10, 100)), countdown=2)
        print(result)
        if result.ready():
            print("Task has run : %s" % result)
            if result.successful():
                print("Result was: %s" % result.result)
            else:
                if isinstance(result.result, Exception):
                    print("Task failed due to raising an exception")
                    raise result.result
                else:
                    print("Task failed without raising exception")
        else:
            print("Task has not yet run")

class DetectorAdmin(admin.ModelAdmin):
    list_display = (upper_case_name, 'description', 'last_run_date', 'run_count')
    readonly_fields = ('name', 'last_run_date', 'run_count', 'created_at')
    actions = [launch_sample_run]

admin.site.register(Detector, DetectorAdmin)
custom_admin_site.register(Detector, DetectorAdmin)


def detector_link(obj):
    # http://localhost:8000/admin/playground/result/4/
    # http://localhost:8000/admin/playground/detector/1/
    return '<a href="/admin/playground/detector/%d">%s</a>' % (obj.detector.id, urlquote(obj.detector.name))

detector_link.allow_tags = True

class ResultAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['content', 'detector', detector_link, 'value', 'duration']
    ordering = ['created_at']
    actions = [make_processed]
    readonly_fields = [detector_link, 'content', 'detector', 'value', 'duration', 'created_at']

admin.site.register(Result, ResultAdmin)
custom_admin_site.register(Result, ResultAdmin)


# https://docs.djangoproject.com/en/1.6/ref/contrib/admin/#other-methods
# https://docs.djangoproject.com/en/1.6/ref/contrib/admin/#django.contrib.admin.ModelAdmin.changelist_view
# https://docs.djangoproject.com/en/1.6/ref/contrib/admin/actions/#making-actions-available-site-wide

