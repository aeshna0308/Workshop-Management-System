"""
Module 3: Payment Tracking
"""
from modules.data import attendee_details


def show_payment_summary() -> None:
    """Calculates and displays aggregate payment statuses."""
    paid_count = sum(details["paid"] for details in attendee_details.values())
    unpaid_count = len(attendee_details) - paid_count
    print(f"Payments: {paid_count} paid, {unpaid_count} payment due")
