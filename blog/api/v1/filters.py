from django_filters.rest_framework import FilterSet, CharFilter
from merojob.blog.models import BlogPost


class BlogPostFilter(FilterSet):
    category = CharFilter(name="category__title", lookup_expr='iexact', distinct=True)

    class Meta:
        model = BlogPost
        fields = ['category']
