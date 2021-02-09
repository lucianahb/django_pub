from django.contrib import admin
from .models import Stock


class StockAdmin(admin.ModelAdmin):
    list_display = ('sku', 'quantity', 'id_product', 'id_seller')
admin.site.register(Stock, StockAdmin)