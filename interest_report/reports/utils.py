from datetime import date

def calculate_due_amount(total_amount, received_amount):
    return total_amount - received_amount

def calculate_interest(due_amount, received_amount, due_date, received_date, percentage=10.25):
    if received_amount:
        no_of_days = (received_date - due_date).days
        interest = (received_amount * no_of_days * (percentage / 100)) / 365
    else:
        no_of_days = (received_date - due_date).days if received_date else 0
        interest = (due_amount * no_of_days * (percentage / 100)) / 365
    gst = interest * 0.18
    total_interest = interest + gst
    return interest, gst, total_interest
