from django.urls import path, include

from rest_framework.routers import DefaultRouter
from userapi import views


router = DefaultRouter()

router.register('profile',views.UserProfileViewSet)
# router = router.DefaultRouter(trailing_slash=False)
router.register('auth', views.AuthViewSet)
router.register('payment',views.TransactionViewSet)

urlpatterns = [
    path('login/',views.UserLoginApiView.as_view()),
    path('disaster/', include('disaster.urls')),
    path('',include(router.urls)),
    path('signup/otp/',views.otp_verif_signup,name='otp_signup'),
    path('otp/',views.otp_verification,name='otp_conf'),
]
