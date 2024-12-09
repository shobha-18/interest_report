from rest_framework import serializers
from .models import (
    TblBookingPaymentSchedule, 
    payment_master_tbl, 
    TblPaymentReceiptReferences, 
    TblCreditsNotesMaster, 
    TblCreditsNotesReferences
)
from .utils import calculate_due_amount, calculate_interest

class TblBookingPaymentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblBookingPaymentSchedule
        fields = '__all__'


class payment_master_tblSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment_master_tbl
        fields = '__all__'


class TblPaymentReceiptReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblPaymentReceiptReferences
        fields = '__all__'


class TblCreditsNotesMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblCreditsNotesMaster
        fields = '__all__'


class TblCreditsNotesReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblCreditsNotesReferences
        fields = '__all__'







class TblBookingPaymentScheduleSerializer(serializers.ModelSerializer):
    due_amount = serializers.SerializerMethodField()
    interest = serializers.SerializerMethodField()
    gst = serializers.SerializerMethodField()
    total_interest = serializers.SerializerMethodField()

    class Meta:
        model = TblBookingPaymentSchedule
        fields = '__all__'

    def get_due_amount(self, obj):
        receipt = payment_master_tbl.objects.filter(booking_id=obj.booking_id).first()
        if receipt:
            return calculate_due_amount(obj.total_amount, receipt.amount)
        return obj.total_amount

    def get_interest(self, obj):
        receipt = payment_master_tbl.objects.filter(booking_id=obj.booking_id).first()
        if receipt:
            due_amount = self.get_due_amount(obj)
            interest, _, _ = calculate_interest(due_amount, receipt.amount, obj.due_date, receipt.transaction_date)
            return interest
        return 0

    def get_gst(self, obj):
        receipt = payment_master_tbl.objects.filter(booking_id=obj.booking_id).first()
        if receipt:
            due_amount = self.get_due_amount(obj)
            _, gst, _ = calculate_interest(due_amount, receipt.amount, obj.due_date, receipt.transaction_date)
            return gst
        return 0

    def get_total_interest(self, obj):
        receipt = payment_master_tbl.objects.filter(booking_id=obj.booking_id).first()
        if receipt:
            due_amount = self.get_due_amount(obj)
            _, _, total_interest = calculate_interest(due_amount, receipt.amount, obj.due_date, receipt.transaction_date)
            return total_interest
        return 0
