from django import forms
from .models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name', 'email', 'phone', 'job_category', 'resume')
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'fname', 'placeholder': 'Enter Your Full Name'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Enter valid email address'}),
            'phone': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'Enter Mobile Number'}),
            'job_category': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'job', 'placeholder': 'Enter job title'}),
            'resume': forms.FileInput(attrs={'id': 'resume'}),
        }
