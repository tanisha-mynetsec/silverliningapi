from django.urls import path, include
from rest_framework.routers import DefaultRouter
from disaster import views
from.models import Riot

router=DefaultRouter()
router.register('nuclearwar',views.NuclearWarViewSet)
router.register('fire',views.FireViewSet)
router.register('pollution',views.PollutionViewSet)
router.register('terrorism',views.TerrorViewSet)
router.register('tsunami',views.TsunamiViewSet)
router.register('floods',views.FloodViewSet)
router.register('riots',views.RiotViewSet)
router.register('cyberattack',views.CyberViewSet)
router.register('earthquake',views.EarthQuakeViewset)


urlpatterns = [
    path('',include(router.urls)),
]