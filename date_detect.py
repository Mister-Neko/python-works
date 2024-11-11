#! Python
# date_detect - Finds date in the format DD/MM/YYYY and stores them in variables month, day, year.

import re

DMY = re.compile(r'''
  (\d{2}\\)  # Day
  (\d{2}\\)  # Month
  (\d{4})    # Year
  ''', re.X)

