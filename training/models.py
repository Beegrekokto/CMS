from django.db import models
from page.models import Page
from common.validators import validate_image
from tinymce.models import HTMLField
from client.models import Client


class NewEvent(models.Model):
    event_on = models.ForeignKey(Page, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    detail = models.TextField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title
