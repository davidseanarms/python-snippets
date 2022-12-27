# Gregorian Calendar
# Input date in format dd/mm/yyyy
date = input("Enter a date (dd/mm/yyyy): ")

# Split the input
try:
    day, month, year = date.split('/')
except ValueError:
    print("Invalid date format!")
    exit()

# Print Gregorian Calendar date
print("Gregorian Calendar Date:", date)

# Islamic Calendar
# Import module
import islamic.date as islamic_date

# Validate date
try:
    islamic_date.from_gregorian(int(year), int(month), int(day))
except ValueError:
    print("Invalid date!")
    exit()

# Convert Gregorian Calendar to Islamic Calendar
islamic_date = islamic_date.from_gregorian(int(year), int(month), int(day))

# Print Islamic Calendar date
print("Islamic Calendar Date:", islamic_date)

# Chinese Calendar
# Import module
import chinese_calendar as cc

# Validate date
try:
    cc.from_gregorian(int(year), int(month), int(day))
except ValueError:
    print("Invalid date!")
    exit()

# Convert Gregorian Calendar to Chinese Calendar
chinese_date = cc.from_gregorian(int(year), int(month), int(day))

# Print Chinese Calendar date
print("Chinese Calendar Date:", chinese_date)

# Julian Calendar
# Import module
from datetime import date
from julian import to_jd, from_jd

# Validate date
try:
    to_jd(date(int(year), int(month), int(day)))
except ValueError:
    print("Invalid date!")
    exit()

# Convert Gregorian Calendar to Julian Calendar
julian_date = to_jd(date(int(year), int(month), int(day)))

# Print Julian Calendar date
print("Julian Calendar Date:", julian_date)

# Hebrew Calendar
# Import module
import hebrew_calendar as hc

# Convert Gregorian Calendar to Hebrew Calendar
hebrew_date = hc.from_gregorian(int(year), int(month), int(day))

# Print Hebrew Calendar date
print("Hebrew Calendar Date:", hebrew_date)
