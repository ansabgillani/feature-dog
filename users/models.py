from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Organization(models.Model):
    organization_name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    website_link = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='images/')
    description = models.TextField()
    no_of_employees = models.PositiveIntegerField()


class OrganizationProfile(models.Model):
    class OrganizationRoles(models.TextChoices):
        ADMIN = 'ADMIN', _('Admin')
        MODERATOR = 'MODERATOR', _('Moderator')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    professional_email = models.EmailField(unique=True)
    designation = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='images/')
    role = models.CharField(max_length=255, choices=OrganizationRoles.choices, default=OrganizationRoles.ADMIN)


class CustomerProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images/')


class AssociatedOrganizationToCustomer(models.Model):
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    organization = models.ForeignKey(OrganizationProfile, on_delete=models.CASCADE)


