from django.contrib.sitemaps import Sitemap
from .models import OurConcernPageName, PartnerPageName


class BusinessSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return OurConcernPageName.objects.all()


class PartnerSitemap(BusinessSitemap):
    def items(self):
        return PartnerPageName.objects.all()