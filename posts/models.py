from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from users.models import OrganizationProfile, Tag


class Post(models.Model):
    class STATUSES(models.TextChoices):
        WAITING = 'WAITING', _('waiting')
        IN_PROGRESS = 'IN_PROGRESS', _('in_progress')

    title = models.CharField(max_length=255)
    body = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(OrganizationProfile, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUSES, default=STATUSES.WAITING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_draft = models.BooleanField()
    is_published = models.BooleanField()


class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField()
    is_internal = models.BooleanField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class CommentUpvote(models.Model):
    upvote_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Upvote(models.Model):
    upvote_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class PostImage(models.Model):
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
