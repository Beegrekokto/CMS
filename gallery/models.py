from django.db import models
from tinymce.models import HTMLField
from common.validators import validate_image


class Gallery(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    content = HTMLField('Content')
    date_created = models.DateField(auto_now=True, auto_now_add=False)
    date_modified = models.DateField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title

    def get_active_photos(self):
        return self.photo_set.filter(is_active=True)


class Photo(models.Model):
    title = models.CharField(max_length=255)
    date_added = models.DateField(auto_now=True, auto_now_add=False)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/', default='default.png', validators=[validate_image])
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title
