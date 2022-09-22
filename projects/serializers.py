from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Project


class projectSerializers(serializers.ModelSerializer):
    class Meta:
        model  =Project
        fields = ('id', 'title','description','tecnology','created_at')
        read_only_fields = ('created_at',)