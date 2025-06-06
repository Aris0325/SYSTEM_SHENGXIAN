from django.db import models

# Create your models here.
from django.db import models

class FinancialFlows(models.Model):
    flow_id = models.CharField(max_length=20, primary_key=True)
    type = models.CharField(max_length=10)
    source_id = models.CharField(max_length=8)
    amount = models.FloatField()
    reason = models.TextField()
    time = models.DateTimeField()

    class Meta:
        db_table = 'financial_flows'

class SalesPayment(models.Model):
    flow_id = models.CharField(max_length=20, primary_key=True)
    order_id = models.CharField(max_length=8)
    amount = models.FloatField()
    pay_time = models.DateTimeField()

    class Meta:
        db_table = 'sales_payment'

class PurchasePayment(models.Model):
    flow_id = models.CharField(max_length=20, primary_key=True)
    purchase_id = models.CharField(max_length=8)
    amount = models.FloatField()
    pay_time = models.DateTimeField()

    class Meta:
        db_table = 'purchase_payment'

class ReimbursementRequests(models.Model):
    reimbursement_id = models.CharField(max_length=10, primary_key=True)
    applicant_id = models.CharField(max_length=8)
    department = models.CharField(max_length=20)
    amount = models.FloatField()
    reason = models.TextField()
    status = models.CharField(max_length=20)
    submit_time = models.DateTimeField()
    audit_time = models.DateTimeField(blank=True, null=True)
    auditor_id = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        db_table = 'reimbursement_requests'