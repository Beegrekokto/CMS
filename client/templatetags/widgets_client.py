from django import template

from client.models import Client

register = template.Library()


@register.inclusion_tag('client/widgets/client.html')
def get_client(count=5):
    return {
        'client': Client.objects.all(),
    }


@register.inclusion_tag('client/widgets/testimonial.html')
def get_testimonial(count=5):
    return {
        'testimonial': Client.objects.exclude(is_testimonial=False),
    }
