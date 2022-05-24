from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from users.api.serializers import UserSerializer
from users.models import User
from rest_framework.renderers import JSONRenderer

class UserListAPI(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class UserDetailAPI(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user)
        return Response(serializer.data)


    def put(self, request, pk):
        #user = User.object.get(pk=pk)
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
