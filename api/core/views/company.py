from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.views import APIView

from rest_framework.response import Response



from core.serializers import CompanySerializer


# Создание компании
class AddCompany(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
