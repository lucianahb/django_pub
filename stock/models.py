from django.db import models

class Stock(models.Model):
    sku = models.CharField(max_length=50, primary_key=True, null=False, blank=False)
    quantity = models.IntegerField(null=False)
    id_product = models.IntegerField(null=False)
    id_seller = models.IntegerField(null=False)
