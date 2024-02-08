from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views.company import AddCompany

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # компании
    path("company/add/", AddCompany.as_view(), name='add_company_api'),

]