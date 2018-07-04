
from django import template

from notice.models import Notice

register = template.Library()


@register.inclusion_tag('notice/widgets/notice.html')
def get_notice(count=5):
    return {
        'notice': Notice.objects.all()
    }

