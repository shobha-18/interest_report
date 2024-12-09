from django.shortcuts import render
from django.db.models import F, Sum
from .models import TblBookingPaymentSchedule, payment_master_tbl, TblPaymentReceiptReferences, TblCreditsNotesMaster, TblCreditsNotesReferences
from decimal import Decimal
from datetime import datetime

def calculate_interest(due_amount, received_amount, due_date, received_date, percentage):
    no_of_days_delay = max((received_date - due_date).days, 0)
    received_amount = Decimal(received_amount)
    due_amount = Decimal(due_amount)
    percentage_decimal = Decimal(percentage) / Decimal(100)  # Convert percentage to Decimal
    
    if received_amount > 0:
        interest = (received_amount * Decimal(no_of_days_delay) * percentage_decimal) / Decimal(365)
    else:
        interest = (due_amount * Decimal(no_of_days_delay) * percentage_decimal) / Decimal(365)
        
    gst = interest * Decimal(0.18)
    total_interest = interest + gst
    
    return {
        'interest': float(interest),
        'gst': float(gst),
        'total_interest': float(total_interest),
        'no_of_days_delay': no_of_days_delay
    }

def get_payment_schedule_details(request):
    data = []
    bookings = TblBookingPaymentSchedule.objects.all()
    serial_number = 1

    for booking in bookings:
        payment_receipts = payment_master_tbl.objects.filter(booking_id=booking.booking_id)
        total_received = Decimal(0)
        
        for receipt in payment_receipts:
            receipt_references = TblPaymentReceiptReferences.objects.filter(receipt_id=receipt.id)
            for ref in receipt_references:
                total_received += ref.amount
                receipt_type = "Receipt"
                due_amount = Decimal(booking.total_amount) if ref.id == 1 else max(Decimal(booking.total_amount) - total_received, Decimal(0))
                interest_details = calculate_interest(
                    due_amount=due_amount,
                    received_amount=ref.amount,
                    due_date=booking.due_date,
                    received_date=receipt.transaction_date,
                    percentage=10.25
                )
                data.append({
                    "S_No": serial_number,
                    "Flat_No": booking.booking_id,
                    "Customer_Name": "Static",
                    "Description": f"{booking.stage_name} & {booking.percentage}",
                    "DueDate": booking.due_date,
                    "DueAmount": float(due_amount),
                    "ReceivedDate": receipt.transaction_date,
                    "ReceiptType": receipt_type,
                    "AmountReceived": float(ref.amount),
                    "No_of_Days_Delay": interest_details['no_of_days_delay'],
                    "Percentage": 10.25,
                    "Interest": interest_details['interest'],
                    "GST": interest_details['gst'],
                    "TotalInterest": interest_details['total_interest']
                })
                serial_number += 1

            credit_notes = TblCreditsNotesMaster.objects.filter(booking_id=booking.booking_id)
            for note in credit_notes:
                credit_references = TblCreditsNotesReferences.objects.filter(notes_id=note.id)
                for ref in credit_references:
                    total_received += ref.amount
                    receipt_type = "TDS"
                    due_amount = Decimal(booking.total_amount)
                    interest_details = calculate_interest(
                        due_amount=due_amount,
                        received_amount=ref.amount,
                        due_date=booking.due_date,
                        received_date=note.transaction_date,
                        percentage=10.25
                    )
                    data.append({
                        "S_No": serial_number,
                        "Flat_No": booking.booking_id,
                        "Customer_Name": "Static",
                        "Description": f"{booking.stage_name} & {booking.percentage}",
                        "DueDate": booking.due_date,
                        "DueAmount": float(due_amount),
                        "ReceivedDate": note.transaction_date,
                        "ReceiptType": receipt_type,
                        "AmountReceived": float(ref.amount),
                        "No_of_Days_Delay": interest_details['no_of_days_delay'],
                        "Percentage": 10.25,
                        "Interest": interest_details['interest'],
                        "GST": interest_details['gst'],
                        "TotalInterest": interest_details['total_interest']
                    })
                    serial_number += 1

    # Adding headers
    headers = [
        "S.No", "Flat_No", "Customer_Name", "Description", "DueDate", "DueAmount",
        "ReceivedDate", "ReceiptType", "AmountReceived", "No_of_Days_Delay",
        "Percentage", "Interest", "GST", "TotalInterest"
    ]

    context = {
        "headers": headers,
        "data": data
    }

    return render(request, 'payment_schedule.html', context)