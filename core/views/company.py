from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.views import APIView

from rest_framework.response import Response

from ..models import Company, Stock
from ..serializers import StockSerializer



# Создание компании
from ..serializers import CompanySerializer


class AddCompany(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StockOfCompany(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        companies_id = request.data.get('companies', [])
        if len(companies_id) == 0:
            companies = Stock.objects.all()
        else:
            companies = Stock.objects.filter(company_id__in=companies_id)
        print(companies)
        serializer = StockSerializer(companies, many=True)
        return Response(serializer.data)


class AllCompany(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)
