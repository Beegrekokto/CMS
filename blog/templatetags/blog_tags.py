from django import template
from blog.models import BlogPost

register = template.Library()


@register.simple_tag
def get_posts_by_category(category, check_deadline=False):
    return BlogPost.all_post(check_deadline=check_deadline).filter(category=category)[:6]


@register.simple_tag
def get_count_posts_by_month(month, year):
    return BlogPost.all_post().filter(created_at__month=month, created_at__year=year).count()
