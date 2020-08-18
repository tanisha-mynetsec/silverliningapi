from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .forms import UserSignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from userapi.models import UserProfile as u
from rest_framework.views import APIView
from rest_framework.response import Response
from hashlib import sha256
from django.db import IntegrityError
# from userapi.models import UserProfile


def usersignup(user):
            # user.is_active = False
            # user.save()
            email_subject = 'Activate Your Account'
            message = render_to_string('activate_account.html', {
                'user': user,
                'domain': 'silverliningapi.herokuapp.com',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = user.email
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()

def activate_account(request, uidb64, token):
    # print("its in")
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        print(uid)
        user = u.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, u.DoesNotExist):
        user = None
    if user is not None :
        if account_activation_token.check_token(user, token):
            #user.is_active = True
            user.username=user.email
            user.email_confirmed=True
            try:
                user.save()
            except IntegrityError:
                user.delete()
                return HttpResponse('Registration Failed as another user with same email exists')
            email_credentials(user)
            return HttpResponseRedirect("http://silverlining-global.com/kit/")
        else:
            # user.delete()
            return HttpResponse('Activation link is invalid!')
    else :
        return HttpResponse('Activation link is invalid!')

def email_credentials(user):
            # user.is_active = False
            # user.save()
            email_subject = 'Account Created Successfully!'
            message = render_to_string('login_credentials.html', {
                'user': user,
                'domain': 'silverliningapi.herokuapp.com',
            })
            to_email = user.email
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()        
