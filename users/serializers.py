from dataclasses import field
from rest_framework import serializers
from users.models import User, CustomerProfile, Organization, OrganizationProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CustomerProfileSerializer(serializers.ModelSerializer):
    user =  serializers.CharField(source='user.get_username')

    class Meta:
        model = CustomerProfile
        fields = '__all__'
        
        
class OrganizationProfileSerializer(serializers.ModelSerializer):
    user =  serializers.CharField(source='user.get_username')
    organization =  serializers.CharField(source='organization.organization_name', read_only=True)

    class Meta:
        model = OrganizationProfile
        fields = '__all__'
        
        read_only_fields = (
            'organization',
        )
        

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
        
