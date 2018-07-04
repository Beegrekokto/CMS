from django.urls import path
from .views import BlogIndexView, BlogPostByCategory, BlogPostDetail, BlogPostSearch

app_name = 'blog'
urlpatterns = [
    path('', BlogIndexView.as_view(), name='index'),
    path('category/<slug:title>/', BlogPostByCategory.as_view(), name='category_detail'),
    path('post/detail/<slug:title>/', BlogPostDetail.as_view(), name='post_detail'),
    path('post/search/', BlogPostSearch.as_view(), name='post_search'),
]
