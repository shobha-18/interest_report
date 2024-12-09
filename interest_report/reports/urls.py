from django.urls import path
from .views import get_payment_schedule_details

urlpatterns = [
    path('payment-schedule-details/', get_payment_schedule_details, name='payment_schedule_details'),
]