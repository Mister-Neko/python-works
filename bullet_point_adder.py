#! python
# bullet_point_addres.py - Adds bullet points '*' to items saved to the clipboard v0.0.0

# from sys import argv
from pyperclip import copy as pcopy
from pyperclip import paste

text = paste()

def add_bullet(txt):
  temp = txt.split('\n')

  for i in range(len(temp)):
    temp[i] = f'* {temp[i]}'

  temp = '\n'.join(temp)
  return temp

text = add_bullet(text)

pcopy(text)

print(paste())