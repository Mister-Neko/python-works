#! python
# reg_txt_search.py - Open all files in a directory and search for any line that matches a user-supplied regular expression and print it to the screen. - v0.0.0

from os import listdir
from os import getcwd
from pyinputplus import inputRegexStr
import re

def read_lines_file(txt_file):
  with open(f'{getcwd()}\\{txt_file}', 'r', encoding='utf8') as fobj:
    return fobj.readlines()

text_file_only = re.compile(r'\w*[^ <>|\\:()&;,?*\'"]*\w[.]txt')

txt_files = text_file_only.findall(' '.join(listdir()))

user_regx = inputRegexStr(prompt='Enter text to search in REGEX format: ')

for f in txt_files:
  lines = read_lines_file(f)
  for l in lines:
    if user_regx.search(l):
      print(l)