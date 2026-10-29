from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('key_management/', views.key_management_view, name='key_management'),
    path('csr_section/', views.csr_view, name='csr_section'),
    path('aen_section/', views.aen_view, name='aen_section'),  # match view name
    path('career/', views.career_view, name='career'),
    path('career/<int:pk>/', views.career_detail_view, name='career_detail'),
    path('contact/', views.contact_view, name='contact'),

    # New SEO-friendly slug URLs
    path('partner_page/<slug:slug>/', views.PartnerPageView, name="partner_page"),
    path('business_page/<slug:slug>/', views.BusinessPageView, name="business_page"),

    # Old links (301 redirect to the new slug URL) - must stay AFTER the slug URLs
    path('partner_page/<str:name>', views.partner_page_legacy, name="partner_page_legacy"),
    path('business_page/<str:name>', views.business_page_legacy, name="business_page_legacy"),
]