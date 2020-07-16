from django.shortcuts import render
from rest_framework import viewsets
from microblog_api import models, serializers
from rest_framework.authentication import TokenAuthentication
from microblog_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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

class BlogViewSet(viewsets.ModelViewSet):
    """ handles creating and updating blogs """
    serializer_class = serializers.BlogSerializer
    queryset = models.Blog.objects.all()
    permission_classes = (permissions.UpdateOwnBlog, IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ("id", "user", "text", )

class CommentViewSet(viewsets.ModelViewSet):
    """ handles creating and updating comment """
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = (permissions.UpdateOwnComment, IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ("id", "text", "blog")
