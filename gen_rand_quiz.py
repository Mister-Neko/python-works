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

from random import choice
from random import randint
from os import path
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

states = tuple(capitals)
cap_only = tuple(capitals.values())

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

def r_q_order(qa):
  rqa = {}
  counter = 0
  
  while counter < 50:
    temp_q = choice(list(qa))
    temp_a = qa[temp_q]
    tl = []

    if temp_q in rqa:
      continue
    else:
      tstr = ''
      while len(tl) < 3:
        if temp_a not in (t := choice(list(qa.values()))):
          tl.append(t)
      tl.insert(randint(0, 3), temp_a)

      for i in range(4):
        tstr += f'\n{chr(97 + i)}. {tl[i]}'
      rqa[temp_q] = tstr
      
      counter += 1

  return rqa

def rqa_to_file(num, qa):
  header = 'State Captials Quiz\n'
  for i in range(num):
    rqa = r_q_order(qa)

    if path.isfile(f'capital_quiz{i + 1}.txt'):
      fobj = open(f'capital_quiz{i + 1}.txt', 'w')
      fobj.write('')
      fobj.close()

    fobj = open(f'capital_quiz{i + 1}.txt', 'a')
    q_num = 1
    fobj.write(header)
    for k in rqa:
      fobj.write(f'\n\n{q_num}. {k}\n{rqa[k]}')
      q_num += 1
    fobj.close()
    

q_and_a = state_cap_question(states, capitals)

rqa_to_file(1, q_and_a)

# r_q_order(q_and_a)