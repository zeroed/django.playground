from django.contrib import admin

from django.contrib import admin
from playground.models import Detector
from playground.models import Result

admin.site.register(Detector)
admin.site.register(Result)
