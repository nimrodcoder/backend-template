from rest_framework import serializers
from microblog_api import models

class UserProfileSerializer(serializers.ModelSerializer):
    """ serializes fields for user profile model """
    class Meta:
        model = models.UserProfile
        fields = ("id", "name", "email", "password")
        extra_kwargs = {
            'password' :{
                'write_only' : True,
                'style' : {'input_type' : 'password'}
            }
        }

    def create(self, validated_data):
        """ creates and returns a user """
        user = models.UserProfile.objects.create_user(
            name = validated_data["name"],
            email = validated_data["email"],
            password = validated_data["password"]
        )
        return user

    def update(self, instance, validated_data):
        """ handles updating a user """
        if "password" in validated_data:
            instance.set_password(password)
            password = validated_data.pop("password")

        return super().update(instance, validated_data)

class BlogSerializer(serializers.ModelSerializer):
    """ serializes fields for blog model """
    class Meta:
        model = models.Blog
        fields = ("id", "text", "likes")
        extra_kwargs = {
            'user' :{
                'read_only' : True,
            }
        }

class CommentSerializer(serializers.ModelSerializer):
    """ serializes fields for comments """
    class Meta:
        model = models.Comment
        fields = ("id", "text", "likes")
        extra_kwargs = {
            'user' :{
                'read_only' : True,
            }
        }
