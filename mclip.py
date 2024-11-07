#! python
# mclip.py - multi-clipboard program. v0.0.0

from sys import argv
from pyperclip import copy as pcopy
from pyperclip import paste

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(argv) < 2:
  print('error: no arguments provided')
  exit()

key_phrase = argv[1]

if key_phrase in TEXT:
  pcopy(TEXT[key_phrase])
  print(f'Text for {key_phrase} copied to keyboard')
else:
  print(f'There is no text for {key_phrase}.')