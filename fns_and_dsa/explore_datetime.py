
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    # Format: YYYY-MM-DD HH:MM:SS
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")
    return current_date

def calculate_future_date(days_to_add):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted = future_date.strftime("%Y-%m-%d")
    print(f"Date after {days_to_add} days: {formatted}")
    return future_date



number_of_days = int(input("Enter the number of days to add to the current date:"))
calculate_future_date(number_of_days)
