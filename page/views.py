from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormMixin, ProcessFormView

from page.models import Page, AboutSection, AboutSidebar, Button, SubServices
from django.core.exceptions import ObjectDoesNotExist
from common.views import BasePageContentMixin
from training.models import  NewEvent
from client.models import Client
from training.models import NewEvent
from training.forms import InterestedInForm
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import  get_object_or_404
from django.contrib import messages

class PageView(BasePageContentMixin, TemplateView):
    template_name = 'page/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # TODO: @aashik generalize these try except
        try:
            context['about_section'] = Page.objects.get(slug='about-section')
        except ObjectDoesNotExist:
            context['about_section'] = None
        try:
            context['client_section'] = Page.objects.get(slug='client-section')
        except ObjectDoesNotExist:
            context['client_section'] = None
        
        context['main_banner'] = Page.objects.exclude(is_main=False).last()

        return context


class PageDetailView(BasePageContentMixin, DetailView):
    model = Page
    template_name = 'page/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.kwargs.get('slug')
        try:
            context['page'] = Page.objects.get(slug = context['slug'])
            context['button'] = context['page'].buttons.all()
            context['all_clients'] = context['page'].client.all()
        except ObjectDoesNotExist:
           context['page'] = None

        try:
            context['recent_services'] = Page.objects.get(slug = context['slug']).get_children()
        except ObjectDoesNotExist:
            context['recent_services'] = None

        context['service_pages'] = Page.objects.filter(title__icontains='service',  level=0).get().get_children()

        context['training_pages'] = Page.objects.filter(title__icontains='training',  level=1).get().get_children()

        context['events'] = NewEvent.objects.filter(event_on__slug=context['slug'])

        context['sub_services'] = SubServices.objects.filter(service_page__slug = context['slug'])

        if len(context['sub_services']) == 0:
            context['a'] = 1
        return context


class AboutView(BasePageContentMixin, TemplateView):
    template_name = 'page/about.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['about_page'] = Page.objects.get(slug='about-us')
        except ObjectDoesNotExist:
            context['about_page'] = None

        context['about_sections'] = AboutSection.objects.all()
        context['about_sidebar'] = AboutSidebar.objects.all()

        return context

