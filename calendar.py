import calendar

def display_calendar():
    # Get user input
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))

    # Create a calendar object and format the month
    cal = calendar.TextCalendar(calendar.SUNDAY)
    month_calendar = cal.formatmonth(year, month)

    # Print the formatted calendar
    print(month_calendar)

# Call the function to display the calendar
display_calendar()
