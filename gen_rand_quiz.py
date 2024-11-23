#! python
# gen_rand_quiz.py - Generate random questions for a quiz - v0.0.0

'''
Project: Generating Random Quiz Files
Say you’re a geography teacher with 35 students in your class and you want to
give a pop quiz on US state capitals. Alas, your class has a few bad eggs in
it, and you can’t trust the students not to cheat. You’d like to randomize the
order of questions so that each quiz is unique, making it impossible for anyone
to crib answers from anyone else. Of course, doing this by hand would be a
lengthy and boring affair. Fortunately, you know some Python.

Here is what the program does:

Create 35 different quizzes with 50 multiple-choice questions for each quiz, in random order
Provides the correct answer and three random wrong answers for each question, in random order
Writes the quizzes to 35 text files
Writes the answer keys to 35 text files
This means the code will need to do the following:

Store the states and their capitals in a dictionary
Call open(), write(), and close() for the quiz and answer key text files
Use random.shuffle() to randomize the order of the questions and multiple-choice options
'''

import re
from random import choice
from random import randint
from random import shuffle
from copy import deepcopy
from os import path
from pyinputplus import inputInt
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento',
            'Colorado': 'Denver', 'Connecticut': 'Hartford',
            'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines', 'Kansas':  'Topeka', 'Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge', 'Maine':  'Augusta',
            'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson', 'Missouri':  'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
            'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
            'Tennessee': 'Nashville', 'Texas': 'Austin',
            'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
            'Wyoming': 'Cheyenne'}


def state_cap_question(states, capitals):
  s = states
  c = capitals
  temp_q = {}

  for i in range(len(c)):
    if i % 5 == 0:
      temp_q[f'What is the capital of {states[i]}?'] = c[states[i]]
    elif i % 5 == 1:
      temp_q[f'{states[i]}\'s capital is?'] = c[states[i]]
    elif i % 5 == 2:
      temp_q[f'Name the capital of {states[i]}'] = c[states[i]]
    elif i % 5 == 3:
      temp_q[f'Which is the capital of {states[i]}?'] = c[states[i]]
    else:
      temp_q[f'Choose the capital name of the state of {states[i]}?'] = c[states[i]]
  
  return temp_q

def r_q_order(capitals):
  s = list(capitals.keys())
  c = capitals
  shuffle(s)
  rqa = state_cap_question(s, c)

  return rqa

def r_ma(qa):
  trqa = deepcopy(qa)
  tq = list(trqa.keys())
  
  for i in range(50):
    tl = []
    tstr = ''
    while len(tl) < 3:
      if trqa[tq[i]] not in (t := choice(list(qa.values()))):
        tl.append(t)
    tl.insert(randint(0, 3), trqa[tq[i]])

    for j in range(4):
      tstr += f'\n{chr(65 + j)}. {tl[j]}'
    trqa[tq[i]] = tstr
  return trqa


def rqa_to_file(num, qa):
  header1 = 'State Capitals Quiz'
  header2 = 'State Capitals Quiz Answer Keys'

  for i in range(num):
    rqa = r_q_order(qa)
    rqma = r_ma(rqa)

    if path.isfile(f'capital_quiz{i + 1}.txt'):
      fobj = open(f'capital_quiz{i + 1}.txt', 'w')
      fobj.write('')
      fobj.close()

    fobj = open(f'capital_quiz{i + 1}.txt', 'a')
    q_num = 1
    fobj.write(f'{header1} Test No. {i + 1}')
    for k in rqma:
      fobj.write(f'\n\n{q_num}. {k}\n{rqma[k]}')
      q_num += 1
    fobj.close()
  
    if path.isfile(f'capital_quiz_answer{i + 1}.txt'):
      fobj = open(f'capital_quiz_answer{i + 1}.txt', 'w')
      fobj.write('')
      fobj.close()

    fobj = open(f'capital_quiz_answer{i + 1}.txt', 'a')
    q_num = 1
    fobj.write(f'{header2} Test No. {i + 1}')
    for k in rqa:
      temp_l = rqma[k].split('\n')
      a = re.compile(fr'.*{rqa[k]}')
      for j in range(len(temp_l)):
        m = a.match(temp_l[j])
        if m:
          fobj.write(f'\n\n{q_num}. {k}\n{temp_l[j]}')
      q_num += 1
    fobj.close()
    



num = inputInt(prompt='Enter number of quizes: ', max=50)
rqa_to_file(num,  capitals)
