from django.contrib import admin

from .models import Appearance, Socialsite

admin.site.register([Appearance, Socialsite])
