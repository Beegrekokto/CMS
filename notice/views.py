from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from notice.models import Notice
from page.models import Page
from django.core.exceptions import ObjectDoesNotExist
from common.views import BasePageContentMixin
from training.models import NewEvent
from training.forms import InterestedInForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


class NoticeView(BasePageContentMixin, TemplateView):
    template_name = 'notice/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notice'] = Notice.objects.exclude(is_active=False)
        try:
            context['notice_section'] = Page.objects.get(slug='notice')
        except ObjectDoesNotExist:
            context['notice_section'] = None


        return context

