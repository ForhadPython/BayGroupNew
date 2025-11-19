from django.contrib import admin
from django.utils.html import format_html
from .models import *
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
    list_display = ( "is_active", image_preview)
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
    list_display = ('id', 'image_preview', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('id',)
    ordering = ('order',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Logo Preview'


# ------------------------------
# CSR Admin
# ------------------------------
@admin.register(Csr)
class CsrAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "sequence", image_preview)
    list_filter = ("is_active",)
    search_fields = ("title",)
    readonly_fields = (image_preview,)
    ordering = ('sequence',)  # admin list default ordering


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
# ===== Footer About =====
@admin.register(FooterAbout)
class FooterAboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'logo_preview', 'description')

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="100" />', obj.logo.url)
        return "-"
    logo_preview.short_description = 'Logo Preview'

# ===== Footer Useful Links =====
@admin.register(FooterUsefulLink)
class FooterUsefulLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    search_fields = ('title', 'url')

# ===== Footer Contact Info =====
@admin.register(FooterContactInfo)
class FooterContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email')
    search_fields = ('address', 'phone', 'email')

# ===== Footer Social Media =====
@admin.register(FooterSocialMedia)
class FooterSocialMediaAdmin(admin.ModelAdmin):
    list_display = ('link_1', 'link_2')
    search_fields = ('link_1', 'link_2')


# ------------------------------
# Start For all Headline
# ------------------------------


@admin.register(HistoryHeadline)
class HistoryHeadlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title', 'description')

@admin.register(OurPartnerHeadline)
class OurPartnerHeadlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title', 'description')

@admin.register(AboutItemHeadline)
class AboutItemHeadlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')

@admin.register(KeyManagementHeadline)
class KeyManagementHeadlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')

@admin.register(BusinessPageName)
class BusinessPageNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'page_name')
    search_fields = ('page_name',)


@admin.register(BusinessPageDetail)
class BusinessPageDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'page_title', 'title', 'business_p')
    search_fields = ('page_title', 'title')
    list_filter = ('business_p',)

@admin.register(CsrHeadline)
class CsrHeadlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')

@admin.register(AenHeadline)
class AenHeadlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')

@admin.register(AenHeadlineHome)
class AenHeadlineHomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        ('Contact Info', {
            'fields': ('address', 'phone1', 'phone2')
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )