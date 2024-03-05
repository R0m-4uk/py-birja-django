from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Stock, Company
from ..serializers import StockSerializer


class AddStock(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = StockSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AllStock(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)


class AddSmartStockAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        stock_data = request.data.get('stock', {})
        company_data = request.data.get('company', {})

        # Проверяем, существует ли компания
        company_title = company_data.get('title', None)
        company, created = Company.objects.get_or_create(title=company_title, defaults=company_data)

        if created:
            stock_data['cost'] = stock_data.get('cost', 0)

        # Связываем акцию с компанией
        stock_data['company'] = company.pk

        # Сериализуем данные акции
        stock_serializer = StockSerializer(data=stock_data)

        # Проверяем валидность данных
        if stock_serializer.is_valid():
            stock_serializer.save()
            return Response(stock_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(stock_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

