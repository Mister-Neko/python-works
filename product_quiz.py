#! python
# product_quiz.py - Find the product of two numbers without using PyInputPlus- v0.0.0

from time import sleep
from time import time
from random import randint as r_int

score = 0
tries = 0

for i in range(10):
  t = int(time())
  n1 = r_int(0, 9)
  n2 = r_int(0, 9)
  answer = n1 * n2
# track tries and timeout
  while tries < 3:
    try:
      print(f'\n{i + 1}{chr(41)} {n1} * {n2} = ', end='')
      user_answer = int(input())
      if int(time()) - t > 8:
        print('Out of time!')
        tries = 0
        break
      elif user_answer == answer:
        print('\nCorrect!')
        score += 1
        tries = 0
        sleep(1)
        break
      elif tries == 2:
        print('Out of tries!')
        tries = 0
        break
      elif tries < 3:
        print('\nIncorrect, try again')
        tries += 1
    except ValueError:
      print('\nNot a number...')
      continue

total = int(score / 10 * 10)
if total % 10 == 0 and total != 0:
  print(f'\nYou Scored: {total}\nPerfect!')
else:
  print(f'Score: {total}')