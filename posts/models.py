from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from users.models import Organization, CustomerProfile


class Post(models.Model):
    class STATUSES(models.TextChoices):
        WAITING = 'WAITING', _('waiting')
        IN_PROGRESS = 'IN_PROGRESS', _('in_progress')

    title = models.CharField(max_length=255)
    body = models.TextField()
    sender = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Organization, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=255, choices=STATUSES.choices, default=STATUSES.WAITING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_internal = models.BooleanField(default=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)


class CommentUpvote(models.Model):
    upvote_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, related_name="comment_upvotes", on_delete=models.CASCADE)


class Upvote(models.Model):
    upvote_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name="upvotes", on_delete=models.CASCADE)


class PostImage(models.Model):
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(
        Post, related_name="post_images", on_delete=models.CASCADE)


class Tag(models.Model):
    color = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(
        Organization, related_name="tags", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PostTag(models.Model):
    post = models.ForeignKey(Post, related_name='post_tags',
                             on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='org_tags',
                            on_delete=models.CASCADE)

