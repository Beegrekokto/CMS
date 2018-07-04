from django.contrib import admin
from .models import Page,AboutSidebar,AboutSection, Button, SubServices
from django import forms


@admin.register(Button)
class Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dest_url', 'is_active']
    list_editable = ['is_active']


class PageAdmin(admin.ModelAdmin):
    exclude = ['slug',]


    class Media:
        js = ("admin/js/change_order.js", )


admin.site.register(Page, PageAdmin)
admin.site.register(AboutSidebar, PageAdmin)
admin.site.register(AboutSection, PageAdmin)
admin.site.register(SubServices, PageAdmin)
