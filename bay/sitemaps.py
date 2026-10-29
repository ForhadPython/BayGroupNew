from django.contrib.sitemaps import Sitemap
from .models import OurConcernPageName, PartnerPageName


class BusinessSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # noindex kora page sitemap-e rakha thik na
        return OurConcernPageName.objects.exclude(slug='bay-emporium-ltd')


class PartnerSitemap(BusinessSitemap):
    def items(self):
        return PartnerPageName.objects.all()