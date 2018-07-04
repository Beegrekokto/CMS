from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import detail_route
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from merojob.blog.api.v1.filters import BlogPostFilter
from merojob.blog.models import BlogPost, BlogCategory
from merojob.blog.serializers import (BlogPostListSerializer, BlogPostDetailSerializer, BlogCategoryListSerializer, \
    BlogCategoryDetailSerializer)


class BlogPostListView(ListAPIView):
    queryset = BlogPost.all_post()
    serializer_class = BlogPostListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = BlogPostFilter


class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.all_post()
    serializer_class = BlogPostDetailSerializer
    lookup_field = 'slug'


class BlogPostViewSet(ReadOnlyModelViewSet):
    queryset = BlogPost.all_post()
    lookup_field = 'slug'
    serializer_class = BlogPostListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BlogPostDetailSerializer
        return self.serializer_class


class BlogCategoryViewSet(ReadOnlyModelViewSet):
    queryset = BlogCategory.all_category(check_blogpost=True)
    lookup_field = 'slug'
    serializer_class = BlogCategoryListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BlogCategoryDetailSerializer
        return self.serializer_class

    @detail_route()
    def posts(self, request, slug=None):
        category = self.get_object()
        posts = BlogPost.all_post().filter(category=category)
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = BlogPostListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = BlogPostListSerializer(posts, many=True)
        return Response(data={'results': serializer.data})


class BlogCategoryListView(ListAPIView):
    queryset = BlogCategory.all_category(check_blogpost=True)
    serializer_class = BlogCategoryListSerializer


class BlogCategoryDetailView(RetrieveAPIView):
    queryset = BlogCategory.all_category(check_blogpost=True)
    serializer_class = BlogCategoryDetailSerializer
