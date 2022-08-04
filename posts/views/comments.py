from users.models import CustomerProfile, Organization, User
from posts.serializers import (
    CommentSerializer,
    Post,
    CommentUpvoteSerializer,
)
from posts.models import (
    Post,
    CommentUpvote,
    Comment,
)
from rest_framework import (
    generics,
    response,
    status,
)


class CommentRetrieveView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, comment_pk, post_pk, organization_slug):
        try:
            organization = Organization.objects.get(slug=organization_slug)
            post = Post.objects.get(receiver=organization, pk=post_pk)
            comment = Comment.objects.get(post=post, pk=comment_pk)
            serializer = CommentSerializer(comment)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response(
                data={
                    'error': str(e)
                },
                status=status.HTTP_404_NOT_FOUND
            )


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, organization_slug, post_pk):
        try:
            data = request.data
            organization = Organization.objects.get(slug=organization_slug)
            post = Post.objects.get(receiver=organization.pk, pk=post_pk)
            sender = User.objects.get(username=data.get('sender'))
            comment = Comment.objects.create(
                body=data.get('body'),
                sender=sender,
                post=post,
            )
            serializer = CommentSerializer(comment)
            return response.Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return response.Response(
                data={
                    'error': str(e)
                },
                status=status.HTTP_404_NOT_FOUND
            )


class CommentUpvoteListCreateView(generics.ListCreateAPIView):
    queryset = CommentUpvote.objects.all()
    serializer_class = CommentUpvoteSerializer

    def get(self, request, comment_pk, post_pk, organization_slug):
        try:
            organization = Organization.objects.get(slug=organization_slug)
            post = Post.objects.get(receiver=organization, pk=post_pk)
            comment = Comment.objects.get(post=post, pk=comment_pk)
            comment_upvote = CommentUpvote.objects.filter(comment=comment)
            serializer = CommentUpvoteSerializer(comment_upvote, many=True)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response(
                data={
                    'error': str(e)
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request, comment_pk, organization_slug, post_pk):
        try:
            data = request.data
            organization = Organization.objects.get(slug=organization_slug)
            post = Post.objects.get(receiver=organization, pk=post_pk)
            comment = Comment.objects.get(post=post, pk=comment_pk)
            upvote_by = User.objects.get(username=data['upvote_by'])

            comment_upvote = CommentUpvote.objects.create(
                upvote_by=upvote_by,
                comment=comment
            )
            serializer = CommentUpvoteSerializer(comment_upvote)
            return response.Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return response.Response(
                data={
                    'error': str(e)
                },
                status=status.HTTP_404_NOT_FOUND
            )
