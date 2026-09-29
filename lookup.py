"""
Module 2: Attendee Lookup
"""
from modules.data import attendee_details


def show_attendee(name: str) -> None:
    """Finds and displays specific attendee details."""
    if name not in attendee_details:
        print(f"No attendee named {name} was found.")
        return

    details = attendee_details[name]
    payment_status = "paid" if details["paid"] else "payment due"
    print(f"{name}: {details['level']} level, {payment_status}")
