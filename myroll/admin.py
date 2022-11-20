from sys import stdout
from django.contrib import admin

from .models import Sbj, Tmt, Atd

admin.site.register(Sbj)
admin.site.register(Tmt)
admin.site.register(Atd)

