from django.db import models

# Create your models here.
from django.db import models

class DeliveryTasks(models.Model):
    delivery_id = models.CharField(max_length=8, primary_key=True)
    order_id = models.CharField(max_length=8)
    driver_id = models.CharField(max_length=8)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'delivery_tasks'

class DeliveryItems(models.Model):
    item_id = models.CharField(max_length=10, primary_key=True)
    delivery_id = models.ForeignKey(DeliveryTasks, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=8)
    batch_id = models.CharField(max_length=12)
    quantity = models.FloatField()

    class Meta:
        db_table = 'delivery_items'

class TemperatureLog(models.Model):
    log_id = models.CharField(max_length=10, primary_key=True)
    delivery_id = models.ForeignKey(DeliveryTasks, on_delete=models.CASCADE)
    time = models.DateTimeField()
    temperature = models.FloatField()
    gps_location = models.CharField(max_length=50)

    class Meta:
        db_table = 'temperature_log'

class DispatchOrders(models.Model):
    dispatch_id = models.CharField(max_length=10, primary_key=True)
    delivery_id = models.ForeignKey(DeliveryTasks, on_delete=models.CASCADE)
    assigned_by = models.CharField(max_length=8)
    assigned_time = models.DateTimeField()
    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'dispatch_orders'