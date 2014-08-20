from django.contrib import admin

from django.contrib import admin
from playground.models import Detector
from playground.models import Result
from playground.models import Taskmeta

admin.site.register(Detector)
admin.site.register(Result)
admin.site.register(Taskmeta)
