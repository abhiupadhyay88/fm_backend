"""
Serializers defined for creation of Facility
"""
from rest_framework import serializers
from .models import Facility
from datetime import datetime


class FacilitySerializer(serializers.ModelSerializer):
    creation_time = serializers.DateTimeField(required=False)
    updation_time = serializers.DateTimeField(required=False)

    class Meta:
        model = Facility
        fields = ['id', 'contact_name', 'contact_business_name', 'contact_email', 'contact_phone', 
                 'business_type', 'city', 'creation_time', 'updation_time']


    def create(self, validated_data):
        validated_data['creation_time'] = validated_data.get('creation_time',datetime.now())
        return Facility.objects.create(**validated_data)