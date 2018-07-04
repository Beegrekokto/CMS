from django.views.generic import ListView
from gallery.models import Gallery, Photo
from page.models import Page
from django.core.exceptions import ObjectDoesNotExist
from common.views import BasePageContentMixin


class GalleryView(BasePageContentMixin, ListView):
    model = Gallery
    template_name = 'gallery/detail.html'
    queryset = Gallery.objects.exclude(is_active=False)
    context_object_name = 'gallery'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['photos'] = Photo.objects.all()

        try:
            # TODO: @aashik why icontains not exact ?
            context['gallery_section'] = Page.objects.filter(slug__icontains='gallery').get()
        except ObjectDoesNotExist:
            context['gallery_section'] = None
        return context
