from django.contrib import messages
from django.urls import reverse
from django.views.generic.edit import FormView
from page.models import Page
from django.core.exceptions import ObjectDoesNotExist
from .forms import ContactForm
from common.views import BasePageContentMixin


class ContactView(BasePageContentMixin, FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'

    def form_valid(self, form):
        form.send()
        messages.success(self.request, 'Form Submission Successful')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Form Submission UnSuccessful')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['contact_section'] = Page.objects.get(slug__icontains='contact')
        except ObjectDoesNotExist:
            context['contact_section'] = None

        return context
