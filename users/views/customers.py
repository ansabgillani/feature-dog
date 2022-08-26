from rest_framework import response, status
from rest_framework import generics
from users.serializers import (
    User,
    OrganizationProfile,
    CustomerProfile,
    CustomerProfileSerializer
)


class CustomerProfileListCreateView(generics.ListCreateAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer

    def filter_data(self, data):
        # data is going to be a dictionary
        customer_profiles = None
        if not data:
            customer_profiles = OrganizationProfile.objects.all()
        else:
            user = User.objects.get(username=data['user']) if data.get(
                'user', None) else None
            sort_asc = data.get('sort_asc', None)
            sort_dsc = data.get('sort_dsc', None)
            arguments = {
                'id': data.get('id', None),
                'user': user
            }
            arguments = {
                argument: query_data for argument, query_data in arguments.items() if query_data is not None
            }
            customer_profiles = OrganizationProfile.objects.filter(
                **arguments)
            if sort_asc and sort_dsc:
                customer_profiles = customer_profiles.order_by(
                    '-'+sort_dsc, sort_asc)
            elif sort_dsc:
                customer_profiles = customer_profiles.order_by(
                    '-'+sort_dsc)
            elif sort_asc:
                customer_profiles = customer_profiles.order_by(
                    sort_asc)
        return customer_profiles

    def get(self, request):
        try:
            customer_profiles = self.filter_data(request.GET)
            serializer = CustomerProfileSerializer(
                customer_profiles, many=True)
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
            user = User.objects.create(username=data.get('user'))
            customer_profile = CustomerProfile.objects.create(
                user=user,
                profile_image=data.get('profile_image', None)
            )
            serializer = CustomerProfileSerializer(customer_profile)
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
