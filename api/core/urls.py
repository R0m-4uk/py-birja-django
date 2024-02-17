from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views.company import AddCompany, AllCompany, StockOfCompany
from core.views.stock import AddStock, AllStock

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # компании
    path("company/add/", AddCompany.as_view(), name='add_company_api'),
    path("company/all/", AllCompany.as_view(), name='all_company_api'),
    path("company/stocks/", StockOfCompany.as_view(), name='stock_of_company_api'),

    # акции
    path("stock/add/", AddStock.as_view(), name='add_stock_api'),
    path("stock/all/", AllStock.as_view(), name='all_stock_api'),
]