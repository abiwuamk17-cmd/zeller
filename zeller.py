# File: zeller.py
# Description: Determines the day of the week for a given date
#              using Zeller's Congruence.
# Assignment Number: 3

# Name: Michael Abiwu
# SID: 2425402790
# Email: abiwuamk17@gmail.com
# Grader: Augustus Buckman

"""
On my honor, Michael Abiwu, this programming assignment is my own work
and I have not provided this code to any other student.


"""

month = input("Enter the month (for example, January, February, etc.): ")
day_in_month = int(input("Enter the day (an integer): "))
year = int(input("Enter the year (an integer): "))

if month == "January":
    month_number = 13
    year = year - 1
elif month == "February":
    month_number = 14
    year = year - 1
elif month == "March":
    month_number = 3
elif month == "April":
    month_number = 4
elif month == "May":
    month_number = 5
elif month == "June":
    month_number = 6
elif month == "July":
    month_number = 7
elif month == "August":
    month_number = 8
elif month == "September":
    month_number = 9
elif month == "October":
    month_number = 10
elif month == "November":
    month_number = 11
else:  # December
    month_number = 12

variation_in_days_per_month = (13 * (month_number + 1)) // 5

leap_year_days = (year // 4) + (year // 400)

century_days = year // 100

total_days = (day_in_month +
              variation_in_days_per_month +
              year +
              leap_year_days -
              century_days)

day_of_week = total_days % 7

if day_of_week == 0:
    day_name = "Saturday"
elif day_of_week == 1:
    day_name = "Sunday"
elif day_of_week == 2:
    day_name = "Monday"
elif day_of_week == 3:
    day_name = "Tuesday"
elif day_of_week == 4:
    day_name = "Wednesday"
elif day_of_week == 5:
    day_name = "Thursday"
else:
    day_name = "Friday"

print("The day of the week is " + day_name + ".")

