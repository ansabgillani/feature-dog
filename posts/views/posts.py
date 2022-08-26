from users.models import CustomerProfile, Organization, User
from posts.serializers import (
    PostSerializer,
    Post,
    UpvoteSerializer,
)
from posts.models import (
    Post,
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


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def filter_data(self, receiver, data):
        # data is going to be a dictionary
        posts = None
        if not data:
            posts = Post.objects.filter(receiver=receiver)
        else:
            sender_username = data.get('sender', None)
            is_published = (True if data.get('is_published') == 'true' else False) if data.get(
                'is_published', None) else None
            is_draft = (True if data.get('is_draft') == 'true' else False) if data.get(
                'is_draft', None) else None
            status = data.get('status') if data.get('status') else None
            created_at = data.get('created_at') if data.get(
                'created_at') else None
            user = User.objects.get(
                username=data['sender']) if sender_username else None
            sort_asc = data.get('sort_asc', None)
            sort_dsc = data.get('sort_dsc', None)
            tags = data.get("tags", None)
            tags = tags.split(",")
            tags = Tag.objects.filter(organization=receiver, color__in=tags)
            arguments = {
                'receiver': receiver,
                'sender': CustomerProfile.objects.get(user=user) if sender_username else None,
                'is_published': is_published,
                'status': status,
                'is_draft': is_draft,
                'created_at': created_at,
                'post_tags__tag__in': tags,
            }
            arguments = {k: v for k, v in arguments.items() if v is not None}
            posts = Post.objects.filter(**arguments)
            if sort_asc and sort_dsc:
                posts = posts.order_by('-'+sort_dsc, sort_asc)
            elif sort_dsc:
                posts = posts.order_by('-'+sort_dsc)
            elif sort_asc:
                posts = posts.order_by(sort_asc)
        return posts

    def get(self, request, organization_slug):
        try:
            organization = Organization.objects.get(slug=organization_slug)
            posts = self.filter_data(receiver=organization, data=request.GET)
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
            upvote = Upvote.objects.filter(post=post)
            serializer = UpvoteSerializer(upvote)
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
