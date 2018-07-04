from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from common.validators import validate_image


class Page(MPTTModel):
    title = models.CharField(max_length=120)
    menu = models.CharField(max_length=120)
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=None, related_name='children', db_index=True)
    content = HTMLField('Content')
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False,auto_now_add=False,)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    order = models.CharField(max_length=120)
    url = models.CharField( max_length=120, default='', blank=True , null=True)
    excerpt = models.CharField(max_length=255, blank=True)
    is_main = models.BooleanField(default=False)
    is_menu = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_footer_link = models.BooleanField(default=False)
    is_title = models.BooleanField(default=True)
    featured_pic = models.ImageField(upload_to = 'pic_folder/', default='default.png',
                                     validators=[validate_image])
    featured_icon = models.ImageField(upload_to = 'pic_folder/', default='default.png',
                                      validators=[validate_image])

    class MPTTMeta:
        order_insertion_by = ['order']

    class Meta:
        unique_together = ('slug', 'parent',)    #enforcing that there can not be two
    
    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Page.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        if not self.url:
            self.url='/page/{}'.format(self.slug)
        
        if self.is_main:
            self.__class__.objects.exclude(slug=self.slug).update(is_main=False)

        super().save(*args, **kwargs)


class AboutSection(models.Model):
    about_title = models.CharField(max_length=120)
    about_content = HTMLField('Content')
    
    def __str__(self):
        return self.about_title


class AboutSidebar(models.Model):
    sidebar_title = models.CharField(max_length=120)
    sidebar_pic = models.ImageField(upload_to = 'pic_folder/', default='default.png', validators=[validate_image])
    sidebar_content = HTMLField('Content')

    def __str__(self):
        return self.sidebar_title


class Button(models.Model):
    page = models.ForeignKey(Page, related_name='buttons', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    dest_url = models.CharField(max_length=120)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']


class SubServices(models.Model):
    service_page = models.ForeignKey(Page, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    featured_icon = models.ImageField(upload_to='pic_folder/', default='default.png', validators=[validate_image])
    content = HTMLField('content')

    def __str__(self):
        return self.title
