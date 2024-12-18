# Generated by Django 3.2 on 2024-06-24 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20240624_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_master',
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
                ('is_booking_receipt', models.BooleanField(default=False)),
                ('comments', models.TextField()),
                ('advance_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('milestone_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField()),
                ('created_on_new', models.CharField(max_length=255)),
                ('updated_on', models.DateTimeField()),
                ('bank_details_id', models.IntegerField()),
                ('booking_id', models.IntegerField()),
                ('created_by_id', models.IntegerField()),
                ('customer_receipt', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='tblpaymentreceiptreferences',
            name='receipt_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='references', to='reports.payment_master'),
        ),
        migrations.DeleteModel(
            name='payment',
        ),
    ]
