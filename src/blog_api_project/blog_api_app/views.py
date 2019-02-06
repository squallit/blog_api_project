from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

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

        # call serializer
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
    # tell DRF to use Token Authentication system
    authentication_classes = (TokenAuthentication,)
    #add permission class to ViewSet, using tuple
    permission_classes = (permissions.UpdateOwnProfile,)

    #provide a tuple of filters, such as SearchFilter
    #add filter function to API
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    # Check email and password and returns an authtoken

    serializer_class = AuthTokenSerializer

    def create(self, request):

        # Use the ObtainAuthToken APIView to validate and create a token
        # since ObtainAuthToken is an APIView, so we "trick" it into a ViewSet
        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):

        serializer.save(user_profile=self.request.user)
