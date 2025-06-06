from django.db import models

# Create your models here.
from django.db import models

class AfterSalesRequests(models.Model):
    request_id = models.CharField(max_length=10, primary_key=True)
    order_id = models.CharField(max_length=8)
    customer_id = models.CharField(max_length=8)
    request_time = models.DateTimeField()
    status = models.CharField(max_length=20)
    reason = models.TextField()

    class Meta:
        db_table = 'after_sales_requests'

class AfterSalesItems(models.Model):
    item_id = models.CharField(max_length=10, primary_key=True)
    request_id = models.ForeignKey(AfterSalesRequests, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=8)
    batch_id = models.CharField(max_length=12)
    quantity = models.FloatField()
    handling_result = models.TextField()

    class Meta:
        db_table = 'after_sales_items'

class AfterSalesResolution(models.Model):
    resolution_id = models.CharField(max_length=10, primary_key=True)
    request_id = models.ForeignKey(AfterSalesRequests, on_delete=models.CASCADE)
    decision = models.CharField(max_length=20)
    decision_by = models.CharField(max_length=8)
    decision_time = models.DateTimeField()
    refund_id = models.CharField(max_length=10)
    notes = models.TextField()

    class Meta:
        db_table = 'after_sales_resolution'