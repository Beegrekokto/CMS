from django.db import models
from tinymce.models import HTMLField
from common.validators import validate_image
from page.models import Page

class Client(models.Model):
    client_testimonial = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='client', null=True)
    title = models.CharField(max_length=255, db_index=True)
    logo = models.ImageField(upload_to='client_img/', default='default.png',
                             validators=[validate_image])
    name = models.CharField(max_length=255, db_index=True)
    designation = models.CharField(max_length=255, db_index=True)
    photo = models.ImageField(upload_to='client_photo/', default='default.png',
                              validators=[validate_image])
    content = HTMLField('Content')
    order = models.CharField(max_length=120)
    url = models.CharField(default='', max_length=120)
    is_active = models.BooleanField(default=False)
    is_testimonial = models.BooleanField(default=False)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title
