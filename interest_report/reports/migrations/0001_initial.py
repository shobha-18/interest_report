# Generated by Django 3.2 on 2024-06-23 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblBookingPaymentSchedule',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('percentage', models.FloatField()),
                ('gst_percentage', models.FloatField()),
                ('invoice_no', models.CharField(max_length=255)),
                ('invoice_on', models.DateField()),
                ('due_date', models.DateField()),
                ('is_special_schedule', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gst', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_paid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_balance_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stage_no', models.IntegerField()),
                ('stage_name', models.CharField(max_length=255)),
                ('booking_id', models.IntegerField()),
                ('payment_schedule_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TblCreditsNotesMaster',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('notes_no', models.CharField(max_length=255)),
                ('transaction_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('advance_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('milestone_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('reject_reason', models.TextField(blank=True, null=True)),
                ('approved_on', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('approved_by_id', models.IntegerField(blank=True, null=True)),
                ('booking_id', models.IntegerField()),
                ('category_id', models.IntegerField()),
                ('created_by_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TblPaymentReceiptMaster',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('receipt_no', models.CharField(max_length=255)),
                ('pay_pattern', models.CharField(max_length=255)),
                ('mode_of_pay', models.CharField(max_length=255)),
                ('transaction_details', models.TextField()),
                ('bank_name', models.CharField(max_length=255)),
                ('branch_name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_date', models.DateField()),
                ('reference_doc', models.CharField(max_length=255)),
                ('comments', models.TextField()),
                ('advance_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('milestone_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_on_new', models.DateTimeField(auto_now=True)),
                ('bank_details_id', models.IntegerField()),
                ('booking_id', models.IntegerField()),
                ('created_by_id', models.IntegerField()),
                ('customer_receipt', models.CharField(max_length=255)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblPaymentReceiptReferences',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('against', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type_id', models.IntegerField()),
                ('receipt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='references', to='reports.tblpaymentreceiptmaster')),
            ],
        ),
        migrations.CreateModel(
            name='TblCreditsNotesReferences',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('against', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type_id', models.IntegerField()),
                ('notes_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='references', to='reports.tblcreditsnotesmaster')),
            ],
        ),
    ]