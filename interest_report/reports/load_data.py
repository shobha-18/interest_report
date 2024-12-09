import openpyxl
import datetime
from reports.models import TblBookingPaymentSchedule

# Load the workbook and select the sheet
workbook = openpyxl.load_workbook('/mnt/data/image.png')
sheet = workbook.active

# Iterate through the rows and create PaymentSchedule objects
for row in sheet.iter_rows(min_row=2, values_only=True):
    TblBookingPaymentSchedule.objects.create(
        id=row[0],
        percentage=row[1],
        gst_percentage=row[2],
        invoice_no=row[3],
        invoice_on=datetime.datetime.strptime(row[4], '%d-%m-%Y').date(),
        due_date=datetime.datetime.strptime(row[5], '%d-%m-%Y').date(),
        is_special_schedule=bool(row[6]),
        amount=row[7],
        gst=row[8],
        total_amount=row[9],
        total_paid_amount=row[10],
        total_balance_amount=row[11],
        stage_no=row[12],
        stage_name=row[13],
        booking_id=row[14],
        payment_schedule_id=row[15]
    )
