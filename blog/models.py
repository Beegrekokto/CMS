import markdown

from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from .unique_slugify import unique_slugify


class AbstractLastModified(models.Model):
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugModel(models.Model):
    slug = models.SlugField(unique=True, max_length=255, blank=True)

    class Meta:
        abstract = True

    def _get_slug_text(self):
        if hasattr(self, 'name'):
            slug_text = self.name.lower()
        elif hasattr(self, 'title'):
            slug_text = self.title.lower()
        elif hasattr(self, 'alt_name'):
            if self.has_alternate_name:
                slug_text = self.alt_name.lower()
            else:
                slug_text = self.real_name.lower()
        return slug_text

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_text = self._get_slug_text()
            unique_slugify(self, slug_text)
        if self.slug and self.slug.startswith("copy-of"):
            slug_text = self._get_slug_text()
            unique_slugify(self, slug_text)
        return super().save(*args, **kwargs)


class BlogTitle(SlugModel):
    name = models.CharField(max_length=255, blank=False, null=False)
    main_image = models.ImageField(upload_to='blog_img/', default='default.png')
    logo = models.ImageField(upload_to='blog_img/', default='default.png')

    def __str__(self):
        return self.name


class BlogCategory(AbstractLastModified, SlugModel):
    blog = models.ForeignKey(BlogTitle, on_delete=models.DO_NOTHING, related_name='blogs')
    title = models.CharField(max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'title': self.slug})

    def get_post_count(self):
        return self.blogpost_set.all().filter(created_at__lte=timezone.now()).distinct().count()

    @staticmethod
    def all_category(check_blogpost=False):
        qs = BlogCategory.objects.all()
        if check_blogpost:
            qs = qs.filter(blogpost__isnull=False, blogpost__created_at__lte=timezone.now())
        return qs.distinct()

    @staticmethod
    def get_all_category(qs, check_blogpost=False):
        if check_blogpost:
            qs.filter(blogpost__isnull=False, blogpost__created_at__lte=timezone.now())
        return qs


class BlogTag(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.title


class BlogPost(AbstractLastModified, SlugModel):
    created_at = models.DateTimeField(db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=255, db_index=True)
    body = models.TextField()
    header_img = models.ImageField(upload_to='header_img/', default='default.png')
    count = models.PositiveIntegerField(auto_created=True, default=0)
    excerpt = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(BlogTag)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @staticmethod
    def all_post(check_created_at=True, check_deadline=False):
        qs = BlogPost.objects.select_related('author', 'category').prefetch_related('tags').order_by('-created_at')
        if check_created_at:
            qs = qs.filter(created_at__lte=timezone.now())
        if check_deadline:
            qs = qs.filter(Q(deadline__gte=timezone.now()) | Q(deadline__isnull=True))
        return qs

    def increase_count(self):
        self.count += 1
        self.save(update_fields=['count'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # Let the abstract default to the first 54 characters of
            # the body field and remove the html tag
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super(BlogPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'title': self.slug})


class BlogSubscribe(models.Model):
    STATUS_CHOICES = (
        ("SUBSCRIBE", 'subscribe'),
        ('UNSUBSCRIBE', 'unsubscribe'),
    )
    user_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, max_length=15)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
