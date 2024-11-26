#! python
# rename_dates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY. - v0.0.0

from os import listdir
# from os import getcwd
from shutil import move
import re

a_date = re.compile(r'''
  ^(.*?)
  [^\d]([01]?[\d]{1}-)
  ([0-3]?[\d]{1}-)
  ((19|20)[\d]{2})
  (.*?)$''', re.X)

e_date = re.compile(r'''
  ^(.*?)
  [^\d]([01]?[\d]{1}-)
  ([0-3]?[\d]{1}-)
  ((19|20)[\d]{2})
  (.*?)$''', re.X)

def dates_a_to_e(f_dates, a_date):
  t_list = []
  for f in f_dates:
    a = a_date.search(f)
    m = a[2]
    d = a[3]
    f = f.replace(d, m, 1)
    f = f.replace(m, d, 1)
    t_list.append(f)
  return t_list


af_dates = []
for f in listdir():
  if a_date.search(f):
    af_dates.append(f)

ef_dates = dates_a_to_e(af_dates, a_date)

for i in range(len(af_dates)):
  move(af_dates[i], ef_dates[i])
  print(f'Renamed {af_dates[i]} as {ef_dates[i]}')