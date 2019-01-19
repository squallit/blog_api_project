from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class HelloApiView(APIView):

    def get(self, request, format=None):

        an_apiview = [
            "User HTTP methods as function (get, post, patch, put, delete)",
            "It is similar to a traditional Django view",
            "Gives you the most control over your logic",
            "is mapped manually to URLS"
        ]

        return Response({'message' : 'hello!', 'an_apiview': an_apiview})
