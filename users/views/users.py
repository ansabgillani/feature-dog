from rest_framework import generics
from users.serializers import (
    User,
    UserSerializer
)


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
