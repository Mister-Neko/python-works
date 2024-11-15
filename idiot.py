#! python
# idiot.py - Loop while asking if the user wants to know how to keep an idiot busy - v0.0.0

'''
Project: How to Keep an Idiot Busy for Hours
Let’s use PyInputPlus to create a simple program that does the following:
1. Ask the user if they’d like to know how to keep an idiot busy for hours.
2. If the user answers no, quit.
3. If the user answers yes, go to Step 1.
Of course, we don’t know if the user will enter something besides “yes” or
“no,” so we need to perform input validation. It would also be convenient for
the user to be able to enter “y” or “n” instead of the full words.
PyInputPlus’s inputYesNo() function will handle this for us and, no matter
what case the user enters, return a lowercase 'yes' or 'no' string value.
'''

import re
from pyinputplus import inputStr
from pyinputplus import inputYesNo

txt = 'Do you want to know how to keep an idiot busy for hours? '
yes_response = ['y', 'yes']

while (user_response := inputYesNo(prompt=txt)) in yes_response:
  pass