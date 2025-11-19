from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

# @@@@@ Home Model @@@@@@@@@@
class HomeBanner(models.Model):
    title = models.CharField(max_length=255, help_text="Main title of the slide")
    subtitle = models.CharField(max_length=255, blank=True, null=True, help_text="Subtitle or tagline")
    background_image = models.ImageField(upload_to='Carousel/', help_text="Background image for the banner")
    primary_button_text = models.CharField(max_length=100, default='Our Services')
    primary_button_link = models.URLField(max_length=300, default='#')
    is_active = models.BooleanField(default=True, help_text="Show or hide this slide")

    def __str__(self):
        return self.title

class HomeAboutSection(models.Model):
    top_title = models.CharField(max_length=255, help_text="Main title of the slide")
    subtitle = CKEditor5Field(config_name='default', blank=True, null=True)
    description = CKEditor5Field('Description')
    image = models.ImageField(upload_to='About/', blank=True, null=True)
    button_text = models.CharField(max_length=100, default='Learn More')
    button_link = models.URLField(max_length=300, default='#')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.top_title

class HistoryHeadline(models.Model):
    title = models.CharField(max_length=255, default="History")
    description = models.TextField(default="Our Journey Through the Years")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class History(models.Model):
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    description = CKEditor5Field()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.year} - {self.title}"

    class Meta:
        ordering = ['order']


class OurPartnerHeadline(models.Model):
    title = models.CharField(max_length=255, default="History")
    description = models.TextField(default="Our Journey Through the Years")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class OurPartner(models.Model):
    image = models.ImageField(upload_to='partners/', help_text="Upload partner logo or image")
    title = models.CharField(max_length=255)
    description = CKEditor5Field()
    link = models.URLField(default="#", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class JoinUs(models.Model):
    title = models.CharField(max_length=255, default="Join Us")
    description = CKEditor5Field()
    button_text = models.CharField(max_length=100, default="See More")
    button_link = models.URLField(max_length=300, default="#")
    background_image = models.ImageField(upload_to='join_us/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class CsrHome(models.Model):
    title = models.CharField(max_length=255, default="Corporate Social Responsibility")
    subtitle = CKEditor5Field('Subtitle', blank=True, null=True)
    description = CKEditor5Field('Description')
    image = models.ImageField(upload_to='csr/', blank=True, null=True)
    button_text = models.CharField(max_length=100, default="Get Started")
    button_link = models.URLField(max_length=300, default="#")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class GroupBrandLogo(models.Model):
    image = models.ImageField(upload_to='brand_logos/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Logo {self.id} - Order {self.order}"


class CsrHeadline(models.Model):
    title = models.CharField(max_length=255, default="History")
    description = models.TextField(default="Our Journey Through the Years")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Csr(models.Model):
    image = models.ImageField(upload_to='csr/', help_text="Main image for the csr section")
    title = models.TextField(help_text="First paragraph text")
    description = CKEditor5Field(blank=True, null=True, help_text="Second paragraph text (optional)")
    button_link = models.URLField(max_length=300, default="", help_text="Link for the Learn More button")
    is_active = models.BooleanField(default=True, help_text="Show or hide this About section")
    sequence = models.PositiveIntegerField(default=0, help_text="Order of display")

    class Meta:
        ordering = ['sequence']  # default ordering by sequence

    def __str__(self):
        return self.title

class AenHeadlineHome(models.Model):
    title = models.CharField(max_length=255, default="Aen")
    description = models.TextField(default="Our Journey Through the Years")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class AenHeadline(models.Model):
    title = models.CharField(max_length=255, default="Aen")
    description = models.TextField(default="Our Journey Through the Years")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Aen(models.Model):
    title = models.CharField(max_length=255)
    description = CKEditor5Field('Description/AEN')
    image = models.ImageField(upload_to='aen/')
    link = models.URLField(default="#", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


#### @@@@@ Home Model @@@@@@@@@@

# @@@@@ About Us Model @@@@@@@@@@

class AboutItemHeadline(models.Model):
    title = models.CharField(max_length=255, default="History")
    description = CKEditor5Field('AboutHeadline')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class AboutItem(models.Model):
    title = models.CharField(max_length=200)
    description = CKEditor5Field('Description/AEN')
    list_items = models.JSONField(blank=True, null=True)
    button_text = models.CharField(max_length=100, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)

    position = models.PositiveIntegerField(default=0)   # <-- ordering field added

    class Meta:
        ordering = ['position']   # default sorting by position

    def __str__(self):
        return self.title
# @@@@@ About Us Model @@@@@@@@@@


# @@@@@ Key management Model @@@@@@@@@@

class KeyManagementHeadline(models.Model):
    title = models.CharField(max_length=255, default="History")
    description = CKEditor5Field('KeyManagement')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class KeyManagement(models.Model):
    """Model to represent a key management or advisory team member."""
    image = models.ImageField(upload_to='key_management/')
    name = models.CharField(max_length=200)
    designation = CKEditor5Field()
    description = CKEditor5Field()
    link = models.URLField()
    order = models.PositiveIntegerField(default=0, help_text="Controls display order on the page.")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this person from the website.")

    def __str__(self):
        return f"{self.name} ({self.designation})"

# @@@@@ End Key management Model @@@@@@@@@@


# @@@@@  Career Model @@@@@@@@@@

class CareerOpportunity(models.Model):
    """Model to represent a career/job opportunity listing."""

    JOB_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('internship', 'Internship'),
        ('contract', 'Contract'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('closed', 'Closed'),
    ]

    title = models.CharField(max_length=200, help_text="Job title (e.g. Marketing Officer, Software Engineer)")
    description = CKEditor5Field(help_text="Short description or job details.")
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='full_time')
    location = models.CharField(max_length=150, help_text="Job location, e.g. Dhaka, Chattogram")

    post_date = models.DateField(help_text="The date this job was posted.")
    deadline = models.DateField(help_text="Application deadline for this position.")

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        help_text="Set whether the job is currently active or closed."
    )

    order = models.PositiveIntegerField(default=0, help_text="Controls display order on the website.")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this job from the website.")

    class Meta:
        ordering = ['order', '-post_date']
        verbose_name = "Career Opportunity"
        verbose_name_plural = "Career Opportunities"

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"

# @@@@@  End Career Model @@@@@@@@@@


# @@@@@  Contact Model @@@@@@@@@@
class ContactMessage(models.Model):
    address = models.CharField(max_length=200, default="Contact Address")
    phone1 = models.TextField(help_text="Contact phone1")
    phone2 = models.TextField(help_text="Contact phone2")
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = CKEditor5Field()
    message = CKEditor5Field()
    created_at = models.DateTimeField(default=timezone.now)  # Add this!
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"


# @@@@@ End Contact Model @@@@@@@@@@


# @@@@@ Start Footer Model @@@@@@@@@@

class FooterAbout(models.Model):
    logo = models.ImageField(upload_to="footer/", null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return "Footer About Section"


class FooterUsefulLink(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class FooterContactInfo(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=255)

    def __str__(self):
        return "Footer Contact Information"


class FooterSocialMedia(models.Model):
    description = models.TextField()
    link_1 = models.CharField(max_length=255,null=True, blank=True)
    link_2 = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.link_1

# @@@@@ End Footer Model @@@@@@@@@@


# @@@@@ Sister Concern @@@@@@@@@@
class BusinessPageName(models.Model):
    page_name = models.CharField(max_length=100)

    def __str__(self):
        return self.page_name


class BusinessPageDetail(models.Model):
    page_title = models.CharField(max_length=200)
    image_1 = models.ImageField(upload_to="business/", null=True, blank=True)
    image_2 = models.ImageField(upload_to="business/", null=True, blank=True)
    title = models.CharField(max_length=200)
    body = CKEditor5Field()
    business_p = models.ForeignKey(BusinessPageName, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# @@@@@ Sister Concern @@@@@@@@@@