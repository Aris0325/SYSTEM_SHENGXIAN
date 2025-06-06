
# Create your models here.
from django.db import models

class Suppliers(models.Model):
    supplier_id = models.CharField(max_length=8, primary_key=True)
    supplier_name = models.CharField(max_length=50)
    address = models.TextField()
    contact_name = models.CharField(max_length=20)
    contact_phone = models.CharField(max_length=11)

    class Meta:
        db_table = 'suppliers'

class SupplierStatusLog(models.Model):
    log_id = models.CharField(max_length=10, primary_key=True)
    supplier_id = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    reason = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'supplier_status_log'

class PurchaseRequests(models.Model):
    request_id = models.CharField(max_length=10, primary_key=True)
    product_id = models.CharField(max_length=8)
    request_quantity = models.FloatField()
    request_time = models.DateTimeField()
    request_by = models.CharField(max_length=8)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'purchase_requests'

class PurchaseOrders(models.Model):
    purchase_id = models.CharField(max_length=8, primary_key=True)
    supplier_id = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    order_time = models.DateTimeField()
    expected_arrival = models.DateTimeField()
    order_status = models.CharField(max_length=20)

    class Meta:
        db_table = 'purchase_orders'

class PurchaseItems(models.Model):
    item_id = models.CharField(max_length=10, primary_key=True)
    purchase_id = models.ForeignKey(PurchaseOrders, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=8)
    quantity = models.FloatField()
    unit_price = models.FloatField()
    batch_id = models.CharField(max_length=12)
    trace_code = models.CharField(max_length=16)

    class Meta:
        db_table = 'purchase_items'

class PurchaseAcceptance(models.Model):
    acceptance_id = models.CharField(max_length=10, primary_key=True)
    item_id = models.ForeignKey(PurchaseItems, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField()
    accepted_quantity = models.FloatField()
    inspection_result = models.CharField(max_length=20)
    inspector = models.CharField(max_length=20)
    batch_id = models.CharField(max_length=12)

    class Meta:
        db_table = 'purchase_acceptance'