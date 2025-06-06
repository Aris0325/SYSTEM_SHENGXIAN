from django.db import models

# Create your models here.
from django.db import models

class WarehouseStock(models.Model):
    product_id = models.CharField(max_length=8)
    batch_id = models.CharField(max_length=12, primary_key=True)
    quantity = models.FloatField()
    product_type = models.CharField(max_length=20)
    location_code = models.CharField(max_length=10)
    warehouse_status = models.CharField(max_length=10)
    entry_time = models.DateTimeField()
    trace_code = models.CharField(max_length=16)

    class Meta:
        db_table = 'warehouse_stock'

class StorageArea(models.Model):
    location_code = models.CharField(max_length=10, primary_key=True)
    type = models.CharField(max_length=10)
    description = models.TextField()
    manager = models.CharField(max_length=20)

    class Meta:
        db_table = 'storage_area'

class StockMovement(models.Model):
    flow_id = models.CharField(max_length=10, primary_key=True)
    batch_id = models.ForeignKey(WarehouseStock, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    operator = models.CharField(max_length=20)
    time = models.DateTimeField()

    class Meta:
        db_table = 'stock_movement'

class InventoryCheck(models.Model):
    check_id = models.CharField(max_length=10, primary_key=True)
    product_id = models.CharField(max_length=8)
    batch_id = models.ForeignKey(WarehouseStock, on_delete=models.CASCADE)
    recorded_quantity = models.FloatField()
    actual_quantity = models.FloatField()
    check_time = models.DateTimeField()
    checker = models.CharField(max_length=20)

    class Meta:
        db_table = 'inventory_check'

class WarehouseOperations(models.Model):
    operation_id = models.CharField(max_length=10, primary_key=True)
    type = models.CharField(max_length=10)
    related_order = models.CharField(max_length=8)
    operator = models.CharField(max_length=8)
    time = models.DateTimeField()
    remark = models.TextField()

    class Meta:
        db_table = 'warehouse_operations'

class BatchQualityLog(models.Model):
    batch_id = models.ForeignKey(WarehouseStock, on_delete=models.CASCADE)
    issue = models.TextField()
    report_time = models.DateTimeField()
    reporter = models.CharField(max_length=8)
    action_taken = models.TextField()

    class Meta:
        db_table = 'batch_quality_log'