from django.contrib import admin
from django.utils.html import format_html
from .models import (
    HomeBanner, HomeAboutSection, History, OurPartner, JoinUs,
    CsrHome, GroupBrandLogo, Csr, Aen, AboutItem,
    KeyManagement, CareerOpportunity, ContactMessage, FooterAbout, UsefulLink, ContactInfo, SocialMedia
)

# ------------------------------
# Image Preview Helper
# ------------------------------
def image_preview(obj):
    if obj.image:
        return format_html('<img src="{}" width="80" style="border-radius:5px;" />', obj.image.url)
    return "No Image"
image_preview.short_description = "Preview"


# ------------------------------
# HomeBanner Admin
# ------------------------------
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'is_active')

    def image_preview(self, obj):
        if obj.background_image:
            return format_html('<img src="{}" width="100" />', obj.background_image.url)
        return "-"

    image_preview.short_description = 'Background Image'


admin.site.register(HomeBanner, HomeBannerAdmin)


# ------------------------------
# HomeAboutSection Admin
# ------------------------------
@admin.register(HomeAboutSection)
class HomeAboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", image_preview)
    search_fields = ("title",)
    readonly_fields = (image_preview,)


# ------------------------------
# History Admin
# ------------------------------
@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ("year", "title", "order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("year", "title")
    ordering = ("order",)


# ------------------------------
# OurPartner Admin
# ------------------------------
@admin.register(OurPartner)
class OurPartnerAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active", image_preview)
    list_filter = ("is_active",)
    search_fields = ("title",)
    ordering = ("order",)
    readonly_fields = (image_preview,)


# ------------------------------
# JoinUs Admin
# ------------------------------
@admin.register(JoinUs)
class JoinUsAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active", image_preview)
    search_fields = ("title",)
    ordering = ("order",)
    readonly_fields = (image_preview,)


# ------------------------------
# CSR Home Admin
# ------------------------------
@admin.register(CsrHome)
class CsrHomeAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active", image_preview)
    ordering = ("order",)
    search_fields = ("title",)


# ------------------------------
# Brand Logo Admin
# ------------------------------
@admin.register(GroupBrandLogo)
class GroupBrandLogoAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active", image_preview)
    ordering = ("order",)
    search_fields = ("title",)


# ------------------------------
# CSR Admin
# ------------------------------
@admin.register(Csr)
class CsrAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", image_preview)
    list_filter = ("is_active",)
    search_fields = ("title",)
    readonly_fields = (image_preview,)


# ------------------------------
# AEN Admin
# ------------------------------
@admin.register(Aen)
class AenAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active", image_preview)
    ordering = ("order",)
    search_fields = ("title",)
    readonly_fields = (image_preview,)


# ------------------------------
# About Item Admin
# ------------------------------
@admin.register(AboutItem)
class AboutItemAdmin(admin.ModelAdmin):
    list_display = ("title", image_preview)
    search_fields = ("title",)
    readonly_fields = (image_preview,)


# ------------------------------
# Key Management Admin
# ------------------------------
@admin.register(KeyManagement)
class KeyManagementAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "order", "is_active", image_preview)
    ordering = ("order",)
    search_fields = ("name",)
    readonly_fields = (image_preview,)


# ------------------------------
# Career Opportunity Admin
# ------------------------------
@admin.register(CareerOpportunity)
class CareerOpportunityAdmin(admin.ModelAdmin):
    list_display = ("title", "job_type", "location", "status", "post_date", "deadline", "is_active")
    list_filter = ("job_type", "status", "is_active")
    search_fields = ("title", "location")
    ordering = ("order", "-post_date")


# ------------------------------
# Contact Message Admin
# ------------------------------
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_read")
    list_filter = ("is_read",)
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created_at",)


@admin.register(FooterAbout)
class FooterAboutAdmin(admin.ModelAdmin):
    list_display = ('description', 'logo')
    # Optional: allow searching by description
    search_fields = ('description',)

@admin.register(UsefulLink)
class UsefulLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    search_fields = ('title', 'url')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email')
    search_fields = ('address', 'phone', 'email')

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('link_1','link_2','link_3')
    search_fields = ('link_1', 'link_2', 'link_3')