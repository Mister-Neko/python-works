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
from pyperclip import copy as pcopy
from pyperclip import paste as ppaste

mcb_s = s_open('mcb')

try:
  if len(argv) == 1:
    print('No command or keword given.')
    exit()
  elif argv[1] == 'save':
    if argv[2]:
      mcb_s[argv[2]] = ppaste()
  elif argv[1] in mcb_s:
    pcopy(mcb_s[argv[1]])
  elif argv[1] == 'list':
    t_str = ''
    for k in mcb_s:
      t_str += f'{mcb_s[k]}\n'
    pcopy(t_str)
  elif argv[1] == 'delete':
    if argv[2] == 'all':
      for k in mcb_s:
        del mcb_s[k]
      pcopy('')
    elif argv[2] in mcb_s:
      del mcb_s[argv[2]]
except IndexError:
  print('error: no value given')
else:
  print('error: command not recognized')
  print('Require arguements:\n\tsave <keyword>\n\tlist <keyword>\n\t<keyword>')

mcb_s.close()