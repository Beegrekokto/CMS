from django.contrib import admin
from .models import NewEvent

from .forms import EventForm


class EventAdmin(admin.ModelAdmin):
    form = EventForm



admin.site.register(NewEvent, EventAdmin)
