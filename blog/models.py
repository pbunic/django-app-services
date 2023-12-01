from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from mdeditor.fields import MDTextField
from taggit.managers import TaggableManager


class Info(models.Model):
    """Site-related base informations."""
    base_title = models.CharField(max_length=30, help_text='Navigation spot title.')
    home_title = models.CharField(max_length=50, help_text='Landing page title.')
    home_paragraph = models.TextField(max_length=500, help_text='Landing page short introduction.')
    about_blog = models.TextField(max_length=2500, help_text='Blog vision and summary.')
    about_author = models.TextField(max_length=2500, help_text='Some informations about author.')
    contact_email = models.EmailField(help_text='Email for contact.')
    copyright = models.CharField(max_length=100, help_text='Bottom copyright text.')

    # Manager
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Informations'

    def __str__(self):
        return 'Website base informations'


# Custom managers for Footer links
class FooterWebsiteManager(models.Manager):
    """Custom manager for filtering website-related footer links."""
    def get_queryset(self):
        return super().get_queryset().filter(link_section=Footer.Section.WEBSITE)


class FooterOtherManager(models.Manager):
    """Custom manager for filtering other non-specific footer links."""
    def get_queryset(self):
        return super().get_queryset().filter(link_section=Footer.Section.OTHER)


class FooterSocialManager(models.Manager):
    """Custom manager for filtering social media related footer links."""
    def get_queryset(self):
        return super().get_queryset().filter(link_section=Footer.Section.SOCIAL)


class Footer(models.Model):
    """Footer links."""

    class Section(models.TextChoices):
        """Footer links grouping."""
        WEBSITE = 'WL', 'Website links'
        OTHER = 'OL', 'Other links'
        SOCIAL = 'SL', 'Social links'

    link_name = models.CharField(max_length=50)
    link_slug = models.SlugField(max_length=200, blank=True, help_text='Slug for website/other.')
    link_url = models.URLField(max_length=200, blank=True, help_text='URL for social.')
    link_section = models.CharField(max_length=2, choices=Section.choices)
    template_title = models.CharField(max_length=100, blank=True)
    template_body = MDTextField(blank=True)

    # Managers
    objects = models.Manager()
    website = FooterWebsiteManager()
    other = FooterOtherManager()
    social = FooterSocialManager()

    class Meta:
        verbose_name_plural = 'Footer Map'
        ordering = ['link_section']
        indexes = [
            models.Index(fields=['link_section']),
        ]

    def __str__(self):
        return self.link_name

    def get_absolute_url(self):
        # for internal urls
        return reverse('blog:general_info', args=[self.link_slug])


class Newsletter(models.Model):
    """Website subscriptions to the newsletters."""
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)
    subscribed = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Subscriptions'
        ordering = ['-subscribed']
        indexes = [
            models.Index(fields=['-subscribed']),
        ]

    def __str__(self):
        return self.email


class TechStack(models.Model):
    """Professional working stack."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, help_text='Name of technology.')
    icon = models.ImageField(upload_to='techstack/', help_text='Logo icon.')
    description = models.TextField(max_length=2500, help_text='Just core description of service-related usage.')
    url = models.URLField(max_length=150, help_text='Website of the technology.')

    # Manager
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Techstack'
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    """Custom manager for filtering published posts."""
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """Post publishing."""

    class Status(models.TextChoices):
        """Post status."""
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        ARCHIVED = 'AR', 'Archived'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    imagecover = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)
    body = MDTextField()
    tags = TaggableManager(
        verbose_name=_('Tags'),
        help_text=_('A comma-separated tags. '
                    'Use quotes for multiple words '
                    'and lowercase letters.')
    )
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    # Managers
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])


class HomeLab(models.Model):
    """Homelab presentation."""
    title = models.CharField(max_length=120)
    lab_image = models.ImageField()
    body = MDTextField()

    # Manager
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Homelab'

    def __str__(self):
        return 'Homelab'
