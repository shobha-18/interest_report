# Generated by Django 3.2 on 2024-06-24 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20240624_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblpaymentreceiptmaster',
            name='is_booking_receipt',
            field=models.BooleanField(default=False),
        ),
    ]
