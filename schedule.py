"""
Module 4: Schedule Management
"""
from modules.data import workshop_schedule


def show_schedule() -> None:
    """Prints the scheduled workshop sessions."""
    for start_time, session_name in workshop_schedule.items():
        print(f"{start_time} - {session_name}")
