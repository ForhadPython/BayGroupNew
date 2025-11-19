from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *

# ===================== HOME PAGE =====================
from django.shortcuts import render
from .models import *

# ===================== HOME PAGE =====================
from django.shortcuts import render


def home_view(request):
    # Home page sections
    banners = HomeBanner.objects.filter(is_active=True)
    about_section = HomeAboutSection.objects.filter(is_active=True).first()
    history_headlines = HistoryHeadline.objects.filter(is_active=True).first()  # NEW
    histories = History.objects.filter(is_active=True).order_by('order')
    partners_headline = OurPartnerHeadline.objects.filter(is_active=True).first()  # NEW
    partners = OurPartner.objects.filter(is_active=True).order_by('order')[:8]
    join_us_section = JoinUs.objects.filter(is_active=True).first()
    csr_section = CsrHome.objects.filter(is_active=True).first()
    brand_logos = GroupBrandLogo.objects.filter(is_active=True).order_by('order')
    aen_posts = Aen.objects.filter(is_active=True).order_by('order')

    business_page_view = BusinessPageName.objects.all()

    aen_headline_home = AenHeadlineHome.objects.filter(is_active=True).first()  # NEW

    # Footer section (using new models)
    footer_about = FooterAbout.objects.first()
    useful_links = FooterUsefulLink.objects.all()
    contact_info = FooterContactInfo.objects.first()
    social_media = FooterSocialMedia.objects.first() 

    context = {
        'banners': banners,
        'about_section': about_section,
        'histories': histories,
        'history_headlines': history_headlines,
        'partners_headline': partners_headline,
        'partners': partners,
        'join_us_section': join_us_section,
        'csr_section': csr_section,
        'brand_logos': brand_logos,
        'aen_posts': aen_posts,
        'footer_about': footer_about,
        'useful_links': useful_links,
        'contact_info': contact_info,
        'social_media': social_media,
        'business_page_view': business_page_view,
        'aen_headline_home': aen_headline_home,
    }

    return render(request, 'index.html', context)



# ===================== ABOUT US PAGE =====================
def about_view(request):
    about_items = AboutItem.objects.all()
    footer_about = FooterAbout.objects.first()
    useful_links = FooterUsefulLink.objects.all()
    contact_info = FooterContactInfo.objects.first()
    social_media = FooterSocialMedia.objects.all()

    about_headline = AboutItemHeadline.objects.first()

    business_page_view = BusinessPageName.objects.all()


    return render(request, 'about.html', {'about_items': about_items,'footer_about':footer_about,useful_links:'useful_links',
                                          'contact_info':contact_info,'social_media':social_media,'about_headline':about_headline,'business_page_view':business_page_view})


# ===================== KEY MANAGEMENT PAGE =====================
def key_management_view(request):
    team_members = KeyManagement.objects.filter(is_active=True).order_by('order')
    footer_about = FooterAbout.objects.first()
    useful_links = FooterUsefulLink.objects.all()
    contact_info = FooterContactInfo.objects.first()
    social_media = FooterSocialMedia.objects.all()
    key_management_headline= KeyManagementHeadline.objects.first()

    business_page_view = BusinessPageName.objects.all()

    return render(request, 'key_management.html', {'team_members': team_members,'footer_about':footer_about,useful_links:'useful_links',
                                          'contact_info':contact_info,'social_media':social_media,'key_management_headline':key_management_headline,'business_page_view':business_page_view})

# ===================== CSR PAGE =====================
def csr_view(request):
    csr_items = Csr.objects.filter(is_active=True).order_by('sequence')
    csr_page_headline = CsrHeadline.objects.first()
    # CsrHeadline
    # Footer section (using new models)
    footer_about = FooterAbout.objects.first()
    useful_links = FooterUsefulLink.objects.all()
    contact_info = FooterContactInfo.objects.first()
    social_media = FooterSocialMedia.objects.all()

    business_page_view = BusinessPageName.objects.all()

    return render(request, 'csr.html', {'csr_items': csr_items,'footer_about':footer_about,useful_links:'useful_links',
                                          'contact_info':contact_info,'social_media':social_media, 'business_page_view':business_page_view,'csr_page_headline':csr_page_headline})

# ===================== AEN PAGE =====================
def aen_view(request):
    # AEN Content
    aen_headline = AenHeadline.objects.first()
    aen_items = Aen.objects.filter(is_active=True).order_by('order')

    # Footer
    footer_about = FooterAbout.objects.first()
    useful_links = FooterUsefulLink.objects.all()
    contact_info = FooterContactInfo.objects.first()
    social_media = FooterSocialMedia.objects.all()

    # Business page
    business_page_view = BusinessPageName.objects.all()

    # CSR headline (if this is needed)
    src_headline = CsrHeadline.objects.first()

    context = {
        'aen_headline': aen_headline,
        'aen_items': aen_items,

        'footer_about': footer_about,
        'useful_links': useful_links,
        'contact_info': contact_info,
        'social_media': social_media,

        'business_page_view': business_page_view,
        'src_headline': src_headline,
    }

    return render(request, 'aen.html', context)



# ===================== CAREER PAGE =====================
def career_view(request):
    jobs = CareerOpportunity.objects.filter(is_active=True, status='active').order_by('order')
    # Footer section (using new models)
    footer_about = FooterAbout.objects.first()
    useful_links = FooterUsefulLink.objects.all()
    contact_info = FooterContactInfo.objects.first()
    social_media = FooterSocialMedia.objects.all()

    business_page_view = BusinessPageName.objects.all()

    context = {'jobs': jobs,'footer_about':footer_about,useful_links:'useful_links',
                                          'contact_info':contact_info,'social_media':social_media,'business_page_view':business_page_view}
    return render(request, 'career.html', context,)


# ===================== CAREER DETAIL PAGE =====================
def career_detail_view(request, pk):
    job = get_object_or_404(CareerOpportunity, pk=pk)
    # Footer section (using new models)
    footer_about = FooterAbout.objects.first()
    useful_links = FooterUsefulLink.objects.all()
    contact_info = FooterContactInfo.objects.first()
    social_media = FooterSocialMedia.objects.all()

    business_page_view = BusinessPageName.objects.all()

    context = {'job': job,'footer_about':footer_about,useful_links:'useful_links',
                                          'contact_info':contact_info,'social_media':social_media,'business_page_view':business_page_view}
    return render(request, 'career_detail.html', context)


# ===================== CONTACT PAGE =====================
def contact_view(request):
    success = False

    # Footer and business menu
    footer_about = FooterAbout.objects.first()
    useful_links = FooterUsefulLink.objects.all()
    contact_info = FooterContactInfo.objects.first()
    social_media = FooterSocialMedia.objects.all()
    business_page_view = BusinessPageName.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            phone1="",
            phone2="",
            address="",
            created_at=timezone.now(),
        )
        success = True

    context = {
        "footer_about": footer_about,
        "useful_links": useful_links,
        "contact_info": contact_info,
        "social_media": social_media,
        "business_page_view": business_page_view,
        "success": success,
    }

    return render(request, "contact.html", context)



def footer_partial(request):
    # Footer section (using new models)
    footer_about = FooterAbout.objects.first()
    useful_links = FooterUsefulLink.objects.all()
    contact_info = FooterContactInfo.objects.first()
    social_media = FooterSocialMedia.objects.all()

    return render(request, "include/footer.html", {
        "footer_about": footer_about,
        "useful_links": useful_links,
        "contact_info": contact_info,
        "social_media": social_media,
    })

def BusinessPageView(request, name):
    business_page = BusinessPageName.objects.filter(page_name=name).first()
    business_data = BusinessPageDetail.objects.filter(business_p=business_page).first()
    business_page_view = BusinessPageName.objects.all()

    # Footer section (using new models)
    footer_about = FooterAbout.objects.first()
    useful_links = FooterUsefulLink.objects.all()
    contact_info = FooterContactInfo.objects.first()
    social_media = FooterSocialMedia.objects.first()
    context = {
        "business_page": business_page,
        "business_data": business_data,
        "business_page_view": business_page_view,
        "footer_about": footer_about,
        "useful_links": useful_links,
        "contact_info": contact_info,
        "social_media": social_media,
    }
    return render(request, "business_page_details.html", context)