from django.contrib import admin
from .models import BlogCategory, BlogTag, BlogPost, BlogTitle


class BlogPostAdminMixin(admin.ModelAdmin):
    raw_id_fields = ('author', 'category', 'tags')
    search_fields = ('title', 'category__title', 'tags__title')
    list_display = ('title', 'category', 'created_at')
    fields = ['title', 'header_img', 'excerpt', 'body', 'category', 'tags', 'author', 'created_at', 'deadline', 'count']


class ExcludeFieldAdminMixin(admin.ModelAdmin):
    exclude = ['slug', ]


admin.site.register(BlogPost, BlogPostAdminMixin)
admin.site.register([BlogTag, ])
admin.site.register([BlogCategory, BlogTitle], ExcludeFieldAdminMixin)
