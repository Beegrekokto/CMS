from django import template

from page.models import Page

register = template.Library()


@register.inclusion_tag('page/widgets/feature.html')
def get_feature_pages(count=5):
    return {
        'feature_pages': Page.objects.exclude(is_featured=False)
    }

@register.inclusion_tag('page/widgets/service.html')
def get_service(count=5):
    return {
        'services_pages': Page.objects.get(slug='services').get_children()[:count]
    }

@register.inclusion_tag('page/widgets/training.html')
def get_training(count=5):
    return{
        'training_pages' : Page.objects.get(slug='training').get_children()
    }


@register.filter()
def slice_string(str):
    return str.split('.')[0]
