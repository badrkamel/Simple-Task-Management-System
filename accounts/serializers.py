from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from . import models

from rest_framework.serializers import (
        EmailField,
    )

UserModel = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):

    email = EmailField(label='Email Address')


    def create(self, validated_data):
        user = UserModel(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {
        		'write_only': True
        	}
        }
        
    def validate(self, data):
        return data

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', )