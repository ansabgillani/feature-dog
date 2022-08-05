from django.urls import path
from users.views.users import UserListCreateView
from users.views.customers import CustomerProfileListCreateView
from users.views.organizations import (
    OrganizaionListCreateView,
    OrganizationProfileListCreateView
)


urlpatterns = [
    path('api/<organization_slug>/profiles', OrganizationProfileListCreateView.as_view(),
         name='organization_profiles_list_create_view'),
    # Organization Profiles List View

    path('api/customers/profiles', CustomerProfileListCreateView.as_view(),
         name='customer_profiles_list_create_view'),
    # Organization Profiles List View

    path('api/organizations', OrganizaionListCreateView.as_view(),
         name='organization_list_create_view'),
    # Organization List View

    path('api/users', UserListCreateView.as_view(),
         name='user_list_create_view'),
    # User List View
]
