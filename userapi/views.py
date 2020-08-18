
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from userapi import serializers
from userapi import models
from userapi import permissions
from django.utils.http import urlquote
from .forms import *

from rest_framework.decorators import api_view
from django.shortcuts import redirect,render

from django.http import JsonResponse
from mail_verification.views import usersignup
import requests
from django.db import IntegrityError
from django_rest_passwordreset.signals import reset_password_token_created

#------------------------------------------------------------------------------------------------------#

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle Creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email','phone')

    def create(self, request, *args, **kwargs):
        # flag=self.request.session['otp_session_data']
        response = super().create(request, *args, **kwargs)
        # here may be placed additional operations for
        # extracting id of the object and using reverse()

        try:
            flag=self.request.session['phone']    
        except KeyError:
            flag=False
        if flag:
            return Response({'Message': 'OTP Sent', 'session_data': request.session['otp_session_data'],
                             'phone': request.session['phone']})
    
        return Response({'Message':'Account activated'})

    # def perform_create(self,serializer):
    # #     # response=serializer.save()
    # #     # return Response(response)
    #     register=serializer.save()
    # #     # print(type(register))
    #     # return JsonResponse({'register':register},safe=False)
        # serializer.save()


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.TransactionSerializer
    queryset=models.Transaction.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnDisaster,IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user_profile')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if 'success' in serializer.validated_data['transaction_status'].lower():
            self.perform_create(serializer)
            self.request.user.has_paid=True
            headers = self.get_success_headers(serializer.data)
            response={}
            response["response"] = "payment successful"
            for x,y in serializer.data.items():
                 if x!='url' and x!='user_profile':
                     response[x]=y
            return Response(response, status=status.HTTP_201_CREATED, headers=headers)
        else:
            self.perform_create(serializer)
            response={}
            headers = self.get_success_headers(serializer.validated_data)
            response["response"]="payment failed please retry"
            for x,y in serializer.data.items():
                 if x!='url' and x!='user_profile':
                     response[x]=y
            return Response(response, status=status.HTTP_400_BAD_REQUEST, headers=headers)

    def perform_create(self,serializer):
            serializer.save(user_profile=self.request.user)
            # self.request.user.has_paid=True
            self.request.user.save(update_fields=['has_paid'])

    def update(self,request,*args,**kwargs):
        return Response({'message':"This instance can't be updated"})

@api_view(['GET', 'POST'])
def otp_verif_signup(request):
    # response_data = {}
    if request.method == "POST" :
        # form=OtpForm(request.POST)
        # if form.is_valid():
        # post=form.save(commit=False)
        '''above line not useful as save method is only present in modelform not in any other form'''
        user_otp = request.POST['otp']
        url = "http://2factor.in/API/V1/89e2e3d6-9d09-11ea-9fa5-0200cd936042/SMS/VERIFY/" + request.POST['session_data'] + "/" + user_otp + ""
        # otp_session_data is fetched from session.
        response = requests.request("GET", url)
        data = response.json()
        try:
            user=models.UserProfile.objects.get(phone=request.POST['phone'])
        except(TypeError, ValueError, OverflowError, models.UserProfile.DoesNotExist):
            user = None
        if user is not None:
            if data['Details'] == "OTP Matched":
                user.is_active = True
                user.username=request.POST['phone']
                user.phone_confirmed=True
                ''' see if above works'''
                try:
                    user.save(update_fields=['is_active','username','phone_confirmed',])
                except IntegrityError:
                    user.delete()
                    response_data= {'Message':'Registration Failed as another user with the same phone no. exists'}
                x=urlquote(user.username)
                url="https://2factor.in/API/R1/?module=TRANS_SMS&apikey=1b310933-9b9d-11ea-9fa5-0200cd936042&to="+user.phone+"&from=SLVRLG&templatename=CRED&var1="+user.name+"&var2="+x
                requests.request("GET",url)
                response_data = {'Message':'Successfully Registered'}
            else:
                # request.user.is_active= False
                # user=models.UserProfile.objects.get(phone=request.session['phone'])
                user.delete()
                response_data = {'Message':'Registration Failed'}
        else:
            response_data = {'Message':'Registration Failed'}
        return Response(response_data)
    else:
        form=OtpForm()
    return render(request,'registration/otp_signup.html',{'form':form})



class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    serializer_class = serializers.TokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        f_pass =  serializer.initial_data.get('forgot_password',False)
        if f_pass:
            #return Response({'Message': 'Password reset currently not working'})
            return redirect('password_reset')
        if serializer.is_valid(raise_exception=True):
        #     return Response(serializer.validated_data['phone'])
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            request.session['token']=token.key
            # request.session['phone']=user.phone
            # if user.phone:
            #     url = "http://2factor.in/API/V1/1b310933-9b9d-11ea-9fa5-0200cd936042/SMS/" + user.phone + "/AUTOGEN"
            #     response = requests.request("GET", url)
            #     data = response.json()
            #     request.session['otp_session_data'] = data['Details']
            # otp_session_data is stored in session.
            # response_data = {'Message':'Success'}
                #return redirect('otp_conf')
            return Response({'token':token.key})    
            # return redirect('login')


# @api_view(['GET','POST'])    
# def send_otp(request):
    
#     username=request.session['phone']
#     url = "http://2factor.in/API/V1/b3dc1967-9708-11ea-9fa5-0200cd936042/SMS/" + username + "/AUTOGEN/OTPSEND"
#     response = requests.request("GET", url)
#     data = response.json()
#     request.session['otp_session_data'] = data['Details']
#     # otp_session_data is stored in session.
#     # response_data = {'Message':'Success'}
#     return redirect('otp_conf')
#             # return JsonResponse(response_data) 

@api_view(['GET','POST'])
def otp_verification(request):
    # response_data = {}
    if request.method == "POST" :
        # form=OtpForm(request.POST)
        # if form.is_valid():
            # post=form.save(commit=False)
        '''above line not useful as save method is only present in modelform not in any other form'''
        user_otp = request.POST['otp']
        url = "http://2factor.in/API/V1/89e2e3d6-9d09-11ea-9fa5-0200cd936042/SMS/VERIFY/" + request.session['otp_session_data'] + "/" + user_otp + ""
        # otp_session_data is fetched from session.
        response = requests.request("GET", url)
        data = response.json()
        if data['Details'] == "OTP Matched":
            # request.user.is_active = True
            response_data = {'Message':'Success',
                            'Token' : request.session['token'],
            }
            # redirect(token_login)
        else:
            response_data = {'Message':'Failed'}
        return Response(response_data)
    else:
        form=OtpForm()
    return render(request,'registration/otp_login.html',{'form':form})

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_subject = 'Reset'
    message = render_to_string('reset_password.html', {
        'user': reset_password_token.user,
        'reset_password_url': reset_password_token.key
    })
    to_email = reset_password_token.user.email
    email = EmailMessage(email_subject, message, to=[to_email])
    email.send()
    #return Response({'token':reset_password_token.key})