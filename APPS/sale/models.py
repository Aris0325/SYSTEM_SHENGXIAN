from django.db import models

# Create your models here.
from django.db import models

class Customers(models.Model):
    customer_id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    address = models.TextField()

    class Meta:
        db_table = 'customers'

class SalesOrders(models.Model):
    order_id = models.CharField(max_length=8, primary_key=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    total_price = models.FloatField()
    order_time = models.DateTimeField()
    delivery_id = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        db_table = 'sales_orders'

class SalesItems(models.Model):
    item_id = models.CharField(max_length=10, primary_key=True)
    order_id = models.ForeignKey(SalesOrders, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=8)
    batch_id = models.CharField(max_length=12)
    unit_price = models.FloatField()
    quantity = models.FloatField()

    class Meta:
        db_table = 'sales_items'