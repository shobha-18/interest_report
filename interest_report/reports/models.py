from django.db import models
from django.utils import timezone



# Create your models here.
from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey
class TblBookingPaymentSchedule(models.Model):
    id = models.IntegerField(primary_key=True)
    percentage = models.FloatField()
    gst_percentage = models.FloatField()
    invoice_no = models.CharField(max_length=255)
    invoice_on = models.DateField()
    due_date = models.DateField()
    is_special_schedule = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    gst = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_balance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    stage_no = models.IntegerField()
    stage_name = models.CharField(max_length=255)
    booking_id = models.IntegerField()
    payment_schedule_id = models.IntegerField()

    
class payment_master_tbl(models.Model):
    id = models.IntegerField(primary_key=True)  # Manually assignable ID field
    receipt_no = models.CharField(max_length=255)
    pay_pattern = models.CharField(max_length=255)
    mode_of_pay = models.CharField(max_length=255)
    transaction_details = models.TextField()
    bank_name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()
    reference_doc = models.CharField(max_length=255)
    is_booking_receipt=models.BooleanField(default=False)
    comments = models.TextField()
    advance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    milestone_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    created_on = models.DateTimeField()
    created_on_new=models.CharField(max_length=255)
    bank_details_id = models.IntegerField()
    booking_id = models.IntegerField()
    created_by_id = models.IntegerField()
    customer_receipt = models.CharField(max_length=255)
    updated_on = models.TimeField()

    def __str__(self):
        return f"Payment Receipt {self.receipt_no}"
class TblPaymentReceiptReferences(models.Model):
    id = models.IntegerField(primary_key=True)  # Manually assignable ID field
    against = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    object_id = models.PositiveIntegerField()
    content_type_id = models.IntegerField()
    receipt_id = models.ForeignKey(payment_master_tbl, related_name='references', on_delete=models.CASCADE)

    def _str_(self):
        return f"Payment Receipt Reference {self.id}"

class TblCreditsNotesMaster(models.Model):
    id = models.IntegerField(primary_key=True)
    notes_no = models.CharField(max_length=255)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    advance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    milestone_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_approved = models.BooleanField(default=False)
    reject_reason = models.TextField(null=True, blank=True)
    approved_on = models.DateTimeField(null=True, blank=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    approved_by_id = models.IntegerField(null=True, blank=True)
    booking_id = models.IntegerField()
    category_id = models.IntegerField()
    created_by_id = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.is_approved and not self.approved_on:
            self.approved_on = timezone.now()

        if self.is_approved is None:
            self.is_approved = False

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Credit Note {self.id}"

class TblCreditsNotesReferences(models.Model):
    id = models.IntegerField(primary_key=True)
    against = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    object_id = models.PositiveIntegerField()
    content_type_id = models.IntegerField()
    notes_id = models.ForeignKey(TblCreditsNotesMaster, related_name='references', on_delete=models.CASCADE)

    # content_object = GenericForeignKey('content_type', 'object_id')

    def _str_(self):
        return f"Credit Note Reference {self.id}"