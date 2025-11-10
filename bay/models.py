from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
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
    title = models.CharField(max_length=255)
    subtitle = RichTextField('Subtitle', blank=True, null=True)
    description = RichTextField('Description')
    image = models.ImageField(upload_to='About/', blank=True, null=True)
    button_text = models.CharField(max_length=100, default='Learn More')
    button_link = models.URLField(max_length=300, default='#')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class History(models.Model):
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.year} - {self.title}"

    class Meta:
        ordering = ['order']


class OurPartner(models.Model):
    image = models.ImageField(upload_to='partners/', help_text="Upload partner logo or image")
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(default="#", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class JoinUs(models.Model):
    title = models.CharField(max_length=255, default="Join Us")
    description = models.TextField()
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
    subtitle = RichTextField('Subtitle', blank=True, null=True)
    description = RichTextField('Description')
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
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='brand_logos/')
    link = models.URLField(default="#", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or f"Brand Logo {self.id}"


class Csr(models.Model):
    image = models.ImageField(upload_to='csr/', help_text="Main image for the csr section")
    title = models.TextField(help_text="First paragraph text")
    description = models.TextField(blank=True, null=True, help_text="Second paragraph text (optional)")
    button_link = models.URLField(max_length=300, default="", help_text="Link for the Learn More button")
    is_active = models.BooleanField(default=True, help_text="Show or hide this About section")

    def __str__(self):
        return self.title


class Aen(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField('Description/AEN')
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

class AboutItem(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    list_items = models.JSONField(blank=True, null=True)
    button_text = models.CharField(max_length=100, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)

    def __str__(self):
        return self.title
# @@@@@ About Us Model @@@@@@@@@@


# @@@@@ Key management Model @@@@@@@@@@

class KeyManagement(models.Model):
    """Model to represent a key management or advisory team member."""
    title_highlight = models.CharField(max_length=100,default="KeyManagement",)
    highlight_desc = models.CharField(max_length=200,default="Group KeyManagement",)
    image = models.ImageField(upload_to='key_management/')
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=150)
    description = models.TextField(blank=True,null=True)
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
    description = models.TextField(help_text="Short description or job details.")
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
    title_highlight = models.CharField(max_length=100, default="ContactMessage")
    highlight_desc = models.CharField(max_length=200, default="Contact Description")
    address = models.CharField(max_length=200, default="Contact Address")
    phone1 = models.TextField(help_text="Contact phone1")
    phone2 = models.TextField(help_text="Contact phone2")
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Add this!
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.subject}"


# @@@@@ End Contact Model @@@@@@@@@@
