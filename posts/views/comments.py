from users.models import Organization, User
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


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def filter_data(self, post, data):
        # data is going to be a dictionary
        comments = None
        if not data:
            comments = Comment.objects.filter(post=post)
        else:
            sender_username = data.get('username', None)
            is_internal = (True if data.get('is_internal') == 'true' else False) if data.get(
                'is_internal', None) else None
            arguments = {
                'post': post,
                'sender': User.objects.get(username=sender_username) if sender_username else None,
                'is_internal': is_internal,
            }
            arguments = {k: v for k, v in arguments.items() if v is not None}
            comments = Comment.objects.filter(**arguments)
        return comments

    def get(self, request, post_pk, organization_slug):
        try:
            organization = Organization.objects.get(slug=organization_slug)
            post = Post.objects.get(receiver=organization, pk=post_pk)
            comments = self.filter_data(post=post, data=request.GET)
            serializer = CommentSerializer(comments, many=True)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response(
                data={
                    'error': str(e)
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request, organization_slug, post_pk):
        try:
            data = request.data
            organization = Organization.objects.get(slug=organization_slug)
            post = Post.objects.get(receiver=organization, pk=post_pk)
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
