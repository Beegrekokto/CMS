from django.shortcuts import render

from notice.models import Notice
from page.models import Page
from appearance.models import Appearance, Socialsite
from django.core.exceptions import ObjectDoesNotExist
from blog.models import BlogTitle, BlogPost


class BasePageContentMixin:

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['pages_menu'] = Page.objects.exclude(is_menu=False)
        try:
            ctx['company_info'] = Appearance.objects.all().first()
        except ObjectDoesNotExist:
            ctx['company_info'] = None
        ctx['socialsite_info'] = Socialsite.objects.all()
        try:
            ctx['blog'] = BlogTitle.objects.first()
        except ObjectDoesNotExist:
            ctx['blog'] = None
        try:
            ctx['popular_posts_qs'] = BlogPost.all_post(check_deadline=True).order_by('-count')[:4]
        except ObjectDoesNotExist:
            ctx['popular_posts_qs'] = None

        try:
            ctx['notices'] = Notice.objects.all()[:3]
        except ObjectDoesNotExist:
            ctx['notices'] = None
        ctx['footer_links'] = Page.objects.filter(is_footer_link=True)

        return ctx
