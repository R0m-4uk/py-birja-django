from rest_framework import serializers
from .models import Company, Stock


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyFullSerializer(serializers.ModelSerializer):
    stocks = serializers.SerializerMethodField()
    class Meta:
        model = Company
        fields = '__all__'

    def get_stocks(self, company):
        return StockSerializer(Stock.objects.filter(company=company), many=True).data



class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class StockOfCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ["cost", "created_at"]
