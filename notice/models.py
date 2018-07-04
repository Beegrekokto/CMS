from django.db import models
from tinymce.models import HTMLField


class Notice(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    content = HTMLField('Content')
    order = models.CharField(max_length=120)
    publish = models.DateField(auto_now=False,auto_now_add=False,)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title

