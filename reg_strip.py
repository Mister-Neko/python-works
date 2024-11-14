#! python
# reg_strip.py - remove whitespace from beginning and end of the string if no argument is passed - v0.0.0

'''
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to strip,
then whitespace characters will be removed from the beginning and end of the
string. Otherwise, the characters specified in the second argument to the
function will be removed from the string.
'''

import re

white_space = re.compile(r'''
  ((?!\s)[\w\W\s]+(?!\s)[\w\W\s])
  ''', re.X)

binary_choice = re.compile(r'''
  ^(?=[ynYN])
  [yesnoYESNO]{1,3}
  ''')

def txt_trimmer(txt):
  print('Add characters to trim, enter for default:')
  reg_char = input()
  
  if reg_char:
    trim = re.compile(f'(?![{reg_char}])[\\w\\W\\s]+(?![{reg_char}])[\\w\\W\\s]')
    temp = trim.findall(txt)
    return temp[0]
  else:
    temp = white_space.findall(txt)
    return temp[0]

print('Input text to trim:')
txt = input()

if txt:
  txt = txt_trimmer(txt)
  print(txt)
else:
  print('No text to trim.')