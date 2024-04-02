from rest_framework import serializers

from .models import Company, Stock


class CompanySerializer(serializers.ModelSerializer):
    stock = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = '__all__'

    def get_stock(self, instance):
        stocks = Stock.objects.filter(company=instance).order_by('-created_at')
        return stocks[0].cost


class CompanyFullSerializer(serializers.ModelSerializer):
    stocks = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = '__all__'

    def get_stocks(self, company):
        return StockSerializer(Stock.objects.filter(company=company), many=True).data


class StockSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Stock
        fields = '__all__'


class StockOfCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ["cost", "created_at"]


class CompanyAndStockSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Stock
        fields = '__all__'
