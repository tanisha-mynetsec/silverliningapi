from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.core.validators import RegexValidator


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self,username,email,name,address,phone,is_Under_Treatment,register,password=None):
        '''create a new user profile'''
        # if not email:
        #     raise ValueError('User must have an email address')
        # if not username:
            # raise ValueError('Username must be entered')    
        # if not contact_no:
        #     raise ValueError('User must have a contact number')

        email = self.normalize_email(email)
        user = self.model(username=username,email=email,name=name,address=address,phone=phone,is_Under_Treatment=is_Under_Treatment,register=register)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,username,email,password):
         '''Create and save a new superuser with given details'''
        #  if not email:
        #     raise ValueError('User must have an email address')
        #  if not username:
        #     raise ValueError('Username must be entered')    
         user = self.create_user(username=username,email=email, name='',address='',phone='',is_Under_Treatment=True,register='',password=password)
         if not username:
             user.delete()
             raise ValueError('Username must be entered')     
         if not email:
             user.delete()
             raise ValueError('User must have an email address')    
         user.is_admin =True
         user.is_staff=True
         user.is_superuser=True
         user.save(using=self._db)

         return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for user in the system"""
    email = models.EmailField(max_length=255,blank=True,default='',unique=True)
    name= models.CharField(max_length=40)
    address=models.TextField()
    # contact_no=models.IntegerField()
    is_Under_Treatment=models.BooleanField(default=False)
    # is_Insured=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    has_paid = models.BooleanField(default=False)
    #############################
    # city=models.CharField(max_length=20)
    # state=models.CharField(max_length=20)
    phone_regex=RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone=models.CharField(validators=[phone_regex], max_length=17, blank=True,default='') 
    username=models.CharField(blank=True,unique=True,max_length=100,default='')
    phone_confirmed=models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    CHOICES=[
        ('1','using phone'),
        ('2', 'using email'),
    ]
    register=models.CharField(choices=CHOICES,max_length=15)
    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['first_name','last_name','dob','address','city','state','institute','enrollment_no','contact_no','upload_id']
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        ''' Retrieve Full Name of the User '''
        return (self.name)

    def get_short_name(self):
        """Retrieve short name of user"""

        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.username

class Transaction(models.Model):
    user_profile=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    transaction_status=models.CharField(max_length=20,default='NA')
    transaction_id=models.CharField(max_length=100,default='NA')
    amount=models.IntegerField()

    def __str__(self):
        return self.user_profile.__str__()
