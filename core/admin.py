from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Company
from .models import Stock


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


class StockAdmin(admin.ModelAdmin):
    list_display = ['company', 'cost', 'created_at']


admin.site.register(Company, CompanyAdmin)
admin.site.register(Stock, StockAdmin)
