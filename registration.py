"""
Module 1: Registration Management
"""
from modules.data import attendee_details, registered_names, signup_order


def register_attendee(name: str, level: str, paid: bool) -> str:
    """Registers a new attendee if they are not already in the system."""
    if name in registered_names:
        return f"{name} is already registered."

    signup_order.append(name)
    registered_names.add(name)
    attendee_details[name] = {"level": level, "paid": paid}
    return f"{name} was registered successfully."
