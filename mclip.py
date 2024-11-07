#! python
# mclip.py - multi-clipboard program. v0.0.0

from sys import argv

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(argv) < 2:
  print('error: no arguments provided')
  exit()
