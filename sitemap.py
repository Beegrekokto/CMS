from django.contrib.sitemaps import Sitemap

from blog.models import BlogPost


class MySiteSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):

        """

        :return:
        items() is simply a method that returns a list of objects.
        The objects returned will get passed to any callable methods
        corresponding to a sitemap property (location, lastmod, changefreq, and priority).
        """
        return BlogPost.objects.all()

    def lastmod(self, obj):

        """

        :param obj:
        :return:
        lastmod should return a datetime for our XML.
        """
        return obj.created_at
