from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        #fields = ("id", "title", "description", "created_at")
        fields = '__all__'
