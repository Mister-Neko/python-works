#! Python
# date_detect - Finds date in the format DD/MM/YYYY and stores them in variables month, day, year.

import re
from sys import exit

DMY = re.compile(r'''
  ([0-3][\d])/  # Day
  ([0-1][\d])/  # Month
  ([1-2][\d]{3})    # Year
  ''', re.X)

print('Drop in date in the format DD/MM/YYYY:')
dates = DMY.findall(input())

try:
  day, month, year = dates[0]
except IndexError:
  print('Invalid date')
  exit()

# print(dates)

# print(f'day: {day}, month: {month}, year: {year}')

if int(month) > 12:
  print('Invalid date')
else:
  match int(month):
    case 2:
      if int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400):
        if int(day) != 29:
          print('Invalid date')
      elif int(day) > 28:
        print('Invalid date')
      else:
        print('Valid date.')
    case 4 | 6 | 9 | 11:
      print('here...')
      if int(day) > 30:
        print('Invalid date')
      else:
        print('Valid date.')
    case default:
      if int(day) > 31:
        print('Invalid date')
      else:
        print('Valid date.')