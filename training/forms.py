# from django.forms import ModelForm, DateInput
from .models import NewEvent
from django.conf.global_settings import MANAGERS
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.forms import ModelChoiceField, ModelForm
from django.db.models.query_utils import Q
from page.models import Page

def training_queryset():
    try:
        qs = Page.objects.filter(
            Q (title__icontains='training') |
            Q (title__icontains='notice')
        )
    except Exception:
        qs = Page.objects.none()
    return qs



def get_clients():
    try:
        # qs = Page.objects.get(slug='services').get_descendants()
        qs = Page.objects.filter(title__icontains='service', level=0).get().get_children()
    except Exception:
        qs = Page.objects.none()
    return qs


class EventForm(ModelForm):
    event_on = ModelChoiceField(queryset = training_queryset())

    class Meta:
        model = NewEvent
        fields = ['event_on', 'title', 'start', 'end', 'detail', 'location']


class InterestedInForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name', 'required':'required'}),
        label='Name',
        max_length=100)

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'id':'email_field', 'required':'required'}),
        label='Email address',
        max_length=70)
    
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number', 'id':'phone', 'required':'required'}),
        label='Phone Number',
        max_length=15)

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'email-class', 'id':'email_title'}),
        max_length=255)