# datetime_operations.py

from datetime import datetime, date, time, timedelta

# 1. Current date and time
now = datetime.now()
print("Current Date & Time:", now)

# 2. Current date only
today = date.today()
print("Today's Date:", today)

# 3. Format date and time
formatted_date = now.strftime("%d-%m-%Y")
formatted_time = now.strftime("%H:%M:%S")

print("Formatted Date:", formatted_date)
print("Formatted Time:", formatted_time)

# 4. Extract individual components
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# 5. Create a custom date and time
custom_date = date(2026, 1, 26)
custom_time = time(10, 30, 0)

print("Custom Date:", custom_date)
print("Custom Time:", custom_time)

# 6. Add and subtract days using timedelta
future_date = today + timedelta(days=10)
past_date = today - timedelta(days=5)

print("Date after 10 days:", future_date)
print("Date before 5 days:", past_date)

# 7. Difference between two dates
date1 = date(2026, 1, 1)
date2 = date(2026, 1, 26)

difference = date2 - date1
print("Difference between dates:", difference.days, "days")

# 8. Convert string to date
date_string = "26-01-2026"
converted_date = datetime.strptime(date_string, "%d-%m-%Y")

print("Converted Date:", converted_date.date())

# 9. Convert date to string
date_to_string = today.strftime("%d/%m/%Y")
print("Date as string:", date_to_string)
