from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from merojob.blog.api.v1.views import (BlogPostListView, BlogPostDetailView, \
    BlogCategoryListView, BlogCategoryDetailView, BlogPostViewSet, BlogCategoryViewSet)

urlpatterns = [
]

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet, base_name='post')
router.register(r'categories', BlogCategoryViewSet, base_name='category')
urlpatterns += router.urls
