# Import a post_save signal when a user is created
from django.db.models.signals import post_save
# Import the built-in User model, which is a sender
from django.contrib.auth.models import User
from django.dispatch import receiver  # Import the receiver
from users.models import CustomerProfile


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         CustomerProfile.objects.create(user=instance)
