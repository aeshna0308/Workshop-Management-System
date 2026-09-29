"""
Core Application Data & State
"""

# Tracks chronological signup order
signup_order = ["Asha", "Ben", "Chandra"]

# Ensures unique names for fast membership checks
registered_names = set(signup_order)

# Key-value store for attendee metadata
attendee_details = {
    "Asha": {"level": "beginner", "paid": True},
    "Ben": {"level": "intermediate", "paid": False},
    "Chandra": {"level": "beginner", "paid": True},
}

# Workshop agenda
workshop_schedule = {
    "09:00": "Collections overview",
    "10:00": "Hands-on list and set practice",
    "11:00": "Dictionary-based mini application",
}
