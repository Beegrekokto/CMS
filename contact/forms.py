from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name', 'required': 'required'}),
        label='Name',
        max_length=100)

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'email_field', 'required': 'required'}),
        label='Email address',
        max_length=70)

    contact_num = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number', 'required': 'required'}),
        label='Contact number',
        max_length=15
    )

    company_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name', 'required': 'required'}),
        label='Company Name',
        max_length=50
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        label='Message')

    subject = 'Contact form'

    recipient_list = [manager[0] for manager in settings.MANAGERS]

    def construct_message(self):
        return ("From: {name} <{email}>\n\n"
                + "{message}\n" + "From company : {company_name} and Contact Number : {contact_num}").format(**self.cleaned_data)

    def send(self):
        send_mail(
            subject=self.subject,
            message=self.construct_message(),
            from_email=self.cleaned_data['email'],
            recipient_list=self.recipient_list,
            fail_silently=False, )
