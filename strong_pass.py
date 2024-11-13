#! python
# strong_pass - Write a function to detection a strong password - v0.0.0

'''
Write a function that uses regular expressions to make sure the password string
it is passed is strong. A strong password is defined as one that is at least
eight characters long, contains both uppercase and lowercase characters, and
has at least one digit. You may need to test the string against multiple regex
patterns to validate its strength.
'''
import re

p_strength = re.compile(r'''
  ^(?=.*[A-Z])
  (?=.*[a-z])
  (?=.*\d)
  ([\w\S]{8,})
  # (?!.*\S)
  ''', re.X)

print('Enter in password:')
password = p_strength.match(input())

if password:
  print('Strong password')
else:
  print('Weak password')