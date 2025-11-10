from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *

# ===================== HOME PAGE =====================
def home_view(request):
    banners = HomeBanner.objects.filter(is_active=True)
    about_section = HomeAboutSection.objects.filter(is_active=True).first()
    histories = History.objects.filter(is_active=True).order_by('-year')
    partners = OurPartner.objects.filter(is_active=True).order_by('order')
    join_us_section = JoinUs.objects.filter(is_active=True).first()
    csr_section = CsrHome.objects.filter(is_active=True).first()
    brand_logos = GroupBrandLogo.objects.filter(is_active=True).order_by('order')
    aen_posts = Aen.objects.filter(is_active=True).order_by('order')

    context = {
        'banners': banners,
        'about_section': about_section,
        'histories': histories,
        'partners': partners,
        'join_us_section': join_us_section,
        'csr_section': csr_section,
        'brand_logos': brand_logos,
        'aen_posts': aen_posts,
    }
    return render(request, 'index.html', context)

# ===================== ABOUT US PAGE =====================
def about_view(request):
    about_items = AboutItem.objects.all()
    return render(request, 'about.html', {'about_items': about_items})

# ===================== KEY MANAGEMENT PAGE =====================
def key_management_view(request):
    team_members = KeyManagement.objects.filter(is_active=True).order_by('order')
    return render(request, 'key_management.html', {'team_members': team_members})

# ===================== CSR PAGE =====================
def csr_view(request):
    csr_items = Csr.objects.filter(is_active=True)
    return render(request, 'csr.html', {'csr_items': csr_items})

# ===================== AEN PAGE =====================
def aen_view(request):
    aen_items = Aen.objects.filter(is_active=True).order_by('order')
    context = {'aen_items': aen_items}
    return render(request, 'aen.html', context)

# ===================== CAREER PAGE =====================
def career_view(request):
    jobs = CareerOpportunity.objects.filter(is_active=True, status='active').order_by('order')
    context = {'jobs': jobs}
    return render(request, 'career.html', context)

# ===================== CAREER DETAIL PAGE =====================
def career_detail_view(request, pk):
    job = get_object_or_404(CareerOpportunity, pk=pk)
    context = {'job': job}
    return render(request, 'career_detail.html', context)

# ===================== CONTACT PAGE =====================
def contact_view(request):
    success = False
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        phone1 = request.POST.get("phone1", "")
        phone2 = request.POST.get("phone2", "")
        address = request.POST.get("address", "")

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            phone1=phone1,
            phone2=phone2,
            address=address,
            created_at=timezone.now(),
        )
        success = True

    context = {
        "success": success,
        "contact_info": ContactMessage.objects.last()  # optional: last message
    }
    return render(request, "contact.html", context)
