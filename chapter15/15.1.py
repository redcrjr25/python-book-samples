# Days of the Week Lab to print all 7 members of enum

from enum import Enum

class DayofWeek(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

for day in DayofWeek:
    print(day)
