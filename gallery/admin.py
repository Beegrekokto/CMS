from django.contrib import admin
from .models import Gallery, Photo


def make_active(queryset):
    queryset.update(is_active=True)


def make_deactive(queryset):
    queryset.update(is_active=False)


make_active.short_description = "Activate"
make_deactive.short_description = "Deactivate"


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'gallery', 'is_active')
    actions = [make_active, make_deactive]


admin.site.register(Gallery)
admin.site.register(Photo, PhotoAdmin)
