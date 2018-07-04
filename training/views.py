import datetime
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, FormView
from .forms import InterestedInForm
from page.models import Page
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, request, JsonResponse
from .models import NewEvent
from django.conf import settings
from common.views import BasePageContentMixin


def calendar(request):

    if request.method == 'GET':
        queryset_dict_obj = NewEvent.objects.prefetch_related('event_on').values('title', 'start', 'end', 'event_on__slug')

        # change date object to string
        final_list = [ { k:str(v) if isinstance(v, datetime.date) else v for k,v in obj.items() } for obj in queryset_dict_obj ]
        
        # return render(request, 'training/calendar.html', context={'events': final_list})
        return JsonResponse(final_list, safe=False)


class TrainingView(BasePageContentMixin, FormView, DetailView):
    model = Page
    form_class = InterestedInForm
    template_name = 'training/detail.html'

    def form_valid(self, form):

        cleaned_form = form.cleaned_data
        trainings = cleaned_form.get('title')
        subject = f"Interested In {trainings}"
        recipient_list = [manager[0] for manager in settings.MANAGERS]
        message = f""" From {cleaned_form.get('name')} <{cleaned_form.get('email')}>
        \n Contact Number: {cleaned_form.get('phone')}
        \n I am {subject} """
    
        send_mail(
            subject = subject,
            message = message,
            from_email = cleaned_form.get('email'),
            recipient_list = recipient_list,
            fail_silently= False
        )

        messages.success(self.request, 'Form Submission Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Form Submission UnSuccessful')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('traininghome', kwargs={'slug': self.kwargs.get('slug')})
    
    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        try:
            context['main_banner'] = Page.objects.get(slug=self.kwargs.get('slug'))
        except ObjectDoesNotExist:
            context['main_banner'] = None
        try:
            context['training_pages'] = Page.objects.filter(title__icontains='training', level=1).get().get_children()
        except ObjectDoesNotExist:
            context['training_pages'] = None
        try:
            context['service_pages'] = Page.objects.filter(title__icontains='service', level=0).get().get_children()
        except ObjectDoesNotExist:
            context['service_pages'] = None


        context['calendar_event'] = NewEvent.objects.all()


        context['events'] = NewEvent.objects.filter(event_on__slug=self.kwargs.get('slug'))


        return context