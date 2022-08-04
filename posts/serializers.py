from rest_framework import serializers
from posts.models import (
    Post,
    CommentUpvote,
    Comment,
    Upvote,
    PostTag,
    Tag,
    PostImage,
)


class CommentUpvoteSerializer(serializers.ModelSerializer):
    upvote_by = serializers.CharField(source='upvote_by.get_username')

    class Meta:
        model = CommentUpvote
        fields = ('upvote_by', 'comment')


class CommentSerializer(serializers.ModelSerializer):
    comment_upvotes = CommentUpvoteSerializer(many=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'body',
            'created_at',
            'is_internal',
            'sender',
            'post',
            'comment_upvotes',
        )

        read_only_fields = (
            'created_at',
        )


class UpvoteSerializer(serializers.ModelSerializer):
    upvote_by = serializers.CharField(source='upvote_by.get_username')

    class Meta:
        model = Upvote
        fields = (
            'upvote_by',
            'post'
        )


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('image',)


class TagSerializer(serializers.ModelSerializer):
    organization = serializers.CharField(
        source='organization.organization_name')

    class Meta:
        model = Tag
        fields = [
            'name',
            'color',
            'organization'
        ]


class PostTagSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = PostTag
        fields = (
            'tag',
        )


class PostSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.user.get_username')
    receiver = serializers.CharField(source='receiver.organization_name')
    receiver_slug = serializers.CharField(source='receiver.slug')
    comments = CommentSerializer(many=True)
    comment_count = serializers.SerializerMethodField()
    upvotes = UpvoteSerializer(many=True)
    post_images = PostImageSerializer(many=True)
    post_tags = PostTagSerializer(many=True)

    def get_comment_count(self, obj):
        return obj.comments.count()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'body',
            'sender',
            'receiver',
            'receiver_slug',
            'status',
            'updated_at',
            'is_draft',
            'is_published',
            'upvotes',
            'comment_count',
            'comments',
            'post_images',
            'post_tags',
        )

        read_only_fields = (
            'created_at',
        )

        # fields = '__all__'
