from django.db import models

# Create your models here.
from django.db import models

class TraceCodes(models.Model):
    trace_code = models.CharField(max_length=16, primary_key=True)
    product_id = models.CharField(max_length=8)
    batch_id = models.CharField(max_length=12)
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'trace_codes'

class TraceEvents(models.Model):
    event_id = models.CharField(max_length=10, primary_key=True)
    trace_code = models.ForeignKey(TraceCodes, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    actor = models.CharField(max_length=20)
    detail = models.TextField()

    class Meta:
        db_table = 'trace_events'