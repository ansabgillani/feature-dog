from users.models import CustomerProfile, Organization, User
from posts.serializers import (
    CommentSerializer,
    PostSerializer,
    Post,
    UpvoteSerializer,
    CommentUpvoteSerializer,
)
from posts.models import (
    Post,
    CommentUpvote,
    Comment,
    Upvote,
    PostTag,
    Tag,
    PostImage,
)
from rest_framework import (
    generics,
    response,
    status,
)


class CommentRetriveView(generics.RetrieveAPIView):
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
    lookup_field = 'comment_key'

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


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # def get_queryset(self):
    #     self.kwargs.get
    #     return super().get_queryset()

    def get(self, request, organization_slug):
        try:
            organization = Organization.objects.get(slug=organization_slug)
            posts = Post.objects.filter(receiver=organization.pk)
            serializer = PostSerializer(posts, many=True)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response(
                data={
                    'error': str(e)
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request, organization_slug):
        try:
            data = request.data
            organization = Organization.objects.get(slug=organization_slug)
            user = User.objects.get(username=data['sender'])
            sender = CustomerProfile.objects.get(user=user)
            post = Post.objects.create(
                title=data.get('title'),
                body=data.get('body'),
                sender=sender,
                receiver=organization,
                is_draft=False,
                is_published=True,
            )

            post_images = data.get('post_images', None)
            if post_images:
                for post_image in post_images:
                    image = PostImage.objects.create(
                        image=post_image['image'], post=post)
                    image.save()
            post_tags = data.get('post_tags', None)
            if post_tags:
                for post_tag in post_tags:
                    tag_ = post_tag.get("tag")
                    tag = Tag.objects.get(color=tag_.get(
                        'color'), organization=organization)
                    p_tag = PostTag.objects.create(tag=tag, post=post)
                    p_tag.save()
            serializer = PostSerializer(post)
            return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
            # data["receiver_slug"] = organization_slug
            # serializer = PostSerializer(data=data)
            # if serializer.validate():
            #     serializer.save()

            #     return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return response.Response(
                data={
                    'error': str(e)
                },
                status=status.HTTP_404_NOT_FOUND
            )


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, pk, organization_slug):
        try:
            organization = Organization.objects.get(slug=organization_slug)
            post = Post.objects.get(receiver=organization, id=pk)
            serializer = PostSerializer(post)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response(
                data={
                    'error': str(e)
                },
                status=status.HTTP_404_NOT_FOUND
            )


class UpvoteListCreateView(generics.ListCreateAPIView):
    queryset = Upvote.objects.all()
    serializer_class = UpvoteSerializer

    def get(self, request, post_pk, organization_slug):
        try:
            organization = Organization.objects.get(slug=organization_slug)
            post = Post.objects.get(receiver=organization, id=post_pk)
            upvote = Upvote.objects.get(post=post)
            serializer = UpvoteSerializerß(upvote)
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
            upvote_by = User.objects.get(username=data['upvote_by'])

            upvote = Upvote.objects.create(
                upvote_by=upvote_by,
                post=post
            )
            serializer = UpvoteSerializer(upvote)
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
