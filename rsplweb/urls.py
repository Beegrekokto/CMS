"""rsplweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from page import views
from sitemap import MySiteSitemap


admin.site.site_header = "**********Real Solutions Pvt Ltd.**********"
admin.site.site_title = 'Real Solution admin site'
admin.site.index_title = 'Real Solution Admin Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('page/', include('page.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('client/', include('client.urls')),
    path('notice/', include('notice.urls')),
    path('training/', include('training.urls')),
    path('gallery/', include('gallery.urls')),
    path('career/', include('career.urls')),
    path('blogmap/', sitemap, {'sitemaps': {'entry': MySiteSitemap}},
         name='django.contrib.sitemaps.views.sitemap'),
    path('', views.PageView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)