from rest_framework import serializers
from rest_framework.response import Response
from userapi import models
from mail_verification.views import usersignup
from rest_framework.authtoken.serializers import AuthTokenSerializer
import requests


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes a user profile object"""
    
    class Meta:
        model = models.UserProfile
        fields = (
        'id', 'username','password', 'url', 'name','email', 'phone','is_Under_Treatment','address','register')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
            },
            'username': {
                'read_only': True,
            },
        }

    def validate_register(self,value):
        if value=='1':
            if not self.initial_data.get('phone',''):
                raise serializers.ValidationError('Phone number is required')
            return value    
        else:
            if not self.initial_data.get('email',''):
                raise serializers.ValidationError('Email is required')
            return value

    def create(self, validated_data):
        '''Create and Return a new user'''
        register=validated_data['register']
        phone=validated_data['phone']
        if register =="1":
            uname=phone
        else:
            uname=validated_data['email']

        user = models.UserProfile.objects.create_user(
            username=uname,
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            address=validated_data['address'],
            is_Under_Treatment=validated_data['is_Under_Treatment'],
            phone=phone,
            register=register,
        )
        # return Response({'register':validated_data['register']})
        user.is_active=True
        # user.username=user.pk
        user.save(update_fields=['is_active',])

        # if register == '1':
        #     # return Response({'message':'register is 1'})
        #     # phone=serializer.validated_data['phone']
        #
        #     url = "http://2factor.in/API/V1/89e2e3d6-9d09-11ea-9fa5-0200cd936042/SMS/" + phone + "/AUTOGEN"
        #     response = requests.request("GET", url)
        #     request = self.context.get('request')
        #     data = response.json()
        #     request.session['otp_session_data'] = data['Details']
        #     request.session['phone'] = phone
        #
        # else:
        #     # return Response({'message':'register is not 1'})
        #     request=self.context.get('request')
        #     request.session['phone']= False
        #     usersignup(user)
            
        

        return user

class TransactionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=models.Transaction
        fields='__all__'
        read_only_fields=['user_profile']

class TokenSerializer(AuthTokenSerializer):
    forgot_password=serializers.BooleanField(default=False)

