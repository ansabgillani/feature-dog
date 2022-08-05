from rest_framework import response, status
from rest_framework import generics
from users.serializers import (
    User,
    Organization,
    OrganizationSerializer,
    OrganizationProfile,
    OrganizationProfileSerializer
)


class OrganizaionListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def filter_data(self, data):
        # data is going to be a dictionary
        orgainzations = None
        if not data:
            orgainzations = Organization.objects.all()
        else:
            id = data.get('id', None)
            sort_asc = data.get('sort_asc', None)
            sort_dsc = data.get('sort_dsc', None)
            arguments = {
                'id': id,
                'organization_name': data.get('organization_name', None),
                'slug': data.get('slug', None),
                'website_link': data.get('website_link', None),
                'logo': data.get('logo', None),
                'description': data.get('description', None),
                'no_of_employees': data.get('no_of_employees', None)
            }
            arguments = {
                argument: query_data for argument, query_data in arguments.items() if query_data is not None
            }
            orgainzations = Organization.objects.filter(
                **arguments
            )
            if sort_asc and sort_dsc:
                orgainzations = orgainzations.order_by(
                    '-'+sort_dsc,
                    sort_asc
                )
            elif sort_dsc:
                orgainzations = orgainzations.order_by(
                    '-'+sort_dsc)
            elif sort_asc:
                orgainzations = orgainzations.order_by(
                    sort_asc)
        return orgainzations

    def get(self, request):
        try:
            orgainzations = self.filter_data(request.GET)
            serializer = OrganizationSerializer(
                orgainzations,
                many=True
            )
            return response.Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            data = {
                'error': str(e),
            }
            return response.Response(
                data=data,
                status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request):
        try:
            data = request.data
            organization = Organization.objects.create(
                organization_name=data.get('organization_name', None),
                slug=data.get('slug', None),
                website_link=data.get('website_link', None),
                logo=data.get('logo', None),
                description=data.get('description', None),
                no_of_employees=data.get('no_of_employees', None)
            )
            serializer = OrganizationSerializer(organization)
            return response.Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            data = {
                'error': str(e),
            }
            return response.Response(
                data=data,
                status=status.HTTP_404_NOT_FOUND
            )


class OrganizationProfileListCreateView(generics.ListCreateAPIView):
    queryset = OrganizationProfile.objects.all()
    serializer_class = OrganizationProfileSerializer

    def filter_data(self, organization, data):
        # data is going to be a dictionary
        organization_profiles = None
        if not data:
            organization_profiles = OrganizationProfile.objects.filter(
                organization=organization
            )
        else:
            user = User.objects.get(username=data['user']) if data.get(
                'user', None) else None
            sort_asc = data.get('sort_asc', None)
            sort_dsc = data.get('sort_dsc', None)
            arguments = {
                'id': data.get('id', None),
                'user': user,
                'professional_email': data.get('professional_email', None),
                'organization': organization,
                'role': data.get('role', None),
                'designation': data.get('designation', None)
            }
            arguments = {
                argument: query_data for argument, query_data in arguments.items() if query_data is not None
            }
            organization_profiles = OrganizationProfile.objects.filter(
                **arguments)
            if sort_asc and sort_dsc:
                organization_profiles = organization_profiles.order_by(
                    '-'+sort_dsc, sort_asc)
            elif sort_dsc:
                organization_profiles = organization_profiles.order_by(
                    '-'+sort_dsc)
            elif sort_asc:
                organization_profiles = organization_profiles.order_by(
                    sort_asc)
        return organization_profiles

    def get(self, request, organization_slug):
        try:
            organization = Organization.objects.get(slug=organization_slug)
            organization_profiles = self.filter_data(organization, request.GET)
            serializer = OrganizationProfileSerializer(
                organization_profiles, many=True)
            return response.Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            data = {
                'error': str(e),
            }
            return response.Response(
                data=data,
                status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request, organization_slug):
        try:
            data = request.data
            organization = Organization.objects.get(slug=organization_slug)
            user = User.objects.get(username=data.get('user'))
            organization_profile = OrganizationProfile.objects.create(
                organization=organization,
                user=user,
                professional_email=data.get('professional_email', None),
                role=data.get('role', None),
                designation=data.get('desgination', None),
                profile_image=data.get('profile_image', None)
            )
            serializer = OrganizationProfileSerializer(organization_profile)
            return response.Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            data = {
                'error': str(e),
            }
            return response.Response(
                data=data,
                status=status.HTTP_404_NOT_FOUND
            )
