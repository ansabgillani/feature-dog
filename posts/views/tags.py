from users.models import Organization
from posts.serializers import TagSerializer
from posts.models import Tag
from rest_framework import (
    generics,
    response,
    status,
)


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get(self, request, organization_slug):
        try:
            organization = Organization.objects.get(slug=organization_slug)
            tag = Tag.objects.filter(organization=organization)
            serializer = TagSerializer(tag, many=True)
            return response.Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
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
            tag = Tag.objects.create(
                color=data.get('color'),
                name=data.get('name'),
                organization=organization
            )
            serializer = TagSerializer(tag)
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
