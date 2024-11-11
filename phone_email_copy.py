#! python
# phone_email_copy.py - Find email and phone numbers in text and copy to clipboard - v0.0.0

import re
from pyperclip import copy as pcopy
from pyperclip import paste

r_phone = re.compile(r'''
  (\(\d{3}[.-]?\)|\d{3}[.-]?)       # Area Code
  (\d{3}[.-]?)                      # Telephone Prefix
  (\d{4})                           # Line Number
  (\s*(ext|x|ext.)\s*(\d{2,5}))*    # Extension
  ''', re.X)

r_email = re.compile(r'''
  ([\w._%+-]{1,64})         # Email Prefix
  ([@].{1,252})      # Separator and Domain
  ([.]\w{3})         # Top-level Domain
  ''', re.X)

def j_found_str(txt):
  temp = ''
  max = len(txt)
  if max > 0:
    for i in range(max):
      try:
        if i != max - 1:
          temp += ''.join(txt[i]) + '\n'
        else:
          temp += ''.join(txt[i])
      except IndexError:
        return None
    return temp
  else:
    return None

txt = paste()
phone_num = j_found_str(r_phone.findall(txt))
email = j_found_str(r_email.findall(txt))

if phone_num != None and email != None:
  txt = (f'Phone Number:\n{phone_num}\nEmail:\n{email}')
  pcopy(txt)
  print(paste())
elif phone_num != None:
  txt = (f'Phone Number:\n{phone_num}')
  pcopy(txt)
  print(paste())
elif email != None:
  txt = (f'Email:\n{email}')
  pcopy(txt)
  print(paste())
else:
  print('No phone numbers or emails found.')

'''
info@nostarch.com
info@nostarch.com
800-420-7240
415-863-9900
media@nostarch.com
415-863-9950
academic@nostarch.com
'''