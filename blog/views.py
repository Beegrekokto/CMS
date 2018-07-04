from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Prefetch
from appearance.models import Appearance, Socialsite
from notice.models import Notice
from .models import BlogPost, BlogCategory, BlogTitle
from appearance.models import Appearance, Socialsite
from page.models import Page


class BlogCategoryMixin:
    """
    Mixin to render block category and popular posts all over the blog templates.
    """
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        qs = BlogTitle.objects.filter(id__gte=1).prefetch_related(
            Prefetch(
                'blogs',
                queryset=BlogCategory.objects.prefetch_related('blogpost_set')
            )
        )
        try:
            ctx['blog_heading'] = qs.first()
        except:
            ctx['blog_heading'] = None

        ctx['blog_category_qs'] = BlogCategory.get_all_category(ctx['blog_heading'].blogs.all(), check_blogpost=False)
        ctx['popular_posts_qs'] = BlogPost.all_post(check_deadline=True).order_by('-count')[:4]
        try:
            ctx['company_info'] = Appearance.objects.all().first()
        except ObjectDoesNotExist:
            ctx['company_info'] = None
        ctx['socialsite_info'] = Socialsite.objects.all()

        try:
            ctx['notices'] = Notice.objects.all()[:3]
        except ObjectDoesNotExist:
            ctx['notices'] = None

        try:
            ctx['footer_links'] = Page.objects.filter(is_footer_link=True)
        except ObjectDoesNotExist:
            ctx['footer_link'] = None
        try:
            ctx['blog_page_title'] = BlogTitle.objects.first()
        except ObjectDoesNotExist:
            ctx['blog_page_title'] = None
        ctx['pages_menu'] = Page.objects.exclude(is_menu=False)

        return ctx


class BlogIndexView(BlogCategoryMixin, ListView):
    """
    Landing view for blog app.
    """
    model = BlogPost
    template_name = 'blog/base_blog.html'
    queryset = BlogPost.all_post(check_deadline=True).order_by('?')[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['blog_page_title'] = BlogTitle.objects.first()
        except ObjectDoesNotExist:
            context['blog_page_title'] = None
        try:
            context['pages_menu'] = Page.objects.exclude(is_menu=False)
        except ObjectDoesNotExist:
            context['pages_menu'] = None

        return context


class BlogPostByCategory(BlogCategoryMixin, ListView):
    """
    View to display the list of blog posts according to their category being selected.
    """
    model = BlogPost
    template_name = 'blog/post_by_category.html'
    paginate_by = 5
    slug_url_kwarg = 'title'

    def get(self, *args, **kwargs):
        self.blog_categ = get_object_or_404(BlogCategory, slug=self.kwargs['title'])
        return super(BlogPostByCategory, self).get(*args, **kwargs)

    def get_queryset(self):
        qs = super(BlogPostByCategory, self).get_queryset().filter(category=self.blog_categ)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super(BlogPostByCategory, self).get_context_data(**kwargs)
        ctx['blog_categ'] = self.blog_categ
        try:
            ctx['blog_page_title'] = BlogTitle.objects.first()
        except ObjectDoesNotExist:
            ctx['blog_page_title'] = None
        try:
            ctx['pages_menu'] = Page.objects.exclude(is_menu=False)
        except ObjectDoesNotExist:
            ctx['pages_menu'] = None

        return ctx


class BlogPostDetail(BlogCategoryMixin, DetailView):
    """
    View to display the detail of blog post.
    """
    model = BlogPost
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'title'

    def get(self, *args, **kwargs):
        self.get_object().increase_count()
        return super(BlogPostDetail, self).get(*args, **kwargs)


class BlogPostSearch(BlogCategoryMixin, ListView):
    """
    This view returns the search results of blog posts.
    """
    model = BlogPost
    template_name = 'blog/search_blog.html'
    paginate_by = 5
    context_object_name = 'blog_posts'

    def get_queryset(self):
        self.search = self.request.GET.get('search', None)
        qs = BlogPost.all_post()
        if self.search:
            qs = BlogPost.all_post().filter(title__icontains=self.search)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super(BlogPostSearch, self).get_context_data(**kwargs)
        ctx['search_q'] = self.search
        return ctx
