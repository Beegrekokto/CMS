from django import template
from blog.models import BlogPost

register = template.Library()


@register.inclusion_tag('blog/widgets/sidebar/recent_blogs.html')
def get_recent_blogs(count=5):
    return {
        'blogs': BlogPost.all_post(check_deadline=True)[:count]
    }
