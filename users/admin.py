from django.contrib import admin
from users.models import (
    Organization,
    OrganizationProfile,
    CustomerProfile,
    AssociatedOrganizationToCustomer,
)



class OrganizationProfileInLine(admin.StackedInline):
    model = OrganizationProfile
    fields = (
        'user', 
        'professional_email',
        'designation',
        'profile_image',
        'role',
    )


@admin.register(CustomerProfile)
class CustomerProfile(admin.ModelAdmin):
    model = CustomerProfile
    list_display = ['profile_image']



@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [
        OrganizationProfileInLine,
    ]

    list_display = [
        'organization_name', 
        'slug', 
        'website_link', 
        'logo', 
        'description',
        'no_of_employees',
    ]
 