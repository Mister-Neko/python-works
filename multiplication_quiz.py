'''
Project: Multiplication Quiz
PyInputPlus’s features can be useful for creating a timed multiplication quiz.
By setting the allowRegexes, blockRegexes, timeout, and limit keyword argument
to pyip.inputStr(), you can leave most of the implementation to PyInputPlus.
The less code you need to write, the faster you can write your programs. Let’s
create a program that poses 10 multiplication problems to the user, where the
valid input is the problem’s correct answer. Open a new file editor tab and
save the file as multiplicationQuiz.py.
'''

from pyinputplus import inputStr as i_str
import pyinputplus as pyip
from random import randint as r_int
from time import sleep

num_q = 10
correct_a = 0

for q_num in range(num_q):
  n1 = r_int(0, 9)
  n2 = r_int(0, 9)
  
  prompt_str = f'#{q_num + 1}: {n1} x {n2} = '

  try:
    i_str(prompt_str, allowRegexes=[f'{n1 * n2}$'],
          blockRegexes=[('.*', 'Incorrect!')],
          timeout=8, limit=3)
  except pyip.TimeoutException:
    print('Out of time!')
  except pyip.RetryLimitException:
    print('Out of tires!')
  else:
    print('Correct!')
    correct_a += 1
  
  sleep(1)
print(f'Score: {int(correct_a / num_q * 10)}')