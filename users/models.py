from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from slugify import slugify
from PIL import Image

from utils.assets import profile_directory_path, logo_directory_path


class Organization(models.Model):
    organization_name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    website_link = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=logo_directory_path, blank=True)
    description = models.TextField()
    no_of_employees = models.PositiveIntegerField()

    def __str__(self):
        return self.organization_name

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.slug = slugify(self.organization_name)
        super().save(*args, **kwargs)

        img = Image.open(self.logo.path)  # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # Resize image
            # Save it again and override the larger image
            img.save(self.logo.path)


class OrganizationProfile(models.Model):
    class OrganizationRoles(models.TextChoices):
        ADMIN = 'ADMIN', _('Admin')
        MODERATOR = 'MODERATOR', _('Moderator')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    professional_email = models.EmailField(unique=True)
    designation = models.CharField(max_length=255)
    profile_image = models.ImageField(
        upload_to=profile_directory_path, blank=True)
    role = models.CharField(
        max_length=255, choices=OrganizationRoles.choices, default=OrganizationRoles.ADMIN)

    def __str__(self):
        return self.organization.organization_name

    # Override the save method of the model
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_image.path)  # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # Resize image
            # Save it again and override the larger image
            img.save(self.profile_image.path)


class CustomerProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to=profile_directory_path, blank=True)

    def __str__(self):
        return self.user.get_username()

    # Override the save method of the model
    def save(self):
        super().save()

        img = Image.open(self.profile_image.path)  # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # Resize image
            # Save it again and override the larger image
            img.save(self.profile_image.path)


class AssociatedOrganizationToCustomer(models.Model):
    customer = models.ForeignKey(
        CustomerProfile, related_name='customer', on_delete=models.CASCADE)
    organization = models.ForeignKey(
        Organization, related_name='organization', on_delete=models.CASCADE)
