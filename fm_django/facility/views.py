from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FacilitySerializer
from .models import Facility
from datetime import datetime 


class FacilityView(viewsets.ModelViewSet):
    serializer_class = FacilitySerializer
    queryset = Facility.objects.all()

        