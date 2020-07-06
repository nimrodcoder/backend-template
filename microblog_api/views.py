from django.shortcuts import render
from rest_framework import viewsets
from microblog_api import models, serializers
from rest_framework.authentication import TokenAuthentication
from microblog_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    """ handles creating and updating users """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ("id", "name", "email", )

class UserLoginAPIView(ObtainAuthToken):
    """ Handle creating user auth token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
