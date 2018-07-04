from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView
from career.models import Vacancies, Cards, CareerTitle
from page.models import Page
from django.core.exceptions import ObjectDoesNotExist
from .forms import ResumeForm
from .models import Resume, ResumeSection
from common.views import BasePageContentMixin


class CareerView(BasePageContentMixin, TemplateView):
    model = Resume
    template_name = 'career/detail.html'
    form_class = ResumeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['career_section'] = Page.objects.get(slug='career')
        except ObjectDoesNotExist:
            context['career_section'] = None
        context['vacancies'] = Vacancies.objects.exclude(is_active=False)
        context['cards'] = Cards.objects.exclude(is_active=False)
        try:
            context['form'] = ResumeForm
        except ObjectDoesNotExist:
            context['form'] = None
        try:
            context['titles'] = CareerTitle.objects.first()
        except ObjectDoesNotExist:
            context['titles'] = None
        try:
            context['cv_drop'] = ResumeSection.objects.first()
        except ObjectDoesNotExist:
            context['cv_drop'] = None

        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            obj = user.resume.name
            y = obj.split('.')[-1]
            list1 = ["pdf", "docx", "odt", "txt", "doc"]
            if y in list1:
                user.save()
                messages.success(request, 'Form submission success')
                return HttpResponseRedirect(reverse('career'))
            else:
                messages.error(request, 'File not supported ')
                return HttpResponseRedirect(reverse('career'))
