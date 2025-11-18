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

    path('business_page/<name>', views.BusinessPageView, name="business_page"),
]

