""" 
How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)? 
"""

from collections import deque

days = deque(["Tuesday", "Wednesday", "Thursday", "Friday", 
              "Saturday", "Sunday", "Monday"])

month_names = {1: "January", 2: "February", 3: "March", 
               4: "April", 5: "May", 6: "June",
               7: "July", 8: "August", 9: "September",
              10: "October", 11: "November", 12: "December"}

months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
          7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

sundays = 0

for year in range(1901, 2001): 
    if year % 4 == 0: months[2] = 29
    else: months[2] = 28 
    for month in range(1, 13):
        for day_of_month in range(1, months[month] + 1): 
            day_of_week = days.popleft()
            days.append(day_of_week)
            if day_of_month == 1 and day_of_week == "Sunday":
                sundays += 1

print sundays 