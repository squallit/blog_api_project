from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models
from . import permissions

# Create your views here.

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        an_apiview = [
            "User HTTP methods as function (get, post, patch, put, delete)",
            "It is similar to a traditional Django view",
            "Gives you the most control over your logic",
            "is mapped manually to URLS"
        ]

        return Response({'message' : 'hello!', 'an_apiview': an_apiview})

    def post(self, request):

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):

        return Response({'method' : 'put'})

    def patch(self, request, pk=None):

        return Response({'method' : 'patch'})

    def delete(self, request, pk=None):

        return Response({'method' : 'delete'})




class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self, request):

        a_viewset = [
            "Use actions (list, create, retrieve, update, partial_update, destroy)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code."
        ]

        return Response({'message' : "Hello!", 'a_viewset' : a_viewset})

    def create(self, request):

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'http_method' : "GET"})

    def update(self, request, pk=None):
        return Response({'http_method' : "PUT"})

    def partial_update(self, request, pk=None):
            return Response({'http_method' : "PATCH"})

    def destroy(self, request, pk=None):
        return Response({'http_method' : "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    #TokenAuthentication store a authorized user's token in head of HTTP request
    authentication_classes = (TokenAuthentication,)
    #add permission class to ViewSet
    permission_classes = (permissions.UpdateOwnProfile,)
