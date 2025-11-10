from django.contrib import admin
from .models import *
from django.utils.html import format_html
# ==========================================
# Home Models
# ==========================================

@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title', 'subtitle')
    list_per_page = 20


@admin.register(HomeAboutSection)
class HomeAboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title',)
    list_per_page = 20


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('year', 'title')
    list_per_page = 20
    ordering = ['order']


@admin.register(OurPartner)
class OurPartnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title',)
    list_per_page = 20
    ordering = ['order']


@admin.register(JoinUs)
class JoinUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_per_page = 20
    ordering = ['order']


@admin.register(CsrHome)
class CsrHomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_per_page = 20
    ordering = ['order']


@admin.register(GroupBrandLogo)
class GroupBrandLogoAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title',)
    list_per_page = 20
    ordering = ['order']


@admin.register(Csr)
class CsrAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'preview_image')
    list_filter = ('is_active',)
    search_fields = ('title',)
    list_editable = ('is_active',)

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="60" style="object-fit:cover; border-radius:8px;" />', obj.image.url)
        return "No Image"
    preview_image.short_description = "Image Preview"


@admin.register(Aen)
class AenAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')  # remove 'created_at'
    list_editable = ('order', 'is_active')
    list_per_page = 20
    search_fields = ('title',)
    ordering = ['order']


# ==========================================
# About Us
# ==========================================


@admin.register(AboutItem)
class AboutItemAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

# ==========================================
# Key Management
# ==========================================

@admin.register(KeyManagement)
class KeyManagementAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'designation')
    list_per_page = 20
    ordering = ['order']


# ==========================================
# Career Opportunities
# ==========================================

@admin.register(CareerOpportunity)
class CareerOpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_type', 'location', 'status', 'post_date', 'deadline', 'order', 'is_active')
    list_editable = ('status', 'order', 'is_active')
    list_filter = ('job_type', 'status')
    search_fields = ('title', 'location')
    list_per_page = 20
    ordering = ['order', '-post_date']


# ==========================================
# Contact Messages
# ==========================================

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'address', 'phone1', 'phone2')  # added address & phones
    list_editable = ('is_read',)
    search_fields = ('name', 'email', 'subject', 'phone1', 'phone2')
    list_filter = ('is_read',)
    list_per_page = 20
