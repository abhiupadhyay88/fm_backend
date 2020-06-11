from django.urls import path
from rest_framework import routers
from .views import FacilityView

router = routers.DefaultRouter()
router.register(r'api', FacilityView, 'facility')

