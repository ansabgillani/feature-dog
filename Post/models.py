from django.db import models
from User.models import BusinessTag


class Post(models.Model):
    statuses = (
        ('W', 'Waiting'),
        ('I', 'InProgress'),
        ('O', 'Ongoing'),
        ('C', 'Completed'),
    )
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=200)
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    status = models.CharField(max_length=1, choices=statuses)
    created_at = models.DateTimeField(max_length=30)
    updated_at = models.DateTimeField(max_length=30)
    is_draft = models.BooleanField()
    is_published = models.BooleanField()


class Comment(models.Model):
    body = models.CharField(max_length=200)
    sender = models.CharField(max_length=30)
    created_at = models.DateTimeField(max_length=30)
    is_internal = models.BooleanField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Upvote(models.Model):
    upvote_by = models.CharField(max_length=30)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)


class Tag(models.Model):
    tag_color = models.CharField(max_length=30)
    business_tag = models.ForeignKey(BusinessTag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class PostImage(models.Model):
    tag_id = models.ImageField(upload_to='uploads/post/images/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
