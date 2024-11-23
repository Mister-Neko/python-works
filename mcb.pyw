#! python
# mcb.pyw - Saves and loads pieces of text to the clipboard. - v0.0.0

'''
1. The command line argument for the keyword is checked.
2. If the argument is save, then the clipboard contents are saved to the keyword.
3. If the argument is list, then all the keywords are copied to the clipboard.
4. Otherwise, the text for the keyword is copied to the clipboard. [DEFAULT]

This means the code will need to do the following:

1. Read the command line arguments from sys.argv.
2. Read and write to the clipboard.
3. Save and load to a shelf file.

Usage: 
  py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
  py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
  py.exe mcb.pyw list - Loads all keywords to clipboard.
'''

from sys import argv
from shelve import open as s_open
from pyperclip import copy as cb_copy
from pyperclip import paste as cb_paste

mcb_s = s_open('mcb')

try:
  if len(argv) == 1:
    print('No command or keword given.')
    exit()
  elif argv[1] == 'save':
    if argv[2]:
      mcb_s[argv[2]] = cb_paste
  elif argv[1] in mcb_s:
    cb_copy(mcb_s[argv[1]])
  elif argv[1] == 'list':
    t_str = ''
    for k in mcb_s:
      t_str += f'{mcb_s[k]}\n'
except IndexError:
  print('error: no value given.')

mcb_s.close()