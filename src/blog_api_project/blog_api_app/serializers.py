from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):

    # Create fields to post / update
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        # model that the serializer represents
        model = models.UserProfile

        # fields that will display in response minus 'password'
        fields = ('id', 'email', 'name', 'password')
        # exlude 'password' in response
        extra_kwargs = {'password' : {'write_only':True}}


    def create(self, validated_data):

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )

        # set_password helps tokenize the text user enter
        user.set_password(validated_data['password'])
        # save to database
        user.save()

        return user
