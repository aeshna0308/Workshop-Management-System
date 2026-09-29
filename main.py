"""
Main Entry Point
"""
from modules.lookup import show_attendee
from modules.payment import show_payment_summary
from modules.registration import register_attendee
from modules.schedule import show_schedule


def main():
    print("--- Workshop Signup Application ---\n")

    # 1. Registration Demo
    print("1. Registration Module:")
    print(register_attendee("Diego", "beginner", False))
    print(register_attendee("Asha", "beginner", True))
    print()

    # 2. Lookup Demo
    print("2. Attendee Lookup Module:")
    show_attendee("Diego")
    show_attendee("Unknown")
    print()

    # 3. Payment Tracking Demo
    print("3. Payment Tracking Module:")
    show_payment_summary()
    print()

    # 4. Schedule Demo
    print("4. Schedule Management Module:")
    show_schedule()


if __name__ == "__main__":
    main()
