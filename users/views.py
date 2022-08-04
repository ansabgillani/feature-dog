from django.shortcuts import render
from django.http import JsonResponse
from users.serializers import UserSerializer, User


def users_data(request):
    data = User.objects.all()
    serializer = UserSerializer(data=data, many=True)
    return JsonResponse(serializer.data, safe=False)
