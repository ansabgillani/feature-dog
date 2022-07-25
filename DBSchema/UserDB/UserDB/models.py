from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=80)
    website_link = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='uploads/business/logos/')
    description = models.CharField(max_length=200)
    no_of_employees = models.IntegerField()


class Profile(models.Model):
    roles = (
        ('A', 'Admin'),
        ('M', 'Moderator')
    )
    email = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to='uploads/business/profiles/')
    role = models.CharField(max_length=1, choices=roles)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
