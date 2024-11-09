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
  (\w{1,64})         # Email Prefix
  ([@].{1,252})      # Separator and Domain
  ([.]\w{3})         # Top-level Domain
  ''', re.X)

def j_found_str(txt):
  temp = ''
  max = len(txt)
  for i in range(max):
    try:
      if i != max - 1:
        temp += ''.join(txt[i]) + '\n'
      else:
        temp += ''.join(txt[i])
    except IndexError:
      return None
  return temp

txt = paste()
phone_num = j_found_str(r_phone.findall(txt))
email = j_found_str(r_email.findall(txt))

if phone_num != None and email != None:
  txt = (f'Phone Number:\n{phone_num}\nEmail:\n{email}')
  pcopy(txt)
elif phone_num != None:
  txt = (f'Phone Number: {phone_num}')
  pcopy(txt)
elif email != None:
  txt = (f'Email: {email}')
  pcopy(txt)

print(paste())

'''
Anne_Gibbons8910@zynuu.tech
Caleb_Evans4631@xqj6f.property
Joseph_Watt6556@ckzyi.store
Mya_Lunt2514@c2nyu.auction
Adalind_Henderson8008@voylg.business

418-543-8090
587-530-2271
404-724-1937
443-307-1473
329-420-1792
770-212-6011
473-522-7496
'''