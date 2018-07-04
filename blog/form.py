from django import forms
from .models import BlogSubscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = BlogSubscribe
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email-Address'}),
        }
