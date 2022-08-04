from django.contrib import admin
from posts.models import (
    Post,
    Upvote,
    PostImage,
    Comment,
    CommentUpvote,
    PostTag,
    Tag
)


class UpvoteInline(admin.StackedInline):
    model = Upvote
    fields = ('upvote_by',)


class PostImageInline(admin.StackedInline):
    model = PostImage
    fields = ('image',)


class PostTagInline(admin.StackedInline):
    model = PostTag
    fields = ('tag',)


class CommentUpvoteInLine(admin.StackedInline):
    model = CommentUpvote
    fields = ('upvote_by',)


class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields=('created_at',)
    fields = (
        'body',
        'is_internal',
        'sender',
    )


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    inlines = [CommentUpvoteInLine, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        'color', 'name', 'organization'
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        UpvoteInline,
        PostImageInline,
        CommentInline,
        PostTagInline
    ]
    list_display = ['title', 'sender', 'receiver', 'status', 'created_at']
